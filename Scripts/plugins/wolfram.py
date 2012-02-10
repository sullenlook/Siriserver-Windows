#!/usr/bin/python
# -*- coding: utf-8 -*-

#Author: WebScript
#Todo: Nothing that I know
#For: SiriServer
#Commands: The same as in original Wolfram Alpha in Siri
#If you find bug: email me - admin@game-host.eu

import re, urlparse
import urllib2, urllib
import json
from urllib2 import urlopen
from xml.dom import minidom

from plugin import *

from siriObjects.baseObjects import AceObject, ClientBoundCommand
from siriObjects.uiObjects import AddViews, AssistantUtteranceView

APPID = "JHQR8Q-T3728KR9QK" #Add your APPID between the ""

class SiriAnswerSnippet(AceObject):
    def __init__(self, answers=None):
        super(SiriAnswerSnippet, self).__init__("Snippet", "com.apple.ace.answer")
        self.answers = answers if answers != None else []
        self.confirmationOptions = None
    
    def to_plist(self):
        self.add_property('answers')
        self.add_property('confirmationOptions')
        return super(SiriAnswerSnippet, self).to_plist()

class SiriAnswer(AceObject):
    def __init__(self, title=None, lines=None):
        super(SiriAnswer, self).__init__("Object", "com.apple.ace.answer")
        self.title = title
        self.lines = lines if lines != None else []
    
    def to_plist(self):
        self.add_property('title')
        self.add_property('lines')
        return super(SiriAnswer, self).to_plist()

class SiriAnswerLine(AceObject):
    def __init__(self, text="", image=""):
        super(SiriAnswerLine, self).__init__("ObjectLine", "com.apple.ace.answer")
        self.text = text
        self.image = image
    
    def to_plist(self):
        self.add_property('text')
        self.add_property('image')
        return super(SiriAnswerLine, self).to_plist()

