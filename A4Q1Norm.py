import pymongo
import sys

port_number = int(sys.argv[1])
client = pymongo.MongoClient(f"mongodb://localhost:{port_number}/")
db = client["A4dbNorm"]
songwriters_collection = db["songwriters"]


results = songwriters_collection.aggregate([
    {
        "$match": {
            "recordings": {
                "$ne": []
            }
        }
    },
    {
        "$project": {
            "songwriter_id": 1,
            "name": 1,
            "num_recordings": {
                "$size": "$recordings"
            }
        }
    }
])

for result in results:
    print(result)
