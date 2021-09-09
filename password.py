#!/usr/bin/env python

import json
import random
from pathlib import Path
##from tkinter import *

import pyperclip


__version__ = '1.0.0'


# Get word list
word_list_path = Path(__file__).parent.joinpath('words.json')
with open(word_list_path) as words_file:
    words_list = json.load(words_file)

##print(words_list[0:50])


# Function to add random words to string.
def add_random_words(password, num_of_words=3, word_length_max=7):
    for i in range(num_of_words):
        while True:
            word = random.choice(words_list)
            if len(word) <+ word_length_max:
                break
            
        word = word.title()
        password += word

    return password

# Function to add random numerals to string.
def add_random_numerals(password, digits=2):
    numerals = ""

    for i in range(digits):
        numerals += str(random.randint(0,9))
    password += numerals

    return password


# Actual password generation function, combines other two functions and prints
def generate_password(pass_length_min=8, pass_length_max=12):
    ##while len(password) > pass_length_max or len(password) < pass_length_min:
    password = ""

    password = add_random_words(password)

    password = add_random_numerals(password)

    # Use password length to normalise placement of password length indicator.
    # NOTE (vulnerability): this works, but not for arbitrary character counts
    pass_length = len(password)
    spacing = 30 - pass_length - len(str(pass_length))
    print(password + " "*spacing + "-" + str(pass_length) + " characters")
    pyperclip.copy(password)

    return password


def main():
    while True:
        generate_password()
        input()


if __name__ == '__main__':
    main()


#TODO: finish adding UI

##    Text.delete(0.0, END)
##    Text.insert(END, password)
##
##Window = Tk()
##
##Text = Text(Window, width=23, height=1)
##Button = Button(Window, text='Generate a password', command=gen)
##
##Text.pack()
##Button.pack()