class wolfram(Plugin):
    
    @register("de-DE", "(Wat is [a-zA-Z0-9]+)|(Waar is [a-zA-Z0-9]+)|(Hoe veel [a-zA-Z0-9]+)|(Wat was [a-zA-Z0-9]+)|(Wie is [a-zA-Z0-9]+)|(Hoe lang [a-zA-Z0-9]+)|(Wat is [a-zA-Z0-9]+)|(Hoe ver [a-zA-Z0-9]+)|(Wanneer is [a-zA-Z0-9]+)|(Hoe hoog [a-zA-Z0-9]+)|(Hoe diep [a-zA-Z0-9]+)")     
    @register("en-US", "(What is [a-zA-Z0-9]+)|(Who is [a-zA-Z0-9]+)|(How many [a-zA-Z0-9]+)|(What was [a-zA-Z0-9]+)|(Who's [a-zA-Z0-9]+)|(How long [a-zA-Z0-9]+)|(What's [a-zA-Z0-9]+)|(How far [a-zA-Z0-9]+)|(When is [a-zA-Z0-9]+)|(Show me [a-zA-Z0-9]+)|(How high [a-zA-Z0-9]+)|(How deep [a-zA-Z0-9]+)")
    def wolfram(self, speech, language):
        wolframQuestion = speech.replace('who is ','').replace('what is ','').replace('what was ','').replace('Who is ','').replace('What is ','').replace('What was ','').replace('Wie is ','').replace('Wat is ', '').replace('Wie is ','').replace('Wat is ', '').replace('Hoe veel ','How much ').replace('Hoe lang ','How long ').replace('Hoe ver ','How far ').replace('Wanneer is ','When is ').replace('Hoe hoog ','How high ').replace('Hoe diep ','How deep ').replace('is','is').replace('de','the').replace('het','the').replace('een','the').replace('Hoe veel ','how much ').replace('Hoe lang ','how long ').replace('Hoe ver ','how far ').replace('wanneer is ','when is ').replace('Hoe hoog ','how high ').replace('hoe diep ','how deep ').replace('is','is').replace('de','the').replace('het','the').replace('een','the').replace(' ', '%20').replace(u'ä', 'a').replace(u'ö', 'o').replace(u'ü', 'u').replace(u'ß', 's')
        wolfram_alpha = 'http://api.wolframalpha.com/v1/query.jsp?input=%s&appid=%s' % (wolframQuestion, APPID)
        print wolfram_alpha
        dom = minidom.parse(urlopen(wolfram_alpha))
        count_wolfram = 0
        wolfram0 = 12
        wolfram_pod0 = 12
        wolfram0_img = 12
        wolfram1 = 12
        wolfram_pod1 = 12
        wolfram1_img = 12
        wolfram2 = 12
        wolfram_pod2 = 12
        wolfram2_img = 12
        wolfram3 = 12
        wolfram_pod3 = 12
        wolfram3_img = 12
        wolfram4 = 12
        wolfram_pod4 = 12
        wolfram4_img = 12
        wolfram5 = 12
        wolfram_pod5 = 12
        wolfram5_img = 12
        wolfram6 = 12
        wolfram_pod6 = 12
        wolfram6_img = 12
        wolfram7 = 12
        wolfram_pod7 = 12
        wolfram7_img = 12
        wolfram8 = 12
        wolfram_pod8 = 12
        wolfram8_img = 12
        wolframAnswer = 12
        wolframAnswer2 = 12
        wolframAnswer3 = 12
        wolframAnswer4 = 12
        wolframAnswer8 = 12
        query_list = dom.getElementsByTagName('queryresult')[-1]
        query_type = query_list.getAttribute('error')
        for node in dom.getElementsByTagName('queryresult'):
            for pod in node.getElementsByTagName('pod'):
               xmlTag = dom.getElementsByTagName('plaintext')[count_wolfram].toxml()
               xmlTag2 = dom.getElementsByTagName('subpod')[count_wolfram]
               xmlData=xmlTag.replace('<plaintext>','').replace('</plaintext>','')
               if count_wolfram == 0:
                  if xmlData == "<plaintext/>":
                      image_list = dom.getElementsByTagName('img')[count_wolfram]
                      image_type = image_list.getAttribute('src')
                      wolfram0 = image_type
                      wolfram0_img = 1
                  else:
                      wolfram0 = xmlData
                  wolfram_pod0 = pod.getAttribute('title')
               elif count_wolfram == 1:
                  if xmlData == "<plaintext/>":
                      image_list = dom.getElementsByTagName('img')[count_wolfram]
                      image_type = image_list.getAttribute('src')
                      wolfram1 = image_type
                      wolfram1_img = 1
                  else:
                      wolfram1 = xmlData
                  wolfram_pod1 = pod.getAttribute('title')
               elif count_wolfram == 2:
                  if xmlData == "<plaintext/>":
                     image_list = dom.getElementsByTagName('img')[count_wolfram]
                     image_type = image_list.getAttribute('src')
                     wolfram2 = image_type
                     wolfram2_img = 1
                  else:
                     wolfram2 = xmlData
                  wolfram_pod2 = pod.getAttribute('title')
               elif count_wolfram == 3:
                  if xmlData == "<plaintext/>":
                     image_list = dom.getElementsByTagName('img')[count_wolfram]
                     image_type = image_list.getAttribute('src')
                     wolfram3 = image_type
                     wolfram3_img = 1
                  else:
                     wolfram3 = xmlData
                  wolfram_pod3 = pod.getAttribute('title')
               elif count_wolfram == 4:
                  if xmlData == "<plaintext/>":
                     image_list = dom.getElementsByTagName('img')[count_wolfram]
                     image_type = image_list.getAttribute('src')
                     wolfram4 = image_type
                     wolfram4_img = 1
                  else:
                     wolfram4 = xmlData
                  wolfram_pod4 = pod.getAttribute('title')
               elif count_wolfram == 5:
                  wolfram5 = xmlData
                  wolfram_pod5 = pod.getAttribute('title')
               elif count_wolfram == 6:
                  wolfram6 = xmlData
                  wolfram_pod6 = pod.getAttribute('title')
               elif count_wolfram == 7:
                  wolfram7 = xmlData
                  wolfram_pod7 = pod.getAttribute('title')
               elif count_wolfram == 8:
                  wolfram8 = xmlData
                  wolfram_pod8 = pod.getAttribute('title')
               count_wolfram += 1
        if language == 'de-DE':
            self.say("Dit is misschien het antwoord op jouw vraag:")
        else:
            self.say("This might answer your question:")
        view = AddViews(self.refId, dialogPhase="Completion")
        if wolfram_pod0 != 12:
            if wolfram0_img == 1:
                wolframAnswer = SiriAnswer(title=wolfram_pod0,lines=[SiriAnswerLine(image=wolfram0)])
            else:
                wolframAnswer = SiriAnswer(title=wolfram_pod0,lines=[SiriAnswerLine(text=wolfram0)])
        else:
            print wolfram_pod0
        if wolfram_pod1 != 12:
            if wolfram1_img == 1:
                wolframAnswer1 = SiriAnswer(title=wolfram_pod1,lines=[SiriAnswerLine(image=wolfram1)])
            else:
                wolframAnswer1 = SiriAnswer(title=wolfram_pod1,lines=[SiriAnswerLine(text=wolfram1)])
        else:
            print wolfram_pod1
        if wolfram_pod2 != 12:
            if wolfram2_img == 1:
                wolframAnswer2 = SiriAnswer(title=wolfram_pod2,lines=[SiriAnswerLine(image=wolfram2)])
            else:
                wolframAnswer2 = SiriAnswer(title=wolfram_pod2,lines=[SiriAnswerLine(text=wolfram2)])
        else:
            print wolfram_pod2
        if wolfram_pod3 != 12:
            if wolfram3_img == 1:
                wolframAnswer3 = SiriAnswer(title=wolfram_pod3,lines=[SiriAnswerLine(image=wolfram3)])
            else:
                wolframAnswer3 = SiriAnswer(title=wolfram_pod3,lines=[SiriAnswerLine(text=wolfram3)])
        else:
            print wolfram_pod3
        if wolfram_pod4 != 12:
            if wolfram4_img == 1:
                wolframAnswer4 = SiriAnswer(title=wolfram_pod4,lines=[SiriAnswerLine(image=wolfram4)])
            else:
                wolframAnswer4 = SiriAnswer(title=wolfram_pod4,lines=[SiriAnswerLine(text=wolfram4)])
        else:
            print wolfram_pod4
        if wolfram_pod8 != 12:
            if wolfram8_img == 1:
                wolframAnswer8 = SiriAnswer(title=wolfram_pod8,lines=[SiriAnswerLine(image=wolfram8)])
            else:
                wolframAnswer8 = SiriAnswer(title=wolfram_pod8,lines=[SiriAnswerLine(text=wolfram8)])
        if wolfram_pod0 == 12:
            if APPID == "":
                self.say("Sorry I can't process your request. Your APPID is not set! Please register free dev account at http://wolframalpha.com and edit line 21 with you APPID.")
            else:
                if language == 'de-DE':
                    self.say("Niks gevonden voor je aanvraag")
                else:
                    self.say("Nothing has found for your query!")
            self.complete_request()
            view1 = 0
        elif wolfram_pod1 == 12:
            view1 = SiriAnswerSnippet(answers=[wolframAnswer])
        elif wolfram_pod2 == 12:
            view1 = SiriAnswerSnippet(answers=[wolframAnswer, wolframAnswer1])
        elif wolfram_pod3 == 12:
            view1 = SiriAnswerSnippet(answers=[wolframAnswer, wolframAnswer1, wolframAnswer2])
        elif wolfram_pod4 == 12:
            view1 = SiriAnswerSnippet(answers=[wolframAnswer, wolframAnswer1, wolframAnswer2, wolframAnswer3])
        elif wolfram_pod8 == 12:
            view1 = SiriAnswerSnippet(answers=[wolframAnswer, wolframAnswer1, wolframAnswer2, wolframAnswer3, wolframAnswer4])
        else:
            view1 = SiriAnswerSnippet(answers=[wolframAnswer, wolframAnswer1, wolframAnswer2, wolframAnswer3, wolframAnswer4, wolframAnswer8])
        view.views = [view1]
        self.sendRequestWithoutAnswer(view)
        self.complete_request()
