# step 1: Desgin databse: create a document in a collection
from mongoengine import StringField, IntField, Document
import mlab
from faker import Faker
from random import randint

fake = Faker()

mlab.connect()
class Blog(Document):
    title = StringField()
    likes = IntField()
    author = StringField()
    content = StringField()

# for i in range(50):
#     blog = Blog(title = fake.address(), likes = randint(0,100), author = fake.name(), content = fake.text())
#     blog.save()

greatlikes = Blog.objects(title__contains = "Unit")
# Read http://docs.mongoengine.org/guide/querying.html for more information of queries in MongoDB
for blog in greatlikes:
    print (blog["title"])
    print()
