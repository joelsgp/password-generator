from random import randint, choice
##    from tkinter import *

word_length_max = 7
num_of_words = 3
#TURN THIS OFF IF NOT USING
#pass_length_min = 8
#pass_length_max = 12



words_file = open('words.txt', 'r')
words_str = words_file.read()
words_list = eval(words_str)

def gen():
    password = ""

    #while len(password) > pass_length_max or len(password) < pass_length_min:
    for i in range(num_of_words):
        while True:
            word = choice(words_list)
            if len(word) < word_length_max:
                break
        word = word[0].upper() + word[1:]
        password += word
        
    Number = str(randint(0, 99))
    if len(Number) == 1:
        Number = '0' + Number
    password += Number

    print(password + " -" + str(len(password)) + " characters")

while True:
    gen()
    input()

##        Text.delete(0.0, END)
##        Text.insert(END, password)

##    Window = Tk()
##
##    Text = Text(Window, width=23, height=1)
##    Button = Button(Window, text='Generate a password', command=gen)
##
##    Text.pack()
##    Button.pack()
