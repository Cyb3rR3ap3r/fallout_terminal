#!/usr/bin/python3

####  To Do
# Add a beggining "loading screen" than clear screen before password attempt  "Fallout 3"
# Update the menu after login
# Add a secret area that requires harder hack
#

# Main Menu =   tty-prompt      cursesmenu     simple-term-menu


import random
import sys
import os
import time
import data  # ./data.py
import menu # ./menu.py

os.system('clear')    # Clear screen


guesses = 4
attempts = "ATTEMPTS REMAINING: " + ("# " * guesses)
guess1 = ""
guess2 = ""
guess3 = ""
guess4 = ""
matched1 = ""
matched2 = ""
matched3 = ""
matched4 = ""



def refresh():     # This function quickly prints the text used in main, subtracting the attempts
	os.system('clear')
	global guesses    # Need to call the variable as a global into the function
	print("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK")
	#print("")
	print("PASSWORD REQUIRED...")
	print("")
	guesses -= 1
	print("ATTEMPTS REMAINING: " + ("# " * guesses))
	print("")
	print(data.line0)
	print(data.line1)
	print(data.line2)
	print(data.line3)
	print(data.line4)
	print(data.line5)
	print(data.line6)
	print(data.line7)
	print(data.line8)
	print(data.line9)
	print("")

	if guesses > 0:
		guesser()
	else:
		failed()


def guesser():      # This is the function that compares the password with the value enterd by user
	global guesses
	global guess1
	global guess2
	global guess3
	global guess4
	global matched1
	global matched2
	global matched3
	global matched4
	guess1_len = len(guess1)
	guess2_len = len(guess2)
	guess3_len = len(guess3)
	guess4_len = len(guess4)

	if guess1_len <= 0:
		pass
	else:
		print("> " + guess1)
		print("Entry Denied")
		print(matched1)

	if guess2_len <= 0:
		pass
	else:
		print("> " + guess2)
		print("Entry Denied")
		print(matched2)

	if guess3_len <= 0:
		pass
	else:
		print("> " + guess3)
		print("Entry Denied")
		print(matched3)

	if guess4_len <= 0:
		pass
	else:
		print("> " + guess4)
		print("Entry Denied")
		print(matched4)

	if guesses == 0:
		pass
	else:
		guess = input("> ")
		guess_len = len(guess)

	if guesses == 4:
		guess1 += guess.upper()       # Want to try elif now that I know the logic works

	elif guesses == 3:
		guess2 += guess.upper()

	elif guesses == 2:
		guess3 += guess.upper()

	elif guesses == 1:
		guess4 += guess.upper()


	if guess == data.pwd:
		print("Exact Match!")
		print("Please wait while system is accessed")
		time.sleep(4)
		menu.menu()          ###################################
	else:
		print("Entry Denied")

		matched = 0   # How many letters matched

		if guess_len < 4:
			pass
		elif guess_len > 4:
			pass
		else:
			for i in range(4):
				if guess[i] == data.pwd[0]:
					matched += 1
				elif guess[i] == data.pwd[1]:
					matched += 1
				elif guess[i] == data.pwd[2]:
					matched += 1
				elif guess[i] == data.pwd[3]:
					matched += 1


		correct = ("> " + str(matched) + "/4 correct.")
		print(correct)

		if guesses == 4:
			matched1 += correct
		elif guesses == 3:
			matched2 += correct
		elif guesses == 2:
			matched3 += correct
		elif guesses == 1:
			matched4 += correct
		refresh()


def failed():
	global guess1
	global guess2
	global guess3
	global guess4
	guess1_len = len(guess1)
	guess2_len = len(guess2)
	guess3_len = len(guess3)
	guess4_len = len(guess4)
	os.system('clear')
	global guesses
	print("WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK")
	print("PASSWORD REQUIRED...")
	print("")
	guesses -= 1
	print("ATTEMPTS REMAINING: " + ("# " * guesses))
	print("")
	print(data.line0)
	print(data.line1)
	print(data.line2)
	print(data.line3)
	print(data.line4)
	print(data.line5)
	print(data.line6)
	print(data.line7)
	print(data.line8)
	print(data.line9)
	print("")
	if guess1_len <= 0:
		pass
	else:
		print("> " + guess1)
		print("> Entry Denied")
		print(matched1)

	if guess2_len <= 0:
		pass
	else:
		print("> " + guess2)
		print("> Entry Denied")
		print(matched2)

	if guess3_len <= 0:
		pass
	else:
		print("> " + guess3)
		print("> Entry Denied")
		print(matched3)

	if guess4_len <= 0:
		pass
	else:
		print("> " + guess4)
		print("> Entry Denied")
		print(matched4)
	print("> Entry Denied")
	print("> ")
	print("> Terminal Locked")
	for char in "> Shuting down":
		print(char, sep=' ', end='', flush=True)
		time.sleep(0.00)
	for char in ".....":
		print(char, sep=' ', end='', flush=True)
		time.sleep(1.5)
	os.system('clear')

def main():

	for char in "WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK":
		print(char, sep=' ', end='', flush=True)
		time.sleep(0.03)
	print("")


	for char in "PASSWORD REQUIRED...":
		print(char, sep=' ', end='', flush=True)
		time.sleep(0.03)
	print("\n")

	for char in attempts:
		print(char, sep=' ', end='', flush=True)
		time.sleep(0.02)
	print("\n")


	for char in data.line0:
		print(char, sep=' ', end='', flush=True)
		time.sleep(0.01)
	print("")
	for char in data.line1:
		print(char, sep=' ', end='', flush=True)
		time.sleep(0.01)
	print("")
	for char in data.line2:
		print(char, sep=' ', end='', flush=True)
		time.sleep(0.01)
	print("")
	for char in data.line3:
		print(char, sep=' ', end='', flush=True)
		time.sleep(0.01)
	print("")
	for char in data.line4:
		print(char, sep=' ', end='', flush=True)
		time.sleep(0.01)
	print("")
	for char in data.line5:
		print(char, sep=' ', end='', flush=True)
		time.sleep(0.01)
	print("")
	for char in data.line6:
		print(char, sep=' ', end='', flush=True)
		time.sleep(0.01)
	print("")
	for char in data.line7:
		print(char, sep=' ', end='', flush=True)
		time.sleep(0.01)
	print("")
	for char in data.line8:
		print(char, sep=' ', end='', flush=True)
		time.sleep(0.01)
	print("")
	for char in data.line9:
		print(char, sep=' ', end='', flush=True)
		time.sleep(0.01)
	print("\n")
	print(data.pwd)     ##################### Remove / For Testing
	guesser()


if __name__ == "__main__":
	main()
