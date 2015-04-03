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

# Lists
adjectives = ["Mighty", "Stinky", "Strange", "Upside-down", "Inside-out", "Tasty", "Outrageous", "Wonky", "Angry"]

nouns = ["Bulldog", "Pelican", "Whale", "Canon Ball", "Peg Leg", "Prisoner", "Skalawag", "Ghost"]


def question():
    """Asks user for preferences, maps answers to Boolean values in preferences dictionary; returns preferences"""
    preferences = {}
    for k in questions:
        answer = raw_input(questions[k])
        if answer.lower() in ("yes","y"):
            preferences[k] = True
        elif answer.lower() in ("no","n"):
            preferences[k] = False
    return preferences

  
def mix(preferences):
    """Takes drink preference dictionary; returns drink with randomized ingredients according to preferences"""
    drink = []
    for k in preferences:
        if preferences[k] == True:
          drink.append(random.choice(ingredients[k]))
    return drink
  
  
def name():
    """Returns a random name for a drink"""
    return "" + random.choice(adjectives) + " " + random.choice(nouns)
    
  
def main():
    """Mixes a drink, names it, and serves it"""
    user = raw_input("What be ye name, sailor?")
    while True:
        answer = raw_input("Can I get ye a drink, {}?".format(user)).lower()
        if answer in ("yes", "y"):
            drink = mix(question())
            print "Arrrr, I'll mix ye one presently!"
            print "Behold! I call it a {}. It's made with:".format(name())
            for ingredient in drink:
                print "A {}".format(ingredient)
        else:
            print "Then scram ye lolly-gagger!"
            break
  
if __name__ == '__main__':
    main()
    