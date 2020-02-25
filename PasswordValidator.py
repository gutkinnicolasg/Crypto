#!/usr/bin/python3

# Password Validator
# by Guillaume Gutkin-Nicolas

# Rule 1: Minimum length of 8
# Rule 2: Includes Uppercase
# Rule 3: Includes Lowercase
# Rule 4: Includes Number
# Rule 5: Includes Special Character [!@#$%^&*-_+=?><.,]
# Rule 6: Doesn't include these words [password, secureset]
   
# Global variable list that contains all the allowed special characters
whitelist = ['!','@','#','$','%','^','&','*','-','_','+','=','?','>','<','.',',']
# Global variable list that contains all the words that aren't allowed
blacklist = ['password', 'secureset']

# checkWhite function   
def checkWhite(x):
    for i in whitelist:
        if x == i:
            return True
    return False

# rule1 function
def rule1(password):
    if len(password) >= 8:
        return True
    return False

# rule2 function
def rule2(password):
    for i in password:
        if i.isupper():
            return True
    return False

# rule3 function
def rule3(password):
    for i in password:
        if i.islower():
            return True
    return False

# rule4 function
def rule4(password):
    for i in password:
        if i.isdigit():
            return True
    return False

# rule5 function
def rule5(password):
    for i in password:
        if checkWhite(i):
            return True
    return False

# rule6 function
def rule6(password):
    for i in blacklist:
        if i == password.lower():
            return True
    return False

# getWord function
def getWord(password):
    word = ""
    for i in password:
        if i.isalpha():
            word += i
    return word

# checkRules function
def checkRules(password):
    if rule1(password) != True:
        print("Password isn't long enough!\n")
        return False
    elif rule2(password) != True:
        print("Password doesn't have an uppercase letter!\n")
        return False
    elif rule3(password) != True:
        print("Password doesn't have a lowercase letter!\n")
        return False
    elif rule4(password) != True:
        print("Password doesn't have a number!\n")
        return False
    elif rule5(password) != True:
        print("Password doesn't have a special character!\n")
        return False
    elif rule6(getWord(password)) == True:
        print("Word is part of the forbidden list!\n")
        return False
    return True

# Main function          
if __name__=="__main__":
    print("Welcome to the Password Validator!\n")
    print("Rule 1: Minimum length of 8")
    print("Rule 2: Includes Uppercase")
    print("Rule 3: Includes Lowercase")
    print("Rule 4: Includes Number")
    print("Rule 5: Includes Special Character: !@#$%^&*-_+=?><.,")
    print("Rule 6: Doesn't include these words: password, secureset\n")
    flag = True 
    while flag == True:
        password = input("Please enter a password: ")
        if checkRules(password) == True:
            print("Password Accepted...")
            flag = False 

