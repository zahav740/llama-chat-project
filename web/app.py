# web/app.py
from flask import Flask, request, jsonify, render_template
import grpc
import llama_service_pb2
import llama_service_pb2_grpc

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    input_text = request.json['text']
    
    with grpc.insecure_channel('llama-server:50051') as channel:
        stub = llama_service_pb2_grpc.LlamaServiceStub(channel)
        response = stub.ProcessMessage(llama_service_pb2.MessageRequest(text=input_text))
    
    return jsonify({'response': response.response})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)