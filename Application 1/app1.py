import json #import the json module
from difflib import get_close_matches

data = json.load(open("data.json")) #use json.load to read from the data.json file

def translate(word):
    word = word.lower() #if user enters words in mixed-case, it will convert all to lower
    if word in data: #first-case scenario, look for an exact match in the json file
        return data[word]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    #make sure the length of get_close_matches is > 0
    elif len(get_close_matches(word, data.keys())) > 0:
        #find a match that could be a match for the word entered
        yes_no = input("Did you mean %s instead? Enter Y if yes, or N if no: " % get_close_matches(word, data.keys())[0])
        if yes_no == "Y":
            #the user accepted the match; return that word as the match
            return data[get_close_matches(word, data.keys())[0]]
        elif yes_no == "N":
            return "That word doesn't exist. Please double-check it."
        else:
            return "Sorry. We didn't understand your entry."
    else:
        return "That word doesn't exist. Please double-check it."

word = input("Enter a word: ") #ask user for a word to define
output = translate(word) #call the function and store the result in a variable
if type(output) == list: #see if there is more than one definition for the word
    for item in output: #store the list items line by line
        print(item)
else:
    print(output)
