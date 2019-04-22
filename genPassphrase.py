#genDiceware.py - securely generates a passphrase and sends it to the paste buffer

import pyperclip
import sys
import secrets #random module is not cryptographically secure

#read CLI argument for # of words or default to 7
def main():
	if len(sys.argv) > 1:
		if (sys.argv[1].isnumeric() == false):
			print("You must enter a passphrase length ≥1\n\nTry again!")
		elif int(sys.argv[1]) < 1:
			print("You must enter a passphrase length ≥1\n\nTry again!")
		else:
			passphrase = ' '.join(generatePassphrase(sys.argv[1]));
			sendToClipboard(passphrase)
	else:
		passphrase = ' '.join(generatePassphrase());
		sendToClipboard(passphrase)
	
 
#send generated phrase to clipboard - uncomment print statement to debug
def sendToClipboard(phrase):
	pyperclip.copy(phrase)
	#print(phrase)
	print('Sent passphrase to clipboard.');


#generate the passphrase itself
def generatePassphrase(length=7): #default is 7
	wordList = generateWordListDictionary();
	passphrase = [];

	for n in range(0,int(length)):
		passphrase.append(wordList[generateKey()]);

	return passphrase;	

# rolls a 6 sided die
def rollDie():
	#return random.SystemRandom().randint(1,6);
	die = [1,2,3,4,5,6]
	return secrets.choice(die)

#generates a 5 digit key corresponding to one diceware word
def generateKey():
	k = [] #list to hold die rolls
	for n in range(0,5):
		k.append(rollDie())
	 
	#make list string
	passwordKey = ''.join(str(i) for i in k)
	return(passwordKey)

#build a dictionary from file where each key is a 5 digit number corresponding to a specific diceware word (value)
def generateWordListDictionary():

	wordListDictionary = {};

	#open the file readonly, assumes wordlist is in same directory
	#if wordlist is *not* present can be obtained at https://www.eff.org/files/2016/07/18/eff_large_wordlist.txt
	file = open('./eff_large_wordlist.txt', 'r');

	#add keys and values to dictionary 1 by 1
	#TODO: find a cleaner looking way than using "split"?
	for line in file:
		wordListDictionary[str.split(line)[0]] = str.split(line)[1];

	file.close();

	return wordListDictionary


main();