#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from datetime import date
import locale 
from plugin import *

class talkToMe(Plugin):   
        
    @register("de-DE", ".*Status.*")
    @register("en-GB", ".*Your.*Status.*")
    def ttm_uptime_status(self, speech, language):
        uptime = os.popen("uptime").read()
        if language == 'de-DE':
            self.say('Hier is de status:')
            self.say(uptime, ' ')
        else:
            self.say('Here is the status:')
            self.say(uptime, ' ')
        self.complete_request()     
    
    
    @register("de-DE", "(Welke dag.*)|(Welke datum.*)")
    @register("en-GB", "(What Day.*)|(What.*Date.*)")
    
    def ttm_say_date(self, speech, language):
        now = date.today()
        if language == 'de-DE':
            locale.setlocale(locale.LC_ALL, 'nl_NL')
            result=now.strftime("Het is %A, de %d.%m.%Y (Week: %W)")
            self.say(result)
        else:
            locale.setlocale(locale.LC_ALL, 'en_US')
            result=now.strftime("Today is %A the %d.%m.%Y (Week: %W)")
            self.say(result)
        self.complete_request()
