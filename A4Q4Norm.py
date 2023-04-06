import pymongo
import sys
from datetime import datetime

port_number = int(sys.argv[1])
client = pymongo.MongoClient(f"mongodb://localhost:{port_number}/")
db = client["A4dbNorm"]
songwriters_collection = db["songwriters"]

results = songwriters_collection.aggregate([
    {
        "$unwind": "$recordings"
    },
    {
        "$lookup": {
            "from": "recordings",
            "localField": "recordings",
            "foreignField": "recording_id",
            "as": "recording"
        }
    },
    {
        "$unwind": "$recording"
    },
    {
        "$match": {
            "recording.issue_date": {
                "$gt": datetime(1950, 1, 1)
            }
        }
    },
    {
        "$project": {
            "_id": "$_id",
            "name": 1,
            "r_name": "$recording.name",
            "r_issue_date": "$recording.issue_date"
        }
    }
])

for result in results:
    print(result)
