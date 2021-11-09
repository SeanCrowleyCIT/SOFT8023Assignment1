import grpc
import json
from random import randint

class wordDictionary():

    def __init__(self):
        self.pangrams = {}

        with open("words_dictionary.json") as json_file:
            self.pangrams = json.load(json_file)
            #print(self.pangrams)

    def get_selection(self):
        rand_num = randint(0, len(self.pangrams))
        random_pangram = list(self.pangrams.keys())[rand_num]
        letterSelection = set(random_pangram)
        print(letterSelection)
        return letterSelection

    def is_pangram(self, word_in):
        if len(set(word_in)) == 7 and 's' not in word_in:
            return True
        else:
            return False

wordDictionary()
