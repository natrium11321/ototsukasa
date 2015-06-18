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
empty_num = 0
for r in res:
    if r[1] != now:
        if now != 0:
            l.append(m)
        now = r[1]
        m = {'pos_id':r[1],'lat':r[2],'lng':r[3],'review_comment':r[6],'reviewedtime':str(r[7]),'name':r[4],'toilets':[r[8]],'empty_num':0}
    else:
        m["toilets"].append(r[8])

    if (r[8] == 'Empty'):
        m['empty_num'] += 1
j = json.dumps(l)

print "Content-type: text/javascript; charset=utf-8"
print
print j
