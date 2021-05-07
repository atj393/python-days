import json
from difflib import get_close_matches

data = json.load(open("./data.json"))
is_active: str = 'y'
word: str = ''


def translate(word):
    if word in data:
        return data[word]
    else:
        return False


def find_matches(word):
    return get_close_matches(word, data.keys(), n=3, cutoff=0.8)


def start_dictionary():
    word = input("Enter a word: ")
    result = translate(word.lower())
    if result:
        if len(result) > 1:
            print(word)
            for idx, val in enumerate(result):
                print((idx+1), val, sep=". ")
        else:
            print(word, '\n', result[0])
    else:
        matches = find_matches(word)
        if(matches):
            print("Word not found. Other matching words ->", matches)
            start_dictionary()
        else:
            print("Word not found")


while is_active.lower() == 'y':
    start_dictionary()
    is_active = input("\nTry another word (y/n): ")
