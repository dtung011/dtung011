#1 connect to dtbase
from pymongo import MongoClient

uri = "mongodb://gottenvn:Tung11112010@ds119736.mlab.com:19736/tung_c4e17"
client = MongoClient(uri)

#2 Get default dtbase
db = client.get_default_database()

#3 Get blog collection
blog = db["blog"]
print (blog)

#4 Write a new blog
post = {"title": "Hôm nay trời dâm",
"Content": "Tôi không ở nhà code"}
blog.insert_one(post)

#5 look for blogs
all_posts = blog.find()
for post in all_posts:    
    print (post)