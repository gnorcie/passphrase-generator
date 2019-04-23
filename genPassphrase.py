#!/usr/bin/env python3.8

"""
genDiceware.py - securely generates a passphrase and sends it to the paste buffer
"""

import pyperclip
import sys
import random
from wordlist import wordlist

#read CLI argument for # of words or default to 7
def main():
    if len(sys.argv) > 1:
        if not sys.argv[1].isnumeric():
            print("You must enter a passphrase length ≥1\n\nTry again!")
        elif int(sys.argv[1]) < 1:
            print("You must enter a passphrase length ≥1\n\nTry again!")
        else:
            passphrase = generatePassphrase(int(sys.argv[1]))
            sendToClipboard(passphrase)
    else:
        sendToClipboard(generatePassphrase())

#send generated phrase to clipboard - uncomment print statement to debug
def sendToClipboard(phrase):
    pyperclip.copy(phrase)
    print('Sent passphrase to clipboard.');

#generate the passphrase itself
def generatePassphrase(length=7): #default is 7
    return " ".join(random.choices(wordlist, k=length))

main()
