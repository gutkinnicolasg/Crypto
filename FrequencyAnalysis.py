#!/usr/bin/python3

# by Guillaume Gutkin-Nicolas
#
# Welcome to the Frequency Analysis
#
# This code will let you know how many times an uppercase, lowercase, number, or punctuation  appears in a text.
#
# Global strings
Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
punctuation = "!?.,"

# Uppercase function
def uppercase(text):
    # Loop through every item in global variable Alphabet
    for i in Alphabet:
        # print the count and percentage of item in Alphabet
        print(i + ":", text.count(i), "| Percentage:", text.count(i)/len(text) * 100)

# Lowercase function    
def lowercase(text):
    # Loop through every item in global variable alphabet
    for i in alphabet: 
        # print the count and percentage of item in alphabet
        print(i + ":", text.count(i), "| Percentage:", text.count(i)/len(text) * 100)

# Numbers function
def numbers(text):
    # Loop through every item in global variable numbers
    for i in Alphabet: 
        # print the count and percentage of item in numbers
        print(i + ":", text.count(i), "| Percentage:", text.count(i)/len(text) * 100)

# Punctuation function
def punctuation(text):
    # Loop through every item in global variable punctuation
    for i in Alphabet: 
        # print the count and percentage of item in punctuation
        print(i + ":", text.count(i), "| Percentage:", text.count(i)/len(text) * 100)

# Check function
def check(text):
    # Uppercase Flag
    UFLAG = False
    # Lowercase Flag
    LFLAG = False
    # Numbers Flag
    NFLAG = False
    # Punctuation Flag
    PFLAG = False
    # Loop through every item in the text
    for i in text:
        # if an item is uppercase set the flag to true
        if i.isupper():
            UFLAG = True
        # if an item is lowercase set the flag to true
        elif i.islower():
            LFLAG = True
        # if an item is a digit set the flag to true
        elif i.isdigit():
            NFLAG = True
        # if an item is one of the following set the flag to true
        elif i == '!' or i == '?' or i == '.' or i == ',':
            PFLAG = True
    # if the uppercase flag is true call the uppercase function
    if UFLAG == True:
        uppercase(text)
    # if the lowercase flag is true call the lowercase function
    if LFLAG == True:
        lowercase(text) 
    # if the numbers flag is true call the numbers function
    if NFLAG == True:
        numbers(text)
    # if the punctuation flag is true call the punctuation function
    if PFLAG == True:
        punctuation(text)

# Main function
if __name__=="__main__":
    # filename opens up a file that stores the text to analyze
    filename = open("./sample.txt", "r")
    # stores the whole file in the variable text
    text = filename.read()
    # calls the check function
    check(text)
    # prints the total number of characters in the text
    print("Total: " + str((len(text))))
    # closes file we opened
    filename.close()
