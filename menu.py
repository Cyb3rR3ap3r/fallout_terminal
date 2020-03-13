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

	menu_title = "Main Menu\n"
	menu_items = ["Edit Menu", "Second Item", "Third Item", "Log Off"]
	cursor = "> "
	cursor_style = ("bold",)
	menu_style = ("standout",)
	menu_exit = False

	main_menu = TerminalMenu(menu_entries=menu_items, title=menu_title, menu_cursor=cursor, menu_cursor_style=cursor_style, menu_highlight_style=menu_style, cycle_cursor=True)
	
	edit_menu_title = "Edit Menu\n"
	edit_menu_items = ["Edit Config", "Save Settings", "Back to Main Menu"]
	edit_menu_back = False
	
	edit_menu = TerminalMenu(edit_menu_items, edit_menu_title, cursor, cursor_style, menu_style)
	
	time.sleep(5)

	while not menu_exit:
		os.system('clear')
		main_sel = main_menu.show()

		if main_sel == 0:
			while not edit_menu_back:
				os.system('clear')
				edit_sel = edit_menu.show()
				if edit_sel == 0:
					print("Edit Config Selected")
				elif edit_sel == 1:
					print("Save Selected")
				elif edit_sel == 2:
					edit_menu_back = True
					print("Back Selected")
			edit_menu_back = False
		elif main_sel == 1:
			print("Option 2 Selected")
			time.sleep(5)
		elif main_sel == 2:
			print("Option 3 Selected")
			time.sleep(5)
		elif main_sel == 3:
			menu_exit = True
			print("Quit Selected")
				
# Comment
