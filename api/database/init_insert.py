from qdrant_client import models
import pickle

def insert_init_data(client):
  # エンコードしたデータの読み込み
  with open('./database/encoded_data.pickle', 'rb') as f:
    encoded_data = pickle.load(f)

    client.upload_records(
        collection_name="git_log_data",
        records=[
            models.Record(
                id=idx, vector=doc['vector'], payload=doc['payload']
            )
            for idx, doc in enumerate(encoded_data)
        ],
    )