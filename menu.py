#!/usr/bin/python3

import os
import time
from simple_term_menu import TerminalMenu    # Need to install!!!!!!!!!


def boot():
	os.system('clear')
	for char in "WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK":
		print(char, sep=' ', end='', flush=True)
		time.sleep(0.03)
	print("")
	for char in "> LOGON ADMIN":
		print(char, sep=' ', end='', flush=True)
		time.sleep(0.03)
	print("")
	for char in "ENTER PASSWORD NOW":
		print(char, sep=' ', end='', flush=True)
		time.sleep(0.03)
	print("")
	for char in "> ":
		print(char, sep=' ', end='', flush=True)
		time.sleep(0.0)
	for char in "****":
		print(char, sep=' ', end='', flush=True)
		time.sleep(0.7)
	time.sleep(3)

def menu():
	boot()
	os.system('clear')
	#term_size = os.get_terminal_size()
	#print(term_size)
	#s = "Test"
	#print(s.center(0))

	menu_title = "WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK\nTHANK YOU FOR CHOOSING VAULT-TEC!\n"
	menu_items = ["[INIT PIP-BOY 2000 MK VI]", "[S.P.E.C.I.A.L]", "[VAULT-TEC MEDIA]", "[LOG OFF]"]
	cursor = "> "
	cursor_style = ("bold",)
	menu_style = ("standout",)
	menu_exit = False

	main_menu = TerminalMenu(menu_entries=menu_items, title=menu_title, menu_cursor=cursor, menu_cursor_style=cursor_style, menu_highlight_style=menu_style, cycle_cursor=True)

	spec_menu_title = "WELCOME TO ROBCO INDUSTRIES (TM) TERMLINK\nTHANK YOU FOR CHOOSING VAULT-TEC!\n"
	spec_menu_items = ["[STRENGTH]", "[PERCEPTION]", "[ENDURANCE]", "[CHARISMA]", "[INTELLIGENCE]", "[AGILITY]", "[LUCK]", "[GO BACK..]"]
	spec_menu_back = False

	spec_menu = TerminalMenu(spec_menu_items, spec_menu_title, cursor, cursor_style, menu_style)

	time.sleep(5)

	while not menu_exit:
		os.system('clear')
		main_sel = main_menu.show()

		if main_sel == 0:
			print("Option 2 Selected")
			time.sleep(5)
		elif main_sel == 1:
			while not spec_menu_back:
				os.system('clear')
				spec_sel = spec_menu.show()
				if spec_sel == 0:
					os.system('clear')
					strength = open('ascii-art.html', 'r')
					strength_contents = strength.read()
					print(strength_contents)
					time.sleep(5)
					strength.close()
				elif spec_sel == 1:
					print("Save Selected")
				elif spec_sel == 2:
					spec_menu_back = True
					print("Back Selected")
			edit_menu_back = False
			print("Option 2 Selected")
			time.sleep(5)
		elif main_sel == 2:
			print("Option 3 Selected")
			time.sleep(5)
		elif main_sel == 3:
			menu_exit = True
			print("Quit Selected")

# Comment
