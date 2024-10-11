# client/llama_client.py
import grpc
import llama_service_pb2
import llama_service_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = llama_service_pb2_grpc.LlamaServiceStub(channel)
        message = input("Введите ваше сообщение: ")
        response = stub.ProcessMessage(llama_service_pb2.MessageRequest(text=message))
        print("Ответ от Llama:", response.response)

if __name__ == '__main__':
    run()