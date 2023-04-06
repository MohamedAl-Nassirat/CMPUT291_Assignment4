import pymongo
import sys

port_number = int(sys.argv[1])
client = pymongo.MongoClient(f"mongodb://localhost:{port_number}/")
db = client["A4dbEmbed"]
songwriters_recordings_collection = db["SongwritersRecordings"]

results = songwriters_recordings_collection.aggregate([
    {
        "$unwind": "$recordings"
    },
    {
        "$group": {
            "_id": "$songwriter_id",
            "total_length": {"$sum": "$recordings.length"},
            "songwriter_id": {"$first": "$songwriter_id"}
        }
    }
])

for result in results:
    print(result)
