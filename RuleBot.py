import re
import random

class RuleBot:
    negative_responses = ("no","nope","nah","now","not a chance","sorry")
    exit_commands = ("quit","pause","exit","goodbye","bye","later")
    random_questions = (
        "What is your name?",
        "Where do you live?",
        "Tell me about your problems",
        "Where would you like to have treatment?",
    )

    def __init__(self):
        self.alienbabble = {
            "name_intent":r'.*\s*name.*',
            "location_intent":r'.*\s*live.*',
            "problem_intent":r'.*\s*problem.*',
            "treatment_location_intent":r'.*\s*country.*'
        }
    def greet(self):
        self.name = input("Hello I am Settler. What is your name?\n")
        will_help = input(
            f"Hi {self.name}, Where do you live?\n"
        )
        if will_help in self.negative_responses:
            print("Ok, Have a nice day!")
            return
        self.chat()

    def make_exit(self,reply):
        for command in self.exit_commands:
            if reply == command:
                print("Ok, have a nice day!")
                return True
    
    def chat(self):
        reply = input(i for i in self.random_questions).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self,reply):
        for key,value in self.alienbabble.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern,reply)
            if found_match and intent == "name_intent":
                reply = self.name_intent()
            elif found_match and intent == "location_intent":
                reply = self.location_intent()
            elif found_match and intent == "problem_intent":
                reply = self.problem_intent()
            elif found_match and intent == "treatment_location_intent":
                reply = self.treatment_location_intent()
        if not found_match:
            return self.no_match_intent()

    def name_intent(self):
        responses = ("My name is Settler. Tell me your name?\n",
                     "I am Settler. Introduce yourself?\n")
        return random.choice(responses)
    
    def location_intent(self):
        responses = ("Where do you live now?\n",
                     "What is your location?\n")
        return random.choice(responses)

    def problem_intent(self):
        responses = ("Tell me about your problems.\n",
                     "What kind of physical problem are you facing now?\n")
        return random.choice(responses)
    
    def treatment_location_intent(self):
        responses = ("Where would you like to have treatment?\n",
                     "Tell me about the country where you want to have treatment.\n")
        return random.choice(responses)

    def no_match_intent(self):
        responses = ("Tell me more.\n",
                     "Please describe more.\n")
        return random.choice(responses)
    
AlienBot = RuleBot()
AlienBot.greet()

