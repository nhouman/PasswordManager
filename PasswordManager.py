###     TO DO     ###
#Create new credentials file for each new user
#Name file using hash of username
#Use Fernet to create UsernameHash.key file with hashed password as key
#Compare login username hash with entered hash. If matching, compare password
#   hash with hash in key file. If matching, logging in decrypts other file.
#Make sure file encryption works
#Create GUI 
import uuid, base64, hashlib, random, string, os
import tkinter as tk
from cryptography.fernet import Fernet

loginStatus = False

#Generates an encryption key
#key = Fernet.generate_key()
#with open('filekey.key', 'wb') as filekey:
#   filekey.write(key)
#
#fernet = Fernet(key)
#with open("info.txt", 'rb') as file:
#    original = file.read()
#
#Encrypt the file
#encryptedFile = fernet.encrypt()

#Creates the credentials the user will use to prove identity for passwords.
def createAccount():
    username = setUsername()
    hashedUN = hashlib.sha512(str(username).encode("utf-8")).hexdigest()
    path = hashedUN + ".key"
    if os.path.exists(path):
        print("That username already exists. Please enter a new one.")
        createAccount()
    else:
        file = open(hashedUN + ".key", "x")
        password = setPassword()
        file.write(password)
        file.close()
        print("Your account has been created.")
        
    

#Sets the account username
def setUsername():
    username = input("Username: ")
    return username

#Sets the account password. Allows the user to let the program create a random password.
def setPassword():
    password = input("Enter a password or type \"Random\" to have one generated for you: ")
    if(password.upper() == "RANDOM"):
        password = generatePassword()
    else:
        passConfirm = input("Confirm your password: ")
        if password != passConfirm:
            print("Passwords did not match.")
            setPassword()
        password = hashlib.sha512(str(password).encode("utf-8")).hexdigest()
    return password
    
#Login to password manager.
def login():
    global loginStatus
    try:  
        username = input("Username: ")
        hashedUN = hashlib.sha512(str(username).encode("utf-8")).hexdigest()
        file = open(hashedUN + ".key", "r")
        password = input("Enter your password: ")
        hashedPass = hashlib.sha512(str(password).encode("utf-8")).hexdigest()
        if hashedPass == file.readline():
            print("Login successful")
            loginStatus = True
        file.close()
        getCreds(hashedUN)
    except:
        print("Your username or password is incorrect")
        login()
    
#Add credentials for external accounts.    
def addCreds():
    file = open("info.txt", "a")
    site = input("Enter the name of the site/system: ")
    
    file.close()

#Gets the credentials from the file.
def getCreds(hashedUN):
    file = open(hashedUN + ".txt", "r+")
    file.close()
    
#Generates a reandom password, outputs the plain text, and returns the hashed password
def generatePassword():
    chars = string.ascii_letters + string.digits
    result = ''.join((random.choice(chars) for i in range(12)))
    print("Your password is", result)
    hashed = hashlib.sha512(str(result).encode("utf-8")).hexdigest()
    return hashed

#createAccount()
#login()
