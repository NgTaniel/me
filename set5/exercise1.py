# -*- coding: UTF-8 -*-

import requests

"""REFACTORING

Refactoring is the process of making your code better. You are usually looking 
to make it more readable or easier to maintain. Usually you'll do this by 
pulling out bits of code that encapsualte one idea, especially if that idea is 
used in several places.

We've talked already about 
    ↱red→green→refactor↴
    ↜←←←←←←←←←←←←←←←←←←↩

Where red means make sure the test fails if you haven't done anything, green 
means make the test pass, however you can, now this is the reafactor part.

The function below works fine, but it's long and hard to read. Identify the 
parts that are repeated, and pull them out into their own functions. I've made 
that easier for you by making the function stubs for the bits you need to do.

Modify this function, don't write a whole new one.
"""


def wordy_pyramid():
    baseURL = (
        "https://us-central1-waldenpondpress.cloudfunctions.net/"
        "give_me_a_word?wordlength={length}"
    )
    def append_message(baseURL, a, b, c):
     pyramid_list = []
     for i in range(a, b, c):
        url = baseURL.format(length=i)
        r = requests.get(url)
        if r.status_code == 200:
            message = r.text
            pyramid_list.append(message)
        else:
            print("failed a request", r.status_code, i)
     letter_pyramid = []
     letter_pyramid.append(append_message(baseURL, 3, 21, 2))
     letter_pyramid.append(append_message(baseURL, 20, 3, -2))
     return letter_pyramid
    


def get_a_word_of_length_n(length):
    pass


def list_of_words_with_lengths(list_of_lengths):
    pass


    
if __name__ == "__main__":
    pyramid = wordy_pyramid()
    # for i in range(len(pyramid)):
    #     for j in int(len(pyramid[i])):
            # print(pyramid[i][j])
