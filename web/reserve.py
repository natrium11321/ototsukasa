#! /usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import os
import sys
import cgitb
import MySQLdb


cgitb.enable()

"""
#POST or not
if ( os.environ['REQUEST_METHOD'] != "POST" ):
    print 'Content-type: text/html; charset=UTF-8'
    print  #end of header
    print "METHOD error"
    sys.exit()

form = cgi.FieldStorage()

#check the paremeter
if ("id" not in form):
    print 'Content-type: text/html; charset=UTF-8'
    print  #end of header
    print "Paremeter error"
    sys.exit()

tid = form["id"].value
"""
tid = '0'

#check whether the toilet is empty
connector = MySQLdb.connect(host="localhost", db="ototsukasa", user="ototsukasa", passwd="ototsukasa", charset="utf8")

cursor = connector.cursor()

qcheck = u"SELECT use_status FROM toilet_status WHERE updatedt = (SELECT MAX(updatedt) FROM toilet_status AS t WHERE t.toilet_id = " + tid +');'
cursor.execute(qcheck)
res = cursor.fetchall()
status = res[0][0]

#not empty
if (status in [u"USED",u"RESERVED"]):
    print 'Content-type: text/html; charset=UTF-8'
    print "Status: 303 See other"
    print "Location: /fail.html"
    print  #end of header
elif (status == u"EMPTY"):
    print 'Content-type: text/html; charset=UTF-8'
    print "Status: 303 See other"
    print "Location: /success.html"
    print  #end of header
    qreserve = u"INSERT INTO reservation (toilet_id) VALUES (" + tid +');'
    cursor.execute(qreserve)
    connector.commit()
else: #status error
    print 'Content-type: text/html; charset=UTF-8'
    print  #end of header
    print "Status error"

cursor.close()
connector.close()
#print "id=",form["id"].value
