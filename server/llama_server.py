# server/llama_server.py
import grpc
from concurrent import futures
import llama_service_pb2
import llama_service_pb2_grpc
from llama_model.llama_model import LlamaModel
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
import os
from dotenv import load_dotenv
import uuid
from datetime import datetime, timedelta

load_dotenv()

llama_model = LlamaModel()
qdrant_client = QdrantClient("qdrant", port=6333)

# Создание коллекции, если она не существует
try:
    qdrant_client.create_collection(
        collection_name="conversation_history",
        vectors_config=VectorParams(size=384, distance=Distance.COSINE),
    )
except Exception as e:
    print(f"Collection already exists or error: {e}")

class LlamaServicer(llama_service_pb2_grpc.LlamaServiceServicer):
    def ProcessMessage(self, request, context):
        input_text = request.text
        
        embedding = llama_model.create_embedding(input_text)

        # Поиск релевантного контекста с учетом времени
        search_results = qdrant_client.search(
            collection_name="conversation_history",
            query_vector=embedding,
            limit=10,
            query_filter={
                "created_at": {
                    "$gte": (datetime.now() - timedelta(days=30)).timestamp()
                }
            }
        )

        # Сортировка результатов по релевантности и времени
        sorted_results = sorted(
            search_results,
            key=lambda x: (x.score, x.payload.get('created_at', 0)),
            reverse=True
        )

        # Выбор топ-5 результатов
        top_results = sorted_results[:5]

        context = "\n".join([result.payload.get('text', '') for result in top_results])

        response = llama_model.generate_response(f"Контекст: {context}\n\nВопрос: {input_text}\n\nОтвет:")

        # Сохранение нового вектора с метаданными
        qdrant_client.upsert(
            collection_name="conversation_history",
            points=[
                (
                    str(uuid.uuid4()),
                    embedding,
                    {
                        "text": input_text,
                        "created_at": datetime.now().timestamp(),
                        "importance": 1.0  # Начальная оценка важности
                    }
                )
            ]
        )

        return llama_service_pb2.MessageResponse(response=response)

    def PeriodicSummary(self):
        # Метод для периодического обобщения и обновления долгосрочной памяти
        recent_conversations = qdrant_client.scroll(
            collection_name="conversation_history",
            limit=1000,
            query_filter={
                "created_at": {
                    "$gte": (datetime.now() - timedelta(days=1)).timestamp()
                }
            }
        )

        summary_text = "Обобщение последних разговоров:\n"
        for conv in recent_conversations[0]:
            summary_text += f"- {conv.payload.get('text', '')}\n"

        summary_embedding = llama_model.create_embedding(summary_text)

        qdrant_client.upsert(
            collection_name="long_term_memory",
            points=[
                (
                    str(uuid.uuid4()),
                    summary_embedding,
                    {
                        "text": summary_text,
                        "created_at": datetime.now().timestamp(),
                        "type": "summary"
                    }
                )
            ]
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    llama_service_pb2_grpc.add_LlamaServiceServicer_to_server(LlamaServicer(), server)
    server.add_insecure_port('[::]:50051')
    print("Server started on port 50051")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()