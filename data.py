#!/usr/bin/python3

from random import choice as rc
# Doing it this way allows the variables to be dynamic after ever run

current_possible_pass = []


#####################################################################################################
# Variables for no word strings

r = "!@#$%^&*()_+=-[{]}\|';:.>,</?"

no_word0 = rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r)
no_word1 = rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r)
no_word2 = rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r)
no_word3 = rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r)
no_word4 = rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r)
no_word5 = rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r)
no_word6 = rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r)
no_word7 = rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r)
no_word8 = rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r)
no_word9 = rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r)
no_word10 = rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r)
no_word11 = rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r)
no_word12 = rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r)
no_word13 = rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r)


######################################################################################################
# Variables for worded strings

p = ["SCAN", "RAGS", "NOTE", "FOOD", "EARN", "FALL", "LIFE", "LOVE", "NEAR", "NESS", "RING", "WOLF", "FISH", "FIVE", "KING", "ELSE", "TREE", "OVER", "TIME", "ABLE", "HAVE", "SING", "STAR", "CITY", "SOUL", "RICH", "DUCK", "FOOT", "FILM", "LION", "ANNA", "MEME", "LIVE", "SAFE", "PAIN", "RAIN", "SION", "IRON", "ONCE", "BALL", "WITH", "FIRE", "WOOD", "CARE", "CAKE", "BACK"]


word0 = rc(p)
current_possible_pass.append(word0)     # Used to add word to new list
pop0 = p.index(word0)      		# Used to find the location of word in list
p.pop(pop0)                		# Used to remove the word from the list

word1 = rc(p)
current_possible_pass.append(word1)
pop1 = p.index(word1)
p.pop(pop1)

word2 = rc(p)
current_possible_pass.append(word2)
pop2 = p.index(word2)
p.pop(pop2)

word3 = rc(p)
current_possible_pass.append(word3)
pop3 = p.index(word3)
p.pop(pop3)

word4 = rc(p)
current_possible_pass.append(word4)
pop4 = p.index(word4)
p.pop(pop4)

word5 = rc(p)
current_possible_pass.append(word5)
pop5 = p.index(word5)
p.pop(pop5)


word_line0 = rc(r) + rc(r) + rc(r) + word0 + rc(r) + rc(r) + rc(r) + rc(r) + rc(r)
word_line1 = rc(r) + rc(r) + rc(r) + rc(r) + word1 + rc(r) + rc(r) + rc(r) + rc(r)
word_line2 = rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + word2 + rc(r) + rc(r)
word_line3 = rc(r) + word3 + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r)
word_line4 = rc(r) + rc(r) + rc(r) + word4 + rc(r) + rc(r) + rc(r) + rc(r) + rc(r)
word_line5 = rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + rc(r) + word5 + rc(r) + rc(r)

######################################################################################################


text0 = "0x9430 " + (no_word0)
text1 = "0x9782 " + (no_word1)
line0 = text0 + "   " + text1

text2 = "0x8905 " + (word_line0)
text3 = "0x9107 " + (no_word2)
line1 = text2 + "   " + text3

text4 = "0x8644 " + (no_word3)
text5 = "0x7675 " + (word_line1)
line2 = text4 + "   " + text5

text6 = "0x9976 " + (no_word4)
text7 = "0x9265 " + (no_word5)
line3 = text6 + "   " + text7

text8 = "0x9916 " + (no_word6)
text9 = "0x9265 " + (word_line2)
line4 = text8 + "   " + text9

text10 = "0x9449 " + (no_word7)
text11 = "0x8170 " + (no_word8)
line5 = text10 + "   " + text11

text12 = "0x8905 " + (word_line3)
text13 = "0x9107 " + (no_word9)
line6 = text12 + "   " + text13

text14 = "0x9433 " + (no_word10)
text15 = "0x9769 " + (no_word11)
line7 = text14 + "   " + text15

text16 = "0x8908 " + (word_line4)
text17 = "0x9107 " + (no_word12)
line8 = text16 + "   " + text17

text18 = "0x9326 " + (no_word13)
text19 = "0x9861 " + (word_line5)
line9 = text18 + "   " + text19


# This is the password
pwd = rc(current_possible_pass)
pwd_len = len(pwd)


##################################################################

# Menu

def strength():
    os.system('clear')
    
