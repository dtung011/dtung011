from pymongo import MongoClient
uri='mongodb://admin:admin@ds021182.mlab.com:21182/c4e'
client=MongoClient(uri)

db=client.get_default_database()

customers = db["customers"]

events=customers.find({"ref":"events"}).count()
wom=customers.find({"ref":"wom"}).count()
ads=customers.find({"ref":"ads"}).count()

from matplotlib import pyplot
ref_counts = [events, wom, ads]
ref_labels = ["events", "wom", "ads"]
pyplot.pie(ref_counts, labels = ref_labels, autopct = "%.1f%%")
pyplot.axis("equal")
pyplot.show()