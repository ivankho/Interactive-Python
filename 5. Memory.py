# implementation of card game - Memory


# please note that this program is actually a little faulty and 
# does not work properly as a normal game of memory would dictate.

import simplegui
import random

# helper function to initialize globals
def new_game():
    global deck_of_cards, state, exposed, background, click_pos, index, value1, value2, index1, index2, count
    state = 0
    index = []
    value1 = ""
    value2 = ""
    index1 = ""
    index2 = ""
    count = 1
    label.set_text("Turns = 0")
    deck_of_cards = range(8)
    exposed = [False] * 16
    background = "Green"
    for i in range(8):
        deck_of_cards.append(i)
    random.shuffle(deck_of_cards)
        
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state, deck_of_cards, click_pos, background, index1, index2, value1, value2, count, label
    label.set_text("Turns = " + str(count))
    mouse_pos = list(pos)
    click_pos = []
    card_pos = [15,75]
    polygons = ([0, 0], [50, 0], [50, 100], [0, 100])
    posi = 0
    for i in deck_of_cards:
        posi += 50
        click_pos.append(posi) # creates a list of 50, 100, 150, ... ,800
    if state == 0:
        for i in range(len(click_pos)):
            if mouse_pos[0] < click_pos[i] and mouse_pos[0] > click_pos[i-1]:
                state = 1
                index1 = i
                exposed[i] = True
                value1 = deck_of_cards[i] 
        if mouse_pos[0] < click_pos[0]:
            state = 1
            exposed[0] = True
            index1 = 0 
            value1 = deck_of_cards[0]
    elif state == 1:
        for i in range(len(click_pos)):
            if mouse_pos[0] < click_pos[i] and mouse_pos[0] > click_pos[i-1]:
                state = 2
                exposed[i] = True
                index2 = i
                if index2 == index1:
                    state = 1
                value2 = deck_of_cards[i]
        if mouse_pos[0] < click_pos[0]:
            state = 2
            exposed[0] = True
            index2 = 0 
            if index2 == index1:
                state = 1
            value2 = deck_of_cards[0]
    else:
        state = 1
        count = count + 1
        if value1 != value2:
            exposed[index1] = False
            exposed[index2] = False
        for i in range(len(click_pos)):
            if mouse_pos[0] < click_pos[i] and mouse_pos[0] > click_pos[i-1]:
                state = 1
                index1 = i
                exposed[i] = True
                value1 = deck_of_cards[i] 
        if mouse_pos[0] < click_pos[0]:
            state = 1
            exposed[0] = True
            index1 = 0 
            value1 = deck_of_cards[0]

                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck_of_cards, card_pos, state, exposed, background, index1, index2, value1, value2
    card_pos = [15,75]
    polygons = ([0, 0], [50, 0], [50, 100], [0, 100])
    for i in range(len(deck_of_cards)):
        if exposed[i] == False:
            canvas.draw_polygon([polygons[0], polygons[1], polygons[2], polygons[3]], 1, "Red", "Green")
            polygons[0][0] += (50)
            polygons[1][0] += (50)
            polygons[2][0] += (50)
            polygons[3][0] += (50)
        elif exposed[i] == True:
            polygons[0][0] += (50)
            polygons[1][0] += (50)
            polygons[2][0] += (50)
            polygons[3][0] += (50)
    if state == 0:
        for i in range(len(deck_of_cards)):    
            if exposed[i] == True:
                canvas.draw_text(str(deck_of_cards[i]), (card_pos[0], card_pos[1]),50,"White")
                canvas.draw_polygon([polygons[0], polygons[1], polygons[2], polygons[3]], 1, "Red", "Black")
                card_pos[0] += (50)
            elif exposed[i] == False:
                card_pos[0] += 50
    elif state == 1:
        for i in range(len(deck_of_cards)):    
            if exposed[i] == True:
                canvas.draw_text(str(deck_of_cards[i]), (card_pos[0], card_pos[1]),50,"White")
                canvas.draw_polygon([polygons[0], polygons[1], polygons[2], polygons[3]], 1, "Red", "Black")
                card_pos[0] += (50)
            elif exposed[i] == False:
                card_pos[0] += 50
    elif state == 2:
        for i in range(len(deck_of_cards)):    
            if exposed[i] == True:
                canvas.draw_text(str(deck_of_cards[i]), (card_pos[0], card_pos[1]),50,"White")
                canvas.draw_polygon([polygons[0], polygons[1], polygons[2], polygons[3]], 1, "Red", "Black")
                card_pos[0] += (50)
            elif exposed[i] == False:
                card_pos[0] += 50        
    else:
        if value1 != value2:
            exposed[index1] = False
            exposed[index2] = False
            value1 = ""
            value2 = ""
        elif value1 == value2:
            value1 = ""
            value2 = ""
            index1 = ""
            index2 = ""
        

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
