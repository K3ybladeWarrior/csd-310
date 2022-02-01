from pymongo import MongoClient

url ="mongodb+srv://admin:admin@cluster0.4pih1.mongodb.net/Cluster0?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

docs = db.students.find()

print(docs)

doc = db.students.find_one({"student_id": "1007"})
 
print(doc["student_id"])
