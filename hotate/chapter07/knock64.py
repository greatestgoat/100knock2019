from pymongo import MongoClient
import pymongo
import json


class ArtistDB:
    def __init__(self, db_name='knock64', collection_name='artist'):
        self.client = MongoClient()
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_artist(self, filename='./artist.json', block_size=5000):
        block = list()
        for i, line in enumerate(open(filename, 'r')):
            artist_dic = json.loads(line)
            block.append(artist_dic)
            if i % block_size == 0:
                self.collection.insert_many(block)
                block = []
        self.collection.insert_many(block)

    def make_index(self):
        self.collection.create_index([('name', pymongo.ASCENDING)])
        self.collection.create_index([('aliases.name', pymongo.ASCENDING)])
        self.collection.create_index([('tags.value', pymongo.ASCENDING)])
        self.collection.create_index([('rating.value', pymongo.ASCENDING)])

    def artist_info(self, name):
        return self.collection.find({"name": name})

    def search_aliases(self, name):
        return self.collection.find({"aliases.name": name})


if __name__ == '__main__':
    from itertools import islice

    artist_db = ArtistDB()
    artist_db.insert_artist()
    artist_db.make_index()

    for post in islice(artist_db.collection.find(), 50):
        print(post)
