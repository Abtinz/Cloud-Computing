import requests
from elasticsearch import Elasticsearch
import time


ELASTIC_USERNAME = 'elastic'
ELASTIC_PASSWORD = '12345'


    
class ElasticSearchService:
    def __init__(self):
        print(f"connected to elasticsearch service")

    def search(self, name):
        
        client = Elasticsearch('https://localhost:9200',http_auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD),verify_certs=False)
        res = client.search(index="your_index_name", query={
            "match": {
                "Series_Title": name
            }
        })
        client.close()
        return res['hits'], res['hits']['hits']
    
