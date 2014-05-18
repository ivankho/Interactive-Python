# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
player_turn = True
multiplier = 1

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand = []	# create Hand object
        self.value = 0

    def __str__(self):
        # return a string representation of a hand
        string = "Hand contains " 
        for i in range(len(self.hand)):
            string += str(self.hand[i]) + " "
        return string

    def add_card(self, card):
        # add a card object to a hand
        self.hand.append(card)
        
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand
        keys = []
        values = []
        for cards in self.hand:
            keys.append(str(cards)[-1])
        if "A" not in keys:
            for key in keys:
                values.append(VALUES[key])
                self.value = sum(values)
        elif "A" in keys:
            for key in keys:
                values.append(VALUES[key])
                if sum(values) + 10 <= 21:
                    self.value = sum(values) + 10
                elif sum(values) + 10 > 21:
                    self.value = sum(values)
        return self.value
        

            
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        start_pos = [75, pos]
        for card in self.hand:
            card.draw(canvas, start_pos)
            start_pos[0] += 100

        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.deck = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.deck)

    def deal_card(self):
        # deal a card object from the deck
        return self.deck.pop()
    
    def __str__(self):
        # return a string representing the deck
        string = "Deck contains "
        for card in self.deck:
            string += str(card) + " "
        return string


#define event handlers for buttons
def deal():
    global outcome, in_play, player_hand, dealer_hand, deck, player_turn, message, score, multiplier
    player_hand = Hand()
    dealer_hand = Hand()
    deck = Deck() 
    deck.shuffle()
    player_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    if in_play == True:
        score -= multiplier
    in_play = True
    player_turn = True
    message = "Hit or Stand?"
    outcome = ""

def hit():
    global in_play, message, score, outcome, multiplier
    # if the hand is in play, hit the player        
    if in_play == True:
        player_hand.add_card(deck.deal_card())
    # if busted, assign a message to outcome, update in_play and score
    if player_hand.get_value() > 21:
        if in_play == True:
            score -= multiplier
            message = "New Deal?"
            outcome = "You Busted!"
        in_play = False


       
def stand():
    global player_turn, message, score, in_play, outcome, multiplier
    player_turn = False
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play == True:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
        if dealer_hand.get_value() > 21:
            message = "New deal?"
            outcome = "Dealer Bust!"
            score += multiplier
            in_play = False
        elif player_hand.get_value() > dealer_hand.get_value():
            score += multiplier
            in_play = False
            message = "New deal?"
            outcome = "You Win!"
        elif player_hand.get_value() < dealer_hand.get_value():
            score -= multiplier
            in_play = False
            message = "New deal?"
            outcome = "You Lose!" 


# draw handler    
def draw(canvas):
    global in_play
    player = 400
    dealer = 150
    player_hand.draw(canvas, player)
    dealer_hand.draw(canvas, dealer)
    if player_turn == True and in_play != False:
        canvas.draw_image(card_back, [CARD_BACK_CENTER[0], CARD_BACK_CENTER[1]], CARD_BACK_SIZE, [75 + CARD_BACK_CENTER[0], dealer + CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    canvas.draw_line([0,300], [600,300], 2, "Red")
    canvas.draw_text("Player", [100, 375], 40, "Black")
    canvas.draw_text("Dealer", [100, 125], 40, "Black")
    canvas.draw_text("Score:" + str(score), [430, 50], 40, "Turquoise")
    canvas.draw_text(message, [275, 375], 40, "Black")
    canvas.draw_text(outcome, [275, 125], 40, "Black")
    canvas.draw_text("Black", [50, 50], 50, "Black")
    canvas.draw_text("Jack", [165, 50], 50, "Red")
    canvas.draw_text("Player value: " + str(player_hand.get_value()), [75, 550], 25, "Red")    
    if in_play == False:
        canvas.draw_text("Dealer value: " + str(dealer_hand.get_value()), [75, 275], 25, "Red")    

# Functions to increase or decrease the score
def raise_the_stakes():
    global multiplier, in_play
    if in_play == False:
        multiplier += 1
        label.set_text("Current multiplier: " + str(multiplier))

def lower_the_stakes():
    global multiplier, in_play
    if in_play == False:
        if multiplier > 1:
            multiplier -= 1
        label.set_text("Current multiplier: " + str(multiplier))

    
# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.add_label("")
frame.add_label("")
frame.add_label("Change the Stakes:")
frame.add_button("Raise", raise_the_stakes, 200)
frame.add_button("Lower", lower_the_stakes, 200)
frame.add_label("")
frame.add_label("")
label = frame.add_label("Current multiplier: " + str(multiplier))
frame.add_label("")
frame.add_label("")
frame.add_label("Stakes can only be changed after you win or lose.")
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()