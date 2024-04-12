import redis

'''
    this class will implement redis cache system for our better performances
    properties -> cache : this property will save our redis class with its host and ports
'''
class Cache:
    def __init__(self):
        self.cache = redis.Redis(host='redis', port=6379)
        print('redis is ready on :6379')

    def find(self, query):
        print(F"redis is searching for {query}")
        return self.cache.get(query)
        

    def add(self, query, value):
        print(F"redis is saving this query:{query}")
        self.cache.set(query, value)

