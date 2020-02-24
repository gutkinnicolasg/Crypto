#!/usr/bin/python3

# by Guillaume Gutkin-Nicolas
#
# Welcome to the Permutation Cipher
#

# Decrypt Function 
def decrypt(message, key):
    # creates variable p that stores the result of permutation function defined below
    p = permutation(key)
    # creates variable cipher that stores the result of buildCIpher function defined below
    cipher = buildCipher(message, key)
    # creates a variable dCipher that creates a list of list length of key
    dCipher = [''] * len(key)
    # a helper variable 
    count = 0
    # loop through every item in p
    for i in p:
        # stores the value of cipher's column to dCipher at column[value of i]
        dCipher[int(i)] += cipher[count]
        # increment count to walk through columnds of cipher
        count += 1
    # calls the printCipher function defined below
    printCipher(dCipher, cipher)
    
# Encrypt Function 
def encrypt(message, key):
    # creates variable p that stores the result of permutation function defined below
    p = permutation(key)
    # creates variable cipher that stores the result of buildCIpher function defined below
    cipher = buildCipher(message, key) 
    # creates a variable eCipher that creates a list of list length of key
    eCipher = [''] * len(key)
    # a helper variable 
    count = 0
    # loop through every item in p
    for i in p:
        # stores the value of cipher's at column[value of i] to eCipher
        eCipher[count] += cipher[int(i)]
        # increment count to walk through columnds of eCipher
        count += 1
    # calls the printCipher function defined below
    printCipher(eCipher, cipher)

# Print function
def printCipher(xCipher, cipher):
    # create a variable to store results
    result = ""
    # loops through every element of every row and adds them to result
    for i in range(len(cipher[0])):
        for j in range(len(xCipher)):
            # the try/except statement helps deal with uneven sized columns
            try:
                result += xCipher[j][i]
            except IndexError:
                result += " "
    # print result
    print(result)

# Build Cipher function 
def buildCipher(message, key):
    # creates a variable cipher that creates a list of list length of key
    cipher = [''] * len(key)
    # loops through each column
    for col in range(len(key)):
        pointer = col
        # while pointer is smaller then length of message
        while pointer < len(message):
            # cipher's current columns gets added the letter at pointers location in message
            cipher[col] += message[pointer]
            # increase pointer by length of key to set it at the next item for that cipher column
            pointer += len(key)
    # return cipher
    return cipher 

# Permutation Function that accepts a key
def permutation(key):
    # create a variable to store results
    result = ""
    # create a variable and instantiate it to a string
    sortedKey = ""
    # key gets alphabetized and then truned into a string which is stored in sortedKey
    sortedKey = sortedKey.join(sorted(key))
    # loops through sortedKey and finds the corresponding value in key and saves it's index
    for i in key:
        # if key has repetitive letters
        if key.count(i) > 1:
            # store the value at index(i) in result
            result += str(sortedKey.index(i))
            # turn that value to a '.' in sortedKey
            # this helps deal with repetitive letters while using the sorted() function
            sortedKey = sortedKey.replace(i,".",1)
        # else if this letter is not repeated
        elif key.count(i) == 1:
            # store the value at index(i) in result
            result += str(sortedKey.index(i))
    # return result
    return result

# Main method
if __name__=="__main__":
    # create a variable to store the users input
    choice = input("Would you like to Encrypt(E) or Decrypt(D)? E/D: ")
    # create a variable to store the users input
    key = input("What is your key word?: ")
    # turns the key to all upper case 
    key = key.upper()
    
    if choice == "E" or choice == "e":
        # create a variable to store the users input
        message = input("What message would you like encrypted?: ")
        # calls the encrypt function defined above
        encrypt(message, key)

    elif choice == "D" or choice == "d":
        # create a variable to store the users input
        message = input("What message would you like decrypted?: ")
        # calls the decrypt function defined above
        decrypt(message, key)
