import json

with open("test.json", 'r', encoding='UTF-8') as file:
    room_info = json.load(file)

print(room_info[0]["custom"])