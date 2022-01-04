import json
import psycopg2
import os


def photo_audio_video(timestamp, body, type, room):
    url = body["file"]["url"]
    custom = json.loads(body["custom"])
    userId = custom["user"]["userId"]
    name = custom["user"]["nickName"]
    if type == "audio":
        url = body["file"]["mp3Url"]
    sql = "INSERT INTO " + type + " VALUES (" + "to_timestamp(" + str(timestamp) + "), \'" + url + "\'," + str(
        userId) + ",\'" + name + "\'," + room + ")"
    try:
        # print(sql)
        cur.execute(sql)
        conn.commit()
    except psycopg2.errors.UniqueViolation as error:
        conn.rollback()


def normal_text_msg(time, body, room):
    if  body["messageType"] != "DELETE" and body["messageType"] != "DISABLE_SPEAK":
        userId = body["user"]["userId"]
        name = body["user"]["nickName"]

    # body = json.loads(body)
        if userId in list:
            sql = ""
            if "replyName" in body:
                msg = body["text"]
                reply_to = body["replyName"]
                reply_text = body["replyText"]
                sql = "INSERT INTO reply VALUES (" + "to_timestamp(" + str(time) + "), \'" + msg + "\'," + str(
                    userId) + ",\'" + name + "\'," + room + ", \'"+ reply_to +"\', \'"+ reply_text + "\')"

            elif "liveCover" in body:
                title = body["liveTitle"]
                id = body["liveId"]
                path = body["shortPath"]

                sql = "INSERT INTO live VALUES (" + "to_timestamp(" + str(time) + "), \'" + title + "\'," + str(
                    userId) + ",\'" + name + "\'," + id +", \'" + path + "\')"

            elif "giftInfo" in body:
                '''gift = body["giftInfo"]["giftName"]
                price = body["giftInfo"]["money"]
                accecpId = body["giftInfo"]["acceptUserId"]
                acceptName= body["giftInfo"]["acceptUserName"]'''

                # sql = "INSERT INTO idol_msg VALUES (" + "to_timestamp(" + str(time) + "), \'" + gift + "\'," + userId + ",\'" + name + "\'," + room + ")"

            elif body["messageType"] == "EXPRESSIMAGE":
                msg = body["emotionRemote"]
                sql = "INSERT INTO idol_msg VALUES (" + "to_timestamp(" + str(time) + "), \'" + msg + "\'," + str(
                    userId) + ",\'" + name + "\'," + room + ")"

            else:
                msg = body["text"]
                sql = "INSERT INTO idol_msg VALUES (" + "to_timestamp(" + str(time) + "), \'" + msg + "\'," + str(
                    userId) + ",\'" + name + "\'," + room + ")"


            try:
                if sql != "":
                    # print(sql)
                    cur.execute(sql)
                    conn.commit()
            except psycopg2.errors.UniqueViolation as error:
                conn.rollback()


def flipcard(time, body):
    question = body["question"]
    reply = body["answer"]
    userId = body["user"]["userId"]
    name = body["user"]["nickName"]
    if "url" in reply:
        reply = json.loads(reply)
        reply = reply["url"]
        print(reply)
    sql = "INSERT INTO flipcard VALUES (" + "to_timestamp(" + str(time) + "), \'" + question +"\', \'" + reply + "\'," + str(
        userId) + ",\'" + name + "\'" + ")"
    try:
        # print(sql)
        cur.execute(sql)
        conn.commit()
    except psycopg2.errors.UniqueViolation as error:
        conn.rollback()


if __name__ == '__main__':
    list = [1, 4, 5, 6, 8, 9, 11, 12, 17, 18, 19, 20, 21, 24, 25, 27, 28, 33, 34, 35, 36, 38, 39, 40, 46, 47, 49, 63,
            68, 2508, 5562, 5564, 5566, 5574, 5973, 6429, 6431, 6734, 6735, 6737, 6738, 6739, 6742, 6743, 6744, 6745,
            6746, 9073, 49003, 49005, 63548, 63554, 63555, 63558, 63559, 63560, 63561, 63562, 63564, 63566, 63567,
            63571, 63572, 63573, 63574, 63576, 63577, 63580, 63581, 63582, 286973, 286976, 286977, 286979, 286983,
            327558, 327560, 327561, 327563, 327566, 327567, 327568, 327569, 327571, 327572, 327574, 327575, 327577,
            327579, 327580, 327581, 327587, 327594, 327595, 327596, 327597, 327598, 327601, 327602, 327682, 327683,
            399631, 399652, 399654, 399662, 399667, 399669, 399672, 399674, 407106, 407108, 407110, 407121, 407126,
            407127, 407130, 417311, 417320, 417321, 417324, 417325, 417326, 417329, 417330, 417331, 417336, 419966,
            458335, 459989, 459991, 459997, 459999, 460004, 460005, 460933, 480675, 480680, 526172, 528329, 528335,
            528336, 528337, 528340, 529287, 530383, 530385, 530388, 530390, 530431, 530433, 530439, 530440, 530447,
            530452, 538697, 538735, 593820, 594002, 594003, 601302, 607507, 607511, 607513, 607515, 607521, 607523,
            607524, 607591, 609002, 610042, 614528, 614727, 614728, 614731, 614733, 614734, 614735, 614739, 614741,
            614742, 614750, 614753, 614755, 614756, 614761, 614773, 614776, 618319, 623828, 624121, 654707, 677395,
            677397, 677398, 677400, 677403, 677404, 679448, 679455, 679462, 679464, 679466, 707365, 707369, 707371,
            707372, 707374, 711726, 711732, 711735, 711741, 711746, 722778, 722780, 722781, 722784, 825969, 831078,
            844544, 844552, 846528, 867888, 867891, 867892, 867895, 867896, 868351, 868352, 869171, 874497, 874500,
            874505, 874508, 874512, 874693, 874696, 874701, 874723, 881190, 39911921, 39911923, 42402741, 42402769,
            42402792, 42402830, 42402868, 42402886, 42402897, 42402908, 42402920, 45285669, 45285672, 45285674,
            45285677, 45285682, 45285685, 45285691, 45285698, 45285702, 52494482, 52494487, 52494490, 54526093,
            54526095, 54526097, 54526098, 54526100, 54526102, 57737429, 57737430, 57737478, 58785983, 64422010,
            64422016, 64487703, 64487705, 64487708, 4344250371, 4344250372, 4344250373, 4344250374, 4528799751,
            4998561802, 5384437777, 5602541574, 6827278356, 6827278357, 6827278358, 7984906291, 8957984817, 8957984818,
            8957984819, 9276751976, 9276751977, 9276751978, 34306]
    room_list = ['67313770']
    conn = psycopg2.connect(database="postgres", user="postgres", password="fws7609922", host="localhost", port="5432")
    print("Opened database successfully")

    cur = conn.cursor()
    for i in room_list:
        with os.popen("node c:\\nim-node-main\\src\\bin\\hist.js " + i) as p:
            r = p.read()
        with open("test.json", 'r', encoding='UTF-8') as file:
            msg_info = json.load(file)
        for i in msg_info:
            room = i["chatroomId"]
            time_stamp = i["time"]/1000
            msg_type = i["type"]
            body = json.loads(i["custom"])
            # print(body)
            if msg_type == "image" or msg_type == "video" or msg_type == "audio":
                photo_audio_video(time_stamp, i, msg_type, room)
            elif msg_type == "text" and i["text"] == "偶像翻牌":
                flipcard(time_stamp, body)
            else:
                normal_text_msg(time_stamp, body, room)

    conn.close()
