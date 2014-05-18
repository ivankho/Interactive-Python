# the use of simplegui in this program pertains specifically to codeskulptor

# import necessary modules to run program
import simplegui
from random import randrange

# initialize global variables
number_range = 100

# helper function to start and restart the game
def new_game():
    global number_range, secret_number, input, lives
    if number_range == 100:
		input = ""
		lives = 7
		secret_number = randrange(0,100)
		print "New game. Range is from 0 to %d." % number_range
		print "Number of remaining guesses is %d.\n" % lives
    if number_range == 1000:
		input = ""
		lives = 10
		secret_number = randrange(0,1000)
		print "New game. Range is from 0 to %d." % number_range
		print "Number of remaining guesses is %d.\n" % lives		

		
# event handlers for control panel
def range100():
    global number_range
    number_range = 100
    new_game()

def range1000():
    global number_range
    number_range = 1000
    new_game()
    
def input_guess(guess):
    global secret_number, input, lives
    input = int(guess)
    if lives > 0:
		if input == "":
			pass
		elif input < secret_number:
			lives -= 1
			print "Guess was %s." % str(input)
			print "Number of remaining guesses is %d." % lives
			print "Higher!\n"
		elif input > secret_number:
			lives -= 1
			print "Guess was %s." % str(input)
			print "Number of remaining guesses is %d." % lives
			print "Lower!\n"
		elif input == secret_number:
			lives -= 1
			print "Guess was %s." % str(input)
			print "Number of remaining guesses is %d." % lives
			print "Correct!\n"
			new_game()
		if lives == 0:
			print "You've ran out of guesses!\n"
			new_game()
    
# create frame
frame = simplegui.create_frame("Guess the Number", 200, 200)


# register event handlers for control elements

# button that changes range to range [0,100) and restarts
frame.add_button("Range is [0-100)", range100)

# button that changes range to range [0,1000) and restarts
frame.add_button("Range is [0-1000)", range1000)
frame.add_input("Enter Guess", input_guess, 100)


# call new_game and start frame
new_game()
frame.start()
