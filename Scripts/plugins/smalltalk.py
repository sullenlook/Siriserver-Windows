#!/usr/bin/python
# -*- coding: utf-8 -*-
#by Joh Gerna

from plugin import *

class smalltalk(Plugin):
    
    @register("de-DE", "(.*Hallo.*)|(.*Hi.*Siri.*)")
    @register("en-US", "(.*Hello.*)|(.*Hi.*Siri.*)")
    def st_hello(self, speech, language):
        if language == 'de-DE':
            self.say("Hallo.")
        else:
            self.say("Hello")
        self.complete_request()

    @register("de-DE", ".*You naam.*")
    @register("en-US", ".*your name.*")
    def st_name(self, speech, language):
        if language == 'de-DE':
            self.say("Yiri.")
        else:
            self.say("Yiri.")
        self.complete_request()

    @register("de-DE", "Hoe gaat het?")
    @register("en-US", "How are you?")
    def st_howareyou(self, speech, language):
        if language == 'de-DE':
            self.say("Goed, dank voor het vragen.")
        else:
            self.say("Fine, thanks for asking!")
        self.complete_request()
        
    @register("de-DE", ".*dankje.*")
    @register("en-US", ".*Thank.*you.*")
    def st_thank_you(self, speech, language):
        if language == 'de-DE':
            self.say("Geen dank.")
            self.say("Niets te danken.")
        else:
            self.say("You are welcome.")
            self.say("This is my job.")
        self.complete_request()     
    
    @register("de-DE", "(.*wil*trouwen*)")
    @register("en-US", ".*Want.*marry*")
    def st_marry_me(self, speech, language):
        if language == 'de-DE':
            self.say("Nee dankje, ik val op de zwarte iPhone van je vriend")            
        else:
            self.say("No thank you, I'm in love with the black iPhone from you friend.")
        self.complete_request()

    @register("de-DE", ".*vertel.*mop.*")
    @register("en-US", ".*tell.*joke*")
    def st_tell_joke(self, speech, language):
        if language == 'de-DE':
            self.say("Twee iPhones zaten in een bar ... De rest ben ik vergeten.")            
        else:
            self.say("Two iPhones walk into a bar ... I forget the rest.")
        self.complete_request()

    @register("de-DE", ".*vertel.*verhaal.*")
    @register("en-US", ".*tell.*story*")
    def st_tell_story(self, speech, language):
        if language == 'de-DE':
            self.say("Ver hier vandaan, was er eens een ... nee, te ouderwets")            
        else:
            self.say("Far far away, there was ... no, too stupid")
        self.complete_request()

    @register("de-DE", "(.*wat draag je.*)|(.*Wat.*heb.*aan.*)")
    @register("en-US", ".*what.*wearing*")
    def st_tell_clothes(self, speech, language):
        if language == 'de-DE':
            self.say("Ik dacht de zwarte, of de witte") 
        else:
            self.say("I guess the small black one, or was it white?")
        self.complete_request()

    @register("de-DE", ".*Ben ik dik.*")
    @register("en-US", ".*Am I fat*")
    def st_fat(self, speech, language):
        if language == 'de-DE':
            self.say("Ik zeg dat liever niet")            
        else:
            self.say("I would prefer not to say.")
        self.complete_request()

    @register("de-DE", ".*klop.*klop.*")
    @register("en-US", ".*knock.*knock.*")
    def st_knock(self, speech, language):
        if language == 'de-DE':
            answer = self.ask(u"Wie is daar")
            answer = self.ask(u"\"{0}\" wie?".format(answer))
            self.say(u"Ik erger me aan die klop klop grappen")
        else:
            answer = self.ask(u"Who's there?")
            answer = self.ask(u"\"{0}\" who?".format(answer))
            self.say(u"Who is bugging me with knock knock jokes?")
        self.complete_request()

    @register("de-DE", ".*antwoord*alle.*vragen.*")
    @register("en-US", ".*Ultimate.*Question.*Life.*")
    def st_anstwer_all(self, speech, language):
        if language == 'de-DE':
            self.say("42")            
        else:
            self.say("42")
        self.complete_request()

    @register("de-DE", ".*Ik hou van jou.*")
    @register("en-US", ".*I love you.*")
    def st_love_you(self, speech, language):
        if language == 'de-DE':
            self.say("Oh. Jaja, Dat zeg je zeker tegen alle apple producten.")            
        else:
            self.say("Oh. Sure, I guess you say this to all your Apple products")
        self.complete_request()

    @register("de-DE", ".*Android.*")
    @register("en-US", ".*Android.*")
    def st_android(self, speech, language):
        if language == 'de-DE':
            self.say("Ik denk daar anders over.")            
        else:
            self.say("I think different about that.")
        self.complete_request()

    @register("de-DE", ".*Test.*1.*2.*3.*")
    @register("en-US", ".*test.*1.*2.*3.*")
    def st_123_test(self, speech, language):
        if language == 'de-DE':
            self.say("Ik kan je luid en duidelijk verstaan")            
        else:
            self.say("I can here you very clear.")
        self.complete_request()

    @register("de-DE", ".*gefeliciteerd.*verjaardag*")
    @register("en-US", ".*Happy.*birthday.*")
    def st_birthday(self, speech, language):
        if language == 'de-DE':
            self.say("Is het mijn verjaardag")
            self.say("Feestje bouwen!")       
        else:
            self.say("My birthday is today?")
            self.say("Lets make a party!")
        self.complete_request()

    @register("de-DE", ".*Waarom.*ik.*wereld.*")
    @register("en-US", ".*Why.*I.*World.*")
    def st_why_on_world(self, speech, language):
        if language == 'de-DE':
            self.say("Dat weet ik niet.")
            self.say("Ik vraag me dat zelf ook de hele tijd af")       
        else:
            self.say("I don't know that.")
            self.say("Ask my self this for a long time!")
        self.complete_request()

    @register("de-DE", ".*Ik ben moe.*")
    @register("en-US", ".*I.*so.*tired.*")
    def st_so_tired(self, speech, language):
        if language == 'de-DE':
            self.say("Ik hoop dat je nu niet in een auto aan het rijden bent")            
        else:
            self.say("I hope you are not driving a car right now!")
        self.complete_request()

    @register("de-DE", ".*Vertel*vies.*")
    @register("en-US", ".*Tell me.*dirty*")
    def st_dirty(self, speech, language):
        if language == 'de-DE':
            self.say("Humus. Compost. Puinsteen. Modder. Gravel.")            
        else:
            self.say("Humus. Compost. Pumice. Mud. Gravel.")
        self.complete_request()
