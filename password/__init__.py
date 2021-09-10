#!/usr/bin/env python

import json
import random
import sys
from pathlib import Path
##from tkinter import *

import pyperclip


__version__ = '1.2.0'


# Get word list
word_list_path = Path(__file__).parent.joinpath('words.json')
with open(word_list_path) as words_file:
    words_list = json.load(words_file)

##print(words_list[0:50])


def add_random_words(password, num_of_words=3, word_length_max=7):
    for i in range(num_of_words):
        while True:
            word = random.choice(words_list)
            if len(word) <+ word_length_max:
                break

        word = word.title()
        password += word

    return password

def add_random_numerals(password, digits=2):
    numerals = ""

    for i in range(digits):
        numerals += str(random.randint(0,9))
    password += numerals

    return password


##def generate_password(pass_length_min=8, pass_length_max=12):
def generate_password():
    ##while len(password) > pass_length_max or len(password) < pass_length_min:
    password = ""
    password = add_random_words(password)
    password = add_random_numerals(password)

    print(f'{password:<30} - {len(password):<2} characters')
    pyperclip.copy(password)

    return password


def main():
    try:
        while True:
            generate_password()
            input()
    except KeyboardInterrupt:
        sys.exit()


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
