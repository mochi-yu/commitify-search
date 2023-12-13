from qdrant_client import models, QdrantClient

from init_insert import insert_init_data

# エンコーダによりサイズが変わる
# 現在は all-MiniLM-L6-v2 を使用
VECTOR_SIZE = 384

client = QdrantClient(host="qdrant-db", port=6333)

client.delete_collection(
  collection_name='git_log_data'
)

client.recreate_collection(
    collection_name="git_log_data",
    vectors_config=models.VectorParams(
        size=VECTOR_SIZE,
        distance=models.Distance.COSINE,
    ),
)

insert_init_data(client)