import pymongo
import sys
from datetime import datetime

port_number = int(sys.argv[1])
client = pymongo.MongoClient(f"mongodb://localhost:{port_number}/")
db = client["A4dbEmbed"]
recordings_collection = db["SongwritersRecordings"]

results = recordings_collection.aggregate([
    {
        "$unwind": "$recordings"
    },
    {
        "$match": {
            "recordings.issue_date": {
                "$gt": datetime(1950, 1, 1)
            }
        }
    },
    {
        "$project": {
            "_id": "$_id",
            "name": 1,
            "r_name": "$recordings.name",
            "r_issue_date": "$recordings.issue_date"
        }
    }
])

for result in results:
    print(result)
