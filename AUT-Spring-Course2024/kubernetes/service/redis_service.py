import os
import redis



'''
    this class will implement redis cache system for our better performances
    properties -> cache : this property will save our redis class with its host and ports
'''
class RedisCacheSystem:

    def __init__(self):

        REDIS_HOST = os.getenv('REDIS_HOST') or '10.100.72.210'
        REDIS_PORT = os.getenv('REDIS_PORT') or '6379'
        self.cache = redis.Redis(host=REDIS_HOST, port=6379)
        print(f'redis is ready on {REDIS_HOST}:{REDIS_PORT}')

    def find(self, query):
        print(f"redis is searching for {query}")
        return self.cache.get(query)
        

    def add(self, query, value):
        print(f"redis is saving this query:{query}")
        self.cache.set(query, value)

    def clear(self):
        self.cache.flushdb()
        print("redis is cleared and empty")
