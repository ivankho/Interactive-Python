# Rock-paper-scissors-lizard-Spock template
from random import randrange

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the follwing pass statement and fill in your code below
    if name == "rock":
    	number = 0
    	return number
    elif name == "Spock":
    	number = 1
    	return number
    elif name == "paper":
    	number = 2
    	return number
    elif name == "lizard":
    	number = 3
    	return number
    elif name == "scissors":
    	number = 4
    	return number
    else:
    	return "Error! Inappropriate name!"


def number_to_name(number):
    if number == 0:
    	name = "rock"
    	return name
    elif number == 1:
    	name = "Spock"
    	return name    
    elif number == 2:
       	name = "paper"
    	return name
    elif number == 3:
    	name = "lizard"
    	return name    
    elif number == 4:
    	name = "scissors"
    	return name
    else:
    	return "Error! Number out of range!"
        

def rpsls(player_choice):     
    # print out the message for the player's choice
	print "Player chooses %s" % player_choice
    # convert the player's choice to player_number using the function name_to_number()
	player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
	comp_number = randrange(0,5)
	# convert comp_number to comp_choice using the function number_to_name()
	comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
	print "Computer chooses %s" % comp_choice
    # compute difference of comp_number and player_number modulo five
	diff = (comp_number - player_number) % 5
	if diff == 1 or diff == 2:
		print "Computer wins!"
	elif diff == 3 or diff ==4:
		print "Player wins!"
	elif diff == 0:
		print "Player and Computer tie!"
	# print a blank line to separate consecutive games
	print "\n"
    
# test your code - LEAVE THESE CALLS IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

