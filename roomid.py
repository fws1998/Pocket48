import json
import psycopg2


def readfile(rpath):
    with open(rpath, 'r', encoding="UTF-8") as load_f:
        load_dict = json.load(load_f)
    return load_dict

conn = psycopg2.connect(database="postgres", user="postgres", password="fws7609922", host="localhost", port="5432")
print("Opened database successfully")

cur = conn.cursor()
data = readfile("roomId.json")
json_str = data["roomId"]



for i in json_str:
    id = i['id']
    name = ", \'" + i['ownerName'] + "\'"
    room = ", \'" + i['roomId']+ "\'"
    sql = "INSERT INTO star_info VALUES (" + str(id)+name+room+ ")"
    print(sql)
    print("done")
    cur.execute(sql)

conn.commit()
conn.close()

