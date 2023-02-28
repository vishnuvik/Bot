from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class MathAction(Action):

    def name(self) -> Text:
        return "action_math"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        operation = tracker.latest_message['intent']['name']
        num1 = float(tracker.latest_message['entities'][0]['value'])
        num2 = float(tracker.latest_message['entities'][1]['value'])

        if operation == "addition":
            result = num1 + num2
            dispatcher.utter_message(template="utter_addition", sum=result)
        elif operation == "subtraction":
            result = num1 - num2
            dispatcher.utter_message(template="utter_subtraction", difference=result)
        elif operation == "multiplication":
            result = num1 * num2
            dispatcher.utter_message(template="utter_multiplication", product=result)
        elif operation == "division":
            result = num1 / num2
            dispatcher.utter_message(template="utter_division", quotient=result)

        return []
