#! /usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import os
import random
import sys
import cgitb
import MySQLdb

cgitb.enable()

#POST or not
if ( os.environ['REQUEST_METHOD'] != "POST" ):
    print 'Content-type: text/html; charset=UTF-8'
    print  #end of header
    print "METHOD error"
    sys.exit()

form = cgi.FieldStorage()

#check the paremeter
if ("pos_id" not in form or "sex" not in form):
    print 'Content-type: text/html; charset=UTF-8'
    print  #end of header
    print "Paremeter error"
    print form
    sys.exit()

pid = str(form["pos_id"].value)
sex = form["sex"].value


#check whether the toilet is empty
connector = MySQLdb.connect(host="localhost", db="ototsukasa", user="ototsukasa", passwd="ototsukasa", charset="utf8")

cursor = connector.cursor()

with open("get_empty_toiletid.sql") as f:
    q = f.read().decode("utf-8") + pid + ';'
cursor.execute(q)
ids = cursor.fetchall()

#qcheck = "SELECT use_status FROM toilet_status WHERE updatedt = (SELECT MAX(updatedt) FROM toilet_status AS t WHERE t.toilet_id = " + tid +');'

#cursor.execute(qcheck)
#res = cursor.fetchall()
#status = res[0][0]

#make password
random.seed()
password = str(random.randint(1000,9999))

#not empty
if (len(ids) == 0):
    print 'Content-type: text/html; charset=UTF-8'
    print "Status: 303 See other"
    print "Location: /fail.html"
    print  #end of header
else:
    tid = str(ids[0][0])
    qreserve = "INSERT INTO reservations (toilet_id,password) VALUES (" + tid + ',' + password +');'
    cursor.execute(qreserve)
    connector.commit()
    print 'Content-type: text/html; charset=UTF-8'
    print "Status: 303 See other"
    if (sex == 'F'):
        print "Location: /success_f.html?id=" + tid + "&password=" + password
    else:
        print "Location: /success.html?id=" + tid + "&password=" + password
    print  #end of header


cursor.close()
connector.close()
#print "id=",form["id"].value
