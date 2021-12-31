import requests
import json

header = {
    "User-Agent": "PocketFans201807/6.2.6_21121503 (Redmi Note8 Pro:Android 11;Xiaomi RP1A.2007.20.011)",
    "Content-Type": "application/json; charset=UTF-8",
    "appInfo": "{\"appBuild\":\"21121503\",\"appVersion\":\"6.2.6\"}",
    "token": "YKo7FVAAqbh/I6ddPzqLOV0Vbfb/j7H1j7Uctq6HQLuIKJQoYaUO3J1HOhIOW08t82a93BNzNhOLzHti7WVjIBVbvHeBJpT1"
             "/8LpvNtYtVU=",
    "pa": "''"
}

body = {
    "needTop1Msg": True,
    "nextTime": 0,
    "ownerId": "6737",
    "roomId": "67275431"
}

with open("roomId.json", 'r', encoding='UTF-8') as file:
    room_info = json.load(file)


def get_xox_message(name):
    body["ownerId"] = ""
    body["roomId"] = ""
    session = requests.session()
    res = session.post("https://pocketapi.48.cn/im/api/v1/chatroom/msg/list/homeowner", headers=header,
                       json=body).json()
    print(res)


def get_all_msg(name):
    a, b = search_room(name)
    body["ownerId"] = b
    body["roomId"] = a
    session = requests.session()
    res = session.post("https://pocketapi.48.cn/im/api/v1/chatroom/msg/list/all", headers=header, json=body).json()
    print(res)


def search_room(name):
    body["name"] = name
    session = requests.session()
    res = session.post("https://pocketapi.48.cn/im/api/v1/im/search", headers=header, json=body).json()["content"]["data"][0]
    return res["targetId"], res["ownerId"]


get_all_msg("邵雪聪")
