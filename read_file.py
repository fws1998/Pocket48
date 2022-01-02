import json
import emoji

with open("test.json", 'r', encoding='UTF-8') as file:
    room_info = json.load(file)
for i in room_info:
    time_stamp = room_info[i]["time"]
    body = json.loads(room_info[i]["custom"])
    type = room_info[i]["type"]



def photo(timestamp, body):
    id = timestamp
