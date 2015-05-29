import MySQLdb
import json


connector = MySQLdb.connect(host="localhost", db="ototsukasa", user="ototsukasa", passwd="ototsukasa", charset="utf8")

cursor = connector.cursor()

with open("get_info.sql") as f:
    query = f.read().decode('utf-8')

cursor.execute(query)
res = cursor.fetchall()
l = []
for r in res:
    m = {'toilet_id':r[0],'pos_lat':r[1],'pos_lng':r[2],'use_status':r[3]}
    l.append(m)
j = json.dumps(l)
print(j)
