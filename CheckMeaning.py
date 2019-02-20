# data file 'data.json' is required for this exercise
# this program basically get an input from the user and look for the meaning in data.json file
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def MeaningOf(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y if yes, or N if no: "\
        % get_close_matches(word, data.keys())[0])
        if yn == "Y" or "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif yn == "N" or "n":
            return "The word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word doesn't exist. Please double check it."

word = ""
while word != 'Q' or 'q':
    word = input("Enter word or 'Q' to quit: ")
    if word == 'Q' or word == 'q':
        exit()
    meaning = MeaningOf(word)
    if type(meaning) == list:
        for lines in meaning:
            print(lines + '\n')
    else:
        print(meaning)
