import string
import random

characterList = ""
password = []

def setCharacterList():
    global characterList
    characterList += string.ascii_letters
    characterList += string.digits
    characterList += string.punctuation

def generatePassword():
    setCharacterList()
    password.clear()
    for i in range(12):
        # Picking a random character from our
        # character list
        randomchar = random.choice(characterList)

        # appending a random character to password
        password.append(randomchar)

    return ''.join(password)