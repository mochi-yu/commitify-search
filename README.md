# commitify-search

## 起動コマンド
```
docker-compose build
docker-compose up -d

docker exec -it commitify-search-qdrant-client-1 python database/init.py
docker exec -d -it commitify-search-qdrant-client-1 python main.py
```