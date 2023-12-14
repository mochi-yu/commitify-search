from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer

def serch_from_diff(diff: str) -> list[str]:
  encoder = SentenceTransformer('all-MiniLM-L6-v2')

  if encoder == None:
    print('encoder is None.')
    return []

  client = QdrantClient(host="qdrant-db", port=6333)

  hits = client.search(
      collection_name="git_log_data",
      query_vector=encoder.encode(diff).tolist(),
      limit=5
  )

  return [hit.payload['subject'] for hit in hits]
