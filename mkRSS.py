#!/bin/python3

# TODO: scale for more rss shit

import os
import sys
import urllib.request
import urllib.parse
import threading
import json
import http.server
import socketserver

port = os.getenv("PORT")
time = os.getenv("TIME")

if port != None:
    port = int(port)
else:
    port = 6969

if time != None:
    time = int(time)
else:
    time = 1800

print("Port: " + str(port) + ", Time: " + str(time))

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        #if self.path == '/':
        #    self.path = '/web/anime.rss'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

# Create an object of the above class
handler_object = MyHttpRequestHandler
my_server = socketserver.TCPServer(("", port), handler_object)

thread = threading.Thread(target=my_server.serve_forever)
thread.daemon = True
thread.start()

def setInterval(func, sec):
    def func_wrapper():
        setInterval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def dlRSS():
    print("updating config")
    try:
        configFile = open('./exposed/config.json')
        config = json.load(configFile)
        configFile.close()
    except:
        print("no config found!")
        return;

    for target in config.targets:
        print("working on target output: " + target.output)
        print("assembling rss string")
        rss = ""

        if not os.path.exists("./exposed/" + target.input):
            print("target.input does not exist! check your config?")
            return;

        file = open("./exposed/" + target.input, 'r')
        for line in file.readlines():
            if line[0] != "#" and line.strip() != "":
                rss = rss + "\"" + line.strip() + "\"|"
        file.close()

        rss = rss[:-1]
        rss = urllib.parse.quote(rss)
        rss = "https://nyaa.si/?page=rss&q=" + rss + "+-Batch+1080p&c=1_2&f=2&u=subsplease"

        try:
            fid = urllib.request.urlopen(url=rss,timeout=3)
        except:
            print("connection error!")
            return;

        webpage = fid.read().decode('utf-8')

        print("writing rss file")
        try:
            file = open("./web/" + target.output, "w")
            file.write(webpage)
            file.close()
        except:
            print("error while writing rss file")
            return;

dlRSS()
setInterval(dlRSS,time)
