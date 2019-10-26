from typing import Text
from rasa_sdk import Action
import requests
import json

class ActionHelloWorld(Action):
    def name(self) -> Text:
        return "get_weather"

    def run(self, dispatcher, tracker, domain):
    	city = tracker.get_slot('city_weather')
    	print(city)
    	url = "http://localhost:8080/api/weather/{city}".format(city=city)
    	response = requests.get(url).text
    	dispatcher.utter_message(response)
    	return []
