import pymongo
import sys

port_number = int(sys.argv[1])
client = pymongo.MongoClient(f"mongodb://localhost:{port_number}/")
db = client["A4dbEmbed"]
songwriters_collection = db["SongwritersRecordings"]

results = songwriters_collection.aggregate([
    {
        "$unwind": "$recordings"
    },
    {
        "$match": {
            "recordings.recording_id": {
                "$regex": "^70"
            }
        }
    },
    {
        "$group": {
            "_id": "",
            "avg_rhythmicality": {
                "$avg": "$recordings.rhythmicality"
            }
        }
    }
])

for result in results:
    print(result)
