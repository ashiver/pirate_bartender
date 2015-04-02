# A pirate bartender!
import random

# Dictionaries
questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?"
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}


def question():
    """Asks user for preferences, maps answers to Boolean values in preferences dictionary; returns preferences"""
    preferences = questions
    for k in questions:
        answer = raw_input(questions[k])
        if answer.lower() == "yes" or answer.lower() == "y":
            preferences[k] = True
        elif answer.lower() == "no" or answer.lower() == "n":
            preferences[k] = False
    return preferences

  
def mix(preferences):
    """Takes drink preference dictionary; returns drink with randomized ingredients according to preferences"""
    drink = []
    for k in preferences:
        if preferences[k] == True:
          drink.append(random.choice(ingredients[k]))
    return drink
  
  
  
if __name__ == '__main__': 
    print mix(question())
    
        
                                                       
                                                       
                                                       