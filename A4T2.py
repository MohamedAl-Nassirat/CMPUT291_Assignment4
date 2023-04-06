import pymongo
import bson.json_util
import sys

port_number = int(sys.argv[1])

with open('songwriters.json', encoding='utf-8') as f:
    songwriters_data = bson.json_util.loads(f.read())

with open('recordings.json', encoding='utf-8') as f:
    recordings_data = bson.json_util.loads(f.read())

client = pymongo.MongoClient(f"mongodb://localhost:{port_number}/")

db = client["A4dbEmbed"]
db.create_collection("SongwritersRecordings")

recordings_map = {recording["recording_id"]: recording for recording in recordings_data}


for songwriter in songwriters_data:
    embedded_recordings = [recordings_map[rec_id] for rec_id in songwriter["recordings"]]
    songwriter["recordings"] = embedded_recordings

db["SongwritersRecordings"].insert_many(songwriters_data)
