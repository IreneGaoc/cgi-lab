#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
import cgi
import cgitb
cgitb.enable()

from templates import login_page,secret_page,after_login_incorrect
from secret import username,password
import os
form = cgi.FieldStorage()

f_username = form.getfirst("username")

f_password = form.getfirst("password")
request_type = os.environ.get("REQUEST_METHOD", "GET")



c_username = None
c_password = None
cookie_string = os.environ.get("HTTP_COOKIE")
cookie_kvs = cookie_string.split("; ")
if cookie_kvs:
    for cookie_kv in cookie_kvs:
        k,v = cookie_kv.split("=")
        if k == "username":
            c_username = v
        elif k == "password":
            c_password = v
print("Content-Ty[e: text/html]")

if c_username and c_password:
    print()
    print(secret_page(c_username,c_password))

if request_type == "POST":
    if f_username == username and f_password == password:
        #login ok, set cockie
        print("Set-Cookie: username={};".format(f_username))
        print("Set-Cookie: password={};".format(f_password))
        print()
        print(secret_page(f_username,f_password))
    else:
        print()
        print(after_login_incorrect())
else:
    print()
    print(login_page())
    print(cookie_string())
