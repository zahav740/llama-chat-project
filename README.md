# README.md
# Llama Chat Project

Этот проект представляет собой чат-бот, использующий локальную версию Llama модели для обработки естественного языка и генерации ответов, с Qdrant в качестве векторной базы данных.

## Установка

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/your-username/llama-chat-project.git
   cd llama-chat-project
   ```

2. Установите зависимости для каждого компонента:
   ```
   pip install -r server/requirements.txt
   pip install -r web/requirements.txt
   pip install -r llama_model/requirements.txt
   ```

3. Убедитесь, что у вас установлен Docker и Docker Compose.

4. Сгенерируйте gRPC код:
   ```
   python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/llama_service.proto
   ```

## Запуск

1. Запустите проект с помощью Docker Compose:
   ```
   docker-compose up --build
   ```

2. Откройте веб-браузер и перейдите по адресу `http://localhost:5000` для использования чат-интерфейса.

## Использование gRPC клиента

Для тестирования gRPC сервера напрямую:

```
python client/llama_client.py
```

## Структура проекта

- `protos/`: Содержит определение gRPC сервиса
- `server/`: gRPC сервер, интегрированный с Llama моделью и Qdrant
- `llama_model/`: Локальная версия Llama модели
- `qdrant/`: Конфигурация для Qdrant
- `web/`: Flask веб-сервер и HTML шаблон
- `client/`: gRPC клиент для тестирования

## Лицензия

MIT