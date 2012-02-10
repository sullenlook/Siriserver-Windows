#!/usr/bin/python
# -*- coding: utf-8 -*-

from plugin import *

class serverstatfromfile():
    def siriserverstate(f, g, serverstatus, serverconnections):
        try:
            string = f.read()
            string = g.read() 
            f = open("connections.txt", "r")
            g = open("status.txt", "r")
        
            serverconnections = f.readline()
            serverstatus = g.readlines() 
        finally:
            f.close()
            g.close()

class serverstatus(Plugin):
    @register("de-DE", "(.*server*status)")
    @register("en-US", "(.*server*status)")
    def st_serverstate(self, speech, language, serverstatus):
        self.say("Server status is  up= yes uptime= ", serverstatus)
        self.complete_request()
