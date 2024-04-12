import requests
from elasticsearch import Elasticsearch
import time


ELASTIC_USERNAME = 'elastic'
ELASTIC_PASSWORD = '12345'


def elasticsearch_initializing():
    url = 'https://elasticsearch:9200/bulk?pretty'
    json_file = 'movies.json'

    headers = {
        'Content-Type': 'application/json'
    }

    with open(json_file, 'rb') as f:
        data = f.read()

    response = requests.post(url, auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD), headers=headers, data=data, verify=False)

    while response.status_code != 200:
        print("Error during making index, wait")
        time.sleep(10)
        response = requests.post(url, auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD), headers=headers, data=data,verify=False)
    print("Elasticsearch database initialized successfully!")


class ElasticSearchService:
    def __init__(self):
        self.db = Elasticsearch("https://elasticsearch:9200", http_auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD))
        print(f"connected to elasticsearch service {self.db.ping()}")
        if self.db.ping():
            print(f"connected to elasticsearch service")

    def search(self, name):
        result = self.db.search(index='_all', body={"query": {"match": {"Series_Title": name}}})
        output = [hit['_source'] for hit in result['hits']['hits']]
        if output:
            return output
        else:
            return None
