#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import urllib2, urllib
import json

from plugin import *

from siriObjects.baseObjects import AceObject, ClientBoundCommand
from siriObjects.systemObjects import GetRequestOrigin
from siriObjects.uiObjects import AddViews, AssistantUtteranceView

class SiriMapItemSnippet(AceObject):
    def __init__(self, userCurrentLocation=True, items=None):
        super(SiriMapItemSnippet, self).__init__("MapItemSnippet", "com.apple.ace.localsearch")
        self.userCurrentLocation = userCurrentLocation
        self.items = items
    
    def to_plist(self):
        self.add_property('userCurrentLocation')
        self.add_property('items')
        return super(SiriMapItemSnippet, self).to_plist()



class SiriLocation(AceObject):
    def __init__(self, label="Apple", street="1 Infinite Loop", city="Cupertino", stateCode="CA", countryCode="US", postalCode="95014", latitude=37.3317031860352, longitude=-122.030089795589):
        super(SiriLocation, self).__init__("Location", "com.apple.ace.system")
        self.label = label
        self.street = street
        self.city = city
        self.stateCode = stateCode
        self.countryCode = countryCode
        self.postalCode = postalCode
        self.latitude = latitude
        self.longitude = longitude
    
    def to_plist(self):
        self.add_property('label')
        self.add_property('street')
        self.add_property('city')
        self.add_property('stateCode')
        self.add_property('countryCode')
        self.add_property('postalCode')
        self.add_property('latitude')
        self.add_property('longitude')
        return super(SiriLocation, self).to_plist()

class SiriMapItem(AceObject):
    def __init__(self, label="Apple Headquarters", location=SiriLocation(), detailType="BUSINESS_ITEM"):
        super(SiriMapItem, self).__init__("MapItem", "com.apple.ace.localsearch")
        self.label = label
        self.detailType = detailType
        self.location = location
    
    def to_plist(self):
        self.add_property('label')
        self.add_property('detailType')
        self.add_property('location')
        return super(SiriMapItem, self).to_plist()

class maptest(Plugin):
    
    @register("de-DE", ".*test map.*")     
    @register("en-US", "(test map.*)")
    def mapDisplay(self, speech, language):
        view = AddViews(self.refId, dialogPhase="Completion")
        mapsnippet = SiriMapItemSnippet(items=[SiriMapItem()])
        view.views = [AssistantUtteranceView(text="Testing map", dialogIdentifier="Map#test"), mapsnippet]
        self.sendRequestWithoutAnswer(view)
        self.complete_request()
        
    @register("de-DE", "(waar ben ik.*)")     
    @register("en-US", "(Where am I.*)")
    def whereAmI(self, speech, language):
        if language == 'de-DE': 
            mapGetLocation = self.getResponseForRequest(GetRequestOrigin(self.refId))
            latitude = mapGetLocation["properties"]["latitude"]
            longitude = mapGetLocation["properties"]["longitude"]
            view = AddViews(self.refId, dialogPhase="Completion")
            mapsnippet = SiriMapItemSnippet(items=[SiriMapItem(SiriLocation("", "Je bent hier", "", "", "", "", latitude, longitude))])
            view.views = [AssistantUtteranceView(text="Testing map", dialogIdentifier="Map#test"), mapsnippet]
        else:
            mapGetLocation = self.getResponseForRequest(GetRequestOrigin(self.refId))
            latitude = mapGetLocation["properties"]["latitude"]
            longitude = mapGetLocation["properties"]["longitude"]
            view = AddViews(self.refId, dialogPhase="Completion")
            mapsnippet = SiriMapItemSnippet(items=[SiriMapItem(SiriLocation("", "You and I are here", "", "", "", "", latitude, longitude))])
            view.views = [AssistantUtteranceView(text="Testing map", dialogIdentifier="Map#test"), mapsnippet] 
            self.sendRequestWithoutAnswer(view)
            self.complete_request()
