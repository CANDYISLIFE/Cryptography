"""
cryptography.py
Author: Billy
Credit: <list sources used, if any>

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

userInput = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    
if userInput != "e" and userInput != "d" and userInput != "q":
    print("Did not understand command, try again. ")
elif userInput = "q":
    print("Goodbye!")

    

