import certifi
from pymongo import MongoClient
ca=certifi.where()

url ="mongodb+srv://admin:admin@cluster0.4pih1.mongodb.net/Cluster0?retryWrites=true&w=majority"
client = MongoClient(url, tlsCAFile=ca)
db = client.pytech

docs = db.students.find()

print(docs)

doc = db.students.find_one({"student_id": "1008"})
 
print(doc["student_id"])
