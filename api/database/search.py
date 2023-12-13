from qdrant_client import QdrantClient
import pickle

def serch_from_diff() -> list[str]:
  client = QdrantClient(host="qdrant-db", port=6333)

  with open('./database/encoded_data.pickle', 'rb') as f:
    encoded_data = pickle.load(f)

  hits = client.search(
      collection_name="git_log_data",
      query_vector=encoded_data[0]['vector'],
      score_threshold=0.5,
      limit=5
  )

  return [hit.payload['subject'] for hit in hits]
