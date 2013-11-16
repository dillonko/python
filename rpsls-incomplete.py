def number_to_name(number):
    if number == 0:
        return "rock" 
    elif number == 2:
        return "paper"
    elif number == 4:
        return "scissors" 
    elif number == 3:
        return "lizard"
    else:
        return "Spock"

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "paper":
        return 2 
    elif name == "scissors":
        return 4 
    elif name == "lizard":
        return 3
    elif name == "Spock":
        return 1 
    else:
        return 5

import random

def rpsls(name):