import os
from time import sleep
string = "A \"Hello, World!\" program is generally a computer program that ignores any input and outputs or displays a message similar to \"Hello, World!\". A small piece of code in most general-purpose programming languages, this program is used to illustrate a language's basic syntax. \"Hello, World!\" programs are often the first a student learns to write in a given language, and they can also be used as a sanity check to ensure computer software intended to compile or run source code is correctly installed, and that its operator understands how to use it."
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz !.,\'"'
word = ""
for i in string:
    for j in alphabet:
        print(word + j)
        if(j==i):
            word += j
            break
        else:
            os.system("cls")
