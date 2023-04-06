import pymongo
import bson.json_util 
import sys

port_number = int(sys.argv[1])


# Load the songwriters data from the JSON file
with open('songwriters.json', encoding='utf-8') as f:
    songwriters_data = bson.json_util.loads(f.read())

# Load the recordings data from the JSON file
with open('recordings.json', encoding='utf-8') as f:
    recordings_data = bson.json_util.loads(f.read())

# Set up a connection to the MongoDB server
client = pymongo.MongoClient(f"mongodb://localhost:{port_number}/")



db = client["A4dbNorm"]
db.create_collection("songwriters")
db.create_collection("recordings")

db["songwriters"].insert_many(songwriters_data)
db["recordings"].insert_many(recordings_data)

