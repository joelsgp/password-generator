from random import randint, choice
##from tkinter import *

# Constants
word_length_max = 7
num_of_words = 3
# TURN THIS OFF IF NOT USING
# note from new joel - why?
##pass_length_min = 8
##pass_length_max = 12


# Get word list from txt document formatted as python list
# TODO: remove eval call, very bad
words_file = open('words.txt', 'r')
words_str = words_file.read()
words_list = eval(words_str)

def add_random_words(password, num_of_words=3, word_length_max=7):
    for i in range(num_of_words):
        while True:
            word = choice(words_list)
            if len(word) <+ word_length_max:
                break
            
        word = word[0].upper() + word[1:].lower()
        password += word

    return password

def add_random_numerals(password, digits=2):
    numerals = ""

    for i in range(digits):
        numerals += str(randint(0,9))
    password += numerals

    return password

def generate_password():
    password = ""

    ##while len(password) > pass_length_max or len(password) < pass_length_min:
    password = add_random_words(password)

    password = add_random_numerals(password)

    # NOTE (vulnerability): this works, but not for arbitrary character counts
    pass_length = len(password)
    spacing = 30 - pass_length - len(str(pass_length))
    print(password + " "*spacing + "-" + str(pass_length) + " characters")

while True:
    generate_password()
    input()

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
