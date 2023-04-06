import pymongo
import sys

port_number = int(sys.argv[1])
client = pymongo.MongoClient(f"mongodb://localhost:{port_number}/")
db = client["A4dbNorm"]
recordings_collection = db["recordings"]

results = recordings_collection.aggregate([
    {
        "$match": {
            "recording_id": {
                "$regex": "^70"
            }
        }
    },
    {
        "$group": {
            "_id": "",
            "avg_rhythmicality": {
                "$avg": "$rhythmicality"
            }
        }
    }
])

for result in results:
    print(result)
