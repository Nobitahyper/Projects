import json
from difflib import get_close_matches

with open("data.json", "r") as file:
    data = json.load(file)

def get_definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print(f"Did you mean {get_close_matches(word, data.keys())[0]} instead?")
        decide = input("press y for yes or n for no")
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            return("Sorry, we couldn't find that word.")
        else:
            return("Invalid input. Please enter either y or n.")
    else:
        print("pugger your paw steps on wrong keys")



word = input("Enter the word you want to search: ")
output = get_definition(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

def main():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except Exception as e:
        print(f"Error loading data: {e}")
        return

    word = input("Enter the word you want to search: ")
    output = get_definition(word)
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)

if __name__ == "__main__":
    main()
