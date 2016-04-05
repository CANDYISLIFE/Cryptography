"""
cryptography.py
Author: Billy
Credit: Mr Dennison, Hayden, Adam

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

userInput = input("Enter e to encrypt, d to decrypt, or q to quit: ")

stringInt = []
keyInt = []
encryptedNumbers = []
encryptedLetters = ""
    
if userInput != "e" and userInput != "d" and userInput != "q":
    print("Did not understand command, try again. ")
elif userInput == "q":
    print("Goodbye!")
elif userInput == "e":
    userString = input("Message: ")
    userKey = input("Key: ")
    for i in userString:
        stringInt = stringInt + associations.find(i)
    for e in userKey:
        keyInt = keyInt + associations.find(e)
        while len(keyInt) <= len(stringInt):
            keyInt = keyInt + keyInt
        
        zippedNumbers = zip(stringInt, keyInt)
    for p in zippedNumbers:
        encryptedNumbers = encryptedNumbers + (p[0] + p[1])
    for t in encryptedNumbers:
        encryptedLetters = encryptedLetters + associations[t]
    print(encryptedLetters) 
elif userInput == "d":
    userCyphertext = input("Message: ")
    cyphertextKey = input("Key:")

"""    
print(encryptedNumbers)
print(stringInt)
print(keyInt)
print(zippedNumbers)
for x in zippedNumbers:
    print(x)
"""    