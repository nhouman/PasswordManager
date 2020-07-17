import uuid, base64, hashlib, random, string
import tkinter as tk
file = open("info.txt", "r+")

def setUsername():
    file = open("info.txt", "w")
    username = input("Username: ")
    line = file.readline()
    while line:
        name = line.split(':')[0]
        if username == name:
            print("That username is taken. Try again")
            setUsername()
    file.close()
    
def setPassword():
    file = open("info.txt", "r+")
    password = input("Enter a password: ")
    passConfirm = input("Confirm your password: ")
    if password != passConfirm:
        print("Passwords did not match.")
        setPassword()
    file.close()
    
def createAccount():
    file = open("info.txt", "w")
    setUsername()
    setPassword()
    file.close()

def login():
    file = open("info.txt", "r")
    file.close()
    
def addCreds():
    file = open("info.txt", "a")
    file.close()
    
def generatePassword():
    file = open("info.txt", "a")
    chars = string.ascii_letters + string.digits
    result = ''.join((random.choice(chars) for i in range(12)))
    print("Password is", result)
    hashed = hashlib.sha256(str(result).encode("utf-8")).hexdigest()
    file.write(hashed + "\n")
    file.close()
    
generatePassword()         
