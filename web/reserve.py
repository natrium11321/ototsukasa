#! /usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import os
import sys
import cgitb


cgitb.enable()

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

print 'Content-type: text/html; charset=UTF-8'
print "Status: 303 See other"
print "Location: /logout.html"
print  #end of header

#print "id=",form["id"].value
