import requests
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionRouteToPoliceService(Action):
    def name(self):
        return "action_route_to_police_service"

    def run(self, dispatcher, tracker, domain):
        user_message = tracker.latest_message.get('text')
        url = "http://localhost:5004/webhooks/rest/webhook"

        # Send the user message to the Police service chatbot API
        response = requests.post(url, json={"sender": "classifier_bot", "message": user_message})

        if response.status_code == 200:
            # Parse the response from the Grama Niladhari bot
            responses = response.json()
            for message in responses:
                dispatcher.utter_message(text=message.get('text', 'Sorry, I could not process that.'))
        else:
            dispatcher.utter_message(text="Sorry, I am unable to connect to the Grama Niladhari Services Chatbot at this time.")

        return []

class ActionRouteToGramaNiladhariService(Action):
    def name(self):
        return "action_route_to_grama_niladhari_service"

    def run(self, dispatcher, tracker, domain):
        user_message = tracker.latest_message.get('text')
        url = "http://localhost:5006/webhooks/rest/webhook"

        # Send the user message to the Grama Niladhari service chatbot API
        response = requests.post(url, json={"sender": "classifier_bot", "message": user_message})
        
        if response.status_code == 200:
            # Parse the response from the Grama Niladhari bot
            responses = response.json()
            for message in responses:
                dispatcher.utter_message(text=message.get('text', 'Sorry, I could not process that.'))
        else:
            dispatcher.utter_message(text="Sorry, I am unable to connect to the Grama Niladhari Services Chatbot at this time.")

        return []