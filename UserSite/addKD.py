import pymongo
from pymongo import MongoClient

client = MongoClient()
db = client.testDatabase
UserShoes = db.UserShoes

insert = {
	"name": "KD X"
	
}


result = UserShoes.insert_one(insert)
