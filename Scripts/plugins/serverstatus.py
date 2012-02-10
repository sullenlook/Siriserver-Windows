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

    @register("de-DE", "(.*Hoe*veel*verbonden)")
    @register("en-US", "(.*How*many*connections)|(.*server*conections)")
    def st_state(self, speech, language, serverconnections):
        if language == 'de-DE':
            self.say("Er zijn", serverconnections, "apparaten verbonden.")
        if language == 'en-US':
            self.say("There are", serverconnections, "devices connected")
        self.complete_request()

    @register("de-DE", "(.*server*status)")
    def st_serverstate(self, speech, language, serverstatus):
        self.say("Server status is  up= yes uptime= ", serverstatus)
        self.complete_request()
