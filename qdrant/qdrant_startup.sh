#!/bin/bash

# Запуск локальной версии Qdrant
cd "qvdrant copy"
./qdrant.exe
  --name qdrant \
  -p 6333:6333 \
  -v qdrant_storage:/qdrant/storage \
  qdrant/qdrant:v1.0.0
  