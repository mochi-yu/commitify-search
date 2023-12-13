from qdrant_client import QdrantClient
import pickle

print('############# TEST ASK ##############')

client = QdrantClient(host="qdrant-db", port=6333)

with open('./database/encoded_data.pickle', 'rb') as f:
  encoded_data = pickle.load(f)

hits = client.search(
    collection_name="git_log_data",
    query_vector=encoded_data[0]['vector'],
    score_threshold=0.5,
    limit=5
)

for hit in hits:
    print("score:", hit.score, 'id: ', hit.id)
    print('msg: ', hit.payload['subject'])
    print("diff:\n", hit.payload['diffstr'])