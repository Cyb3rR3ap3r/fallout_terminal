#!/usr/bin/python3

####  To Do
# Add a beggining "loading screen" than clear screen before password attempt  "Fallout 3"
# Add the logic to find the likeness of the password.
#
#
#### Future
# Add menu after successful login to do varies things
# Add a secret area that requires harder hack



# Main Menu =   tty-prompt      cursesmenu     simple-term-menu


import random
import sys
import os
import time
import data  # ./data.py
import password  # ./password.py

os.system('clear')    # Clear screen


guesses = 4
attempts = "Attempts Remaining: " + ("# " * guesses)

# 1.1   For each charactor in the string, it prints the string without appending to new line and waits,
# makeing it appear like someone typing.

def refresh():     # This function quickly prints the text used in main, subtracting the attempts
	os.system('clear')
	global guesses    # Need to call the variable as a global into the function
	print("Welcome to ROBCO Industries (TM) Termlink")
	#print("")
	print("Password Required...")
	print("")
	guesses -= 1
	print("Attempts Remaining: " + ("# " * guesses))
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
	guess = input("> ")

	if guess == data.pwd:
		print("Access Granted!")
	else:
		print("Access Denied")
		#guesses_left = 4
		#guesses_left =- 1
		refresh()

def failed():
	os.system('clear')
	print("FAILED")

def main():
	
	for char in "Welcome to ROBCO Industries (TM) Termlink":
		print(char, sep=' ', end='', flush=True)   # See comment above 1.1
		time.sleep(0.03)
	print("")


	for char in "Password Required...":
		print(char, sep=' ', end='', flush=True)
		time.sleep(0.03)
	print("\n")

	#attempts = "Attempts Remaining: " + ("# " * guesses_left) 

	for char in attempts:
		print(char, sep=' ', end='', flush=True)
		time.sleep(0.02)
	print("\n")


	for char in data.line0:
		print(char, sep=' ', end='', flush=True)
		time.sleep(0.01)
	print("")     # Used to append to new line.
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

	guesser()
	# print(data.pwd)

	#guess = input("> ")

	#if guess == data.pwd:
	#	print("Access Granted!")
	#else:
	#	print("Access Denied")
   


if __name__ == "__main__":
	main()
















###############################################################################
'''
curses_menu = curses.initscr() # Init the curses menu

menu = ['Home', 'Play', 'Exit']


def main(curses_menu):
	curses_menu.clear() # Clear screen
	curses.echo()

	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
	# This init a color pair of Green text with White background, you can call it with the
	# identifier of 1 as specified.  You can add multiple pairs by using different numbers

	curses_menu.attron(curses.color_pair(1))
	# This turns an attribute on (attron).  We are turning the color pair on.
	# To turn off, use attoff    " curses_menu.attoff(curses.color_pair(1)) "

	#curses_menu.addstr("Welcome to ROBCO Industries (TM) Termlink")
	#curses_menu.addstr("W"  + "e"  + "l")		

	curses_menu.refresh()
	curses_menu.getkey()


# if password is correct
curses.wrapper(main)
'''



# curses_menu.addstr   is like print()

















