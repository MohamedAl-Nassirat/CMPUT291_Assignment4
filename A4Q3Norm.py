import pymongo
import sys

port_number = int(sys.argv[1])
client = pymongo.MongoClient(f"mongodb://localhost:{port_number}/")
db = client["A4dbNorm"]
songwriters_collection = db["songwriters"]
recordings_collection = db["recordings"]

results = recordings_collection.aggregate([
    {
        "$unwind": "$songwriter_ids"
    },
    {
        "$group": {
            "_id": "$songwriter_ids",
            "total_length": {"$sum": "$length"},
            "songwriter_id": {"$first": "$songwriter_ids"}
        }
    }
])

for result in results:
    print(result)
