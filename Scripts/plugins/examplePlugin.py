#!/usr/bin/python
# -*- coding: utf-8 -*-


from plugin import *

class examplePlugin(Plugin):
    
    @register("de-DE", ".*bedoeling.*leven.*")
    @register("en-US", ".*Meaning.*Life.*")
    def meaningOfLife(self, speech, language):
        if language == 'de-DE':
            answer = self.ask(u"Wil je dat echt weten?")
        else:
            self.say("I shouldn't tell you!")
        self.complete_request()

    @register("de-DE", ".*Locatie.*test.*")
    @register("en-US", ".*location.*test.*")
    def locationTest(self, speech, language):
        location = self.getCurrentLocation(force_reload=True)
        self.say(u"lat: {0}, long: {1}".format(location.latitude, location.longitude))
        self.complete_request()
