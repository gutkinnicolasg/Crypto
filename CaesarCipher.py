#!/usr/bin/python3

# by Guillaume Gutkin-Nicolas
#
# Welcome to the Caesar Cipher
#
# Encrypt(phrase) = (phrase[letter] + shift) % 26
# Decrpyt(phrase) = (phrase[letter] - shift) % 26

# Decrypt Function
def decrypt(phrase, shift):
    # create a variable to store results
    result = ""
    # loops through every element in phrase
    for i in range(len(phrase)):
        # if this character is in the alphabet
        if phrase[i].isalpha():
            # add the value of that character - shift to results
            # this method changes the character to its ASCII value with ord()
            # it then removes shifts then returns to its character value with chr()
            result+=chr((ord(phrase[i]) - shift - 65) % 26 + 65)
        # else the character is special character, number, or space
        else:
            # add an empty space to results
            result+=' '
    # print result
    print(result)

# Encrypt Function
def encrypt(phrase, shift):
    # create a variable to store results
    result = ""
    # loops through every element in phrase
    for i in range(len(phrase)):
        # if this character is in the alphabet
        if phrase[i].isalpha():
            # add the value of that character + shift to results
            # this method changes the character to its ASCII value with ord()
            # it then adds shifts then returns to its character value with chr()    
            result+=chr((ord(phrase[i]) + shift - 65) % 26 + 65)
        # else the character is special character, number, or space
        else:
            # add an empty space to results
            result+=' '
    # print result
    print(result)

# Main Function
if __name__=="__main__":
    # create a variable to store the users input
    choice = input("Would you like to Encrypt(E) or Decrypt(D)? E/D: ")
    
    if choice == "E" or choice == "e":
        # create a variable to store the users input
        phrase = input("What would you like to encrypt? ")
        # create a variable to store the users input and turns it to an integer with int()
        shift = int(input("Number of shifts? "))
        # calls the encrypt function defined above
        encrypt(phrase.upper(), shift)

    elif choice == "D" or choice == "d":
        # create a variable to store the users input
        phrase = input("what would you like to decrypt? ")
        # create a variable to store the users input and turns it to an integer with int()
        shift = int(input("Number of shifts? "))
        # calls the encrypt function defined above
        decrypt(phrase.upper(), shift)

