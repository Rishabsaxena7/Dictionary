import json
from difflib import get_close_matches
#To load json file
data=json.load(open("data.json"))
# define a function to check word
def translate(word):
    #To convert word in lower case
    word=word.lower()
    if word in data:
        return data[word]
    # To convert word in Title
    elif word.title() in data:
        return data[word.title()]
    # To convert word in upper case
    elif word.upper() in data:
        return data[word.upper()]
    #To get close matches of word
    elif len(get_close_matches(word,data.keys()))>0:
        print("Did you mean %s insted",get_close_matches(word,data.keys())[0])
        deside=input("Enter y for yes or n for No")
        if deside=="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif deside=="n":
            print("word not found")
        else:
            print("please enter y or n")
    else:
        print("word not found")
# print output
word=input("Enter the word for searching")
output=translate(word)
# to display multiple meaning one by one
if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
