#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()
from urllib.parse import parse_qs
import json
import os
print("Content-Type: text/html\n")
print()
print("<!doctype html>")
print("<head>")
print("<title>Hello</title>")
print("<style>pre {white-space: pre-wrap; word-wrap: break-word;}</style>")
print("</head>")
print("<h2>Hello World</h2>")

# print query params
print("<dl>")
print("<dt>QUERY_STRING:</dt>")
print("<dd>")
print(parse_qs(os.environ.get("QUERY_STRING")))
print("</dd>")
print("<dt>HTTP_USER_AGENT:</dt>")
HTTP_USER_AGENT = os.environ.get("HTTP_USER_AGENT", None)
print("<dd>" + HTTP_USER_AGENT + "</dd>")
print("</dl>")

# cgi.print_environ()
print("<pre>")
env_json = {}
for key, value in os.environ.items():
    env_json[key] = value
print(json.dumps(env_json))
print("</pre>")
