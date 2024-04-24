import random
import string
import time

lives = 9


brawlers = random.choice([
    "shelly",
    "nita",
    "colt",
    "bull",
    "jessie",
    "brock",
    "dynamike",
    "bo",
    "tick",
    "8-bit",
    "emz",
    "el primo",
    "barley",
    "poco",
    "rosa",
    "rico",
    "darryl",
    "penny",
    "carl",
    "jacky",
    "piper",
    "pam",
    "frank",
    "bibi",
    "bea",
    "mortis",
    "tara",
    "gene",
    "max",
    "sprout",
    "byron",
    "squeak",
    "nani",
    "surge",
    "colette",
    "lou",
    "amber",
    "meg",
    "griff",
    "buzz",
    "leon",
    "crow",
    "cordelius"
]
)
clue = []
unknown_letters = len(brawlers)

heart = u'\u2764' 
answered_correctly = False
def replace_clue_list(brawlers):
    for counter in range(0, len(brawlers)):
        clue.append('?')


def update_clue(answer, brawlers, clue, unknown_letters):
    unknown_letters == len(brawlers)
    index = 0
    while index < len(brawlers):
        if answer == brawlers[index]:
            clue[index] = answer
            unknown_letters = unknown_letters - 1
        index = index + 1
    
    return unknown_letters
         

replace_clue_list(brawlers)

while lives > 0:
    print(clue)
    print('lives left: ' + heart * lives)
    answer = input("guess letter or whole Brawler ")
    
    if answer == brawlers:
        answered_correctly = True
        break
    
    if answer in brawlers:
        unknown_letters = update_clue(answer, brawlers, clue, unknown_letters)
        
    

    if unknown_letters == 0:
        answered_correctly = True
        break
    else:
        print('incorrect. you lose a life !')
        lives = lives - 1

if answered_correctly:
    print('You won! The secret Brawler was ' + brawlers)
else:
    print('You lost! The secret Brawler was ' + brawlers)    

time.sleep(5)
