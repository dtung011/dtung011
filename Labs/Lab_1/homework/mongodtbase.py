from pymongo import MongoClient
uri='mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client=MongoClient(uri)

db=client.get_default_database()

posts=db["posts"]

content={
    "title": "Paradox",
    "author": "Doan Duy Tung",
    "content": "hoho"
}
posts.insert_one(content)