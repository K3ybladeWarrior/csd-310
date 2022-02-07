import certifi

from pymongo import MongoClient
ca=certifi.where()
url ="mongodb+srv://admin:admin@cluster0.4pih1.mongodb.net/Cluster0?retryWrites=true&w=majority"
client = MongoClient(url, tlsCAFile=ca)
db = client.pytech

fred = {
    "student_id": "1007",
    "firstName": "Fred",
    "lastName": "King"
}
bobby = {
    "student_id": "1008",
    "firstName": "Bobby",
    "lastName": "Davis"
}
toni = {
    "student_id": "1009",
    "firstName": "Toni",
    "lastName": "Lake"
}
    
 
fred_student_id = db.students.insert_one(fred).inserted_id
bobby_student_id = db.students.insert_one(bobby).inserted_id
toni_student_id = db.students.insert_one(toni).inserted_id

 
print(fred_student_id)
print(bobby_student_id)
print(toni_student_id)

 