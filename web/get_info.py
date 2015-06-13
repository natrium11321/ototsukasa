#! /usr/bin/python

import MySQLdb
import json
import cgi
import cgitb

form = cgi.FieldStorage()
cgitb.enable()

connector = MySQLdb.connect(host="localhost", db="ototsukasa", user="ototsukasa", passwd="ototsukasa", charset="utf8")

cursor = connector.cursor()

sex = form["sex"].value
with open("get_info.sql") as f:
    query = f.read().decode('utf-8')
query += "WHERE sex = '{0}' ORDER BY t.pos_id,t.id;".format(sex)

cursor.execute(query)
res = cursor.fetchall()
l = []
now = 0
for r in res:
    if r["pos_id"] != now:
        if now != 0:
            l.append(m)
        now = r["pos_id"]
        m = {'pos_id':r["pos_id"],'lat':r['lat'],'lng':r['lng'],'review_comment':r['comment'],'reviewedtime':r['reviewedtime'],'name':r['name'],toilets:[r['toilet_status']]}
    else:
        m["toilets"].append(r["toilet_status"])
j = json.dumps(l)

print "Content-type: text/javascript; charset=utf-8"
print
print j
