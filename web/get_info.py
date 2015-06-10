#! /usr/bin/python

import MySQLdb
import json
import cgitb

cgitb.enable()

connector = MySQLdb.connect(host="localhost", db="ototsukasa", user="ototsukasa", passwd="ototsukasa", charset="utf8")

cursor = connector.cursor()

with open("get_info.sql") as f:
    query = f.read().decode('utf-8')

cursor.execute(query)
res = cursor.fetchall()
l = []
for r in res:
    m = {'pos_id':r[0],'lat':r[1],'lng':r[2],'num':r[3],'empty':r[4],'occupied':r[5],'reserved':r[6],'review_comment':r[7]}
    l.append(m)
j = json.dumps(l)

print "Content-type: text/javascript; charset=utf-8"
print
print j
