# Implementation of classic arcade game Pong

# Import modules
import simplegui
from random import randrange
from math import sqrt

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = True
RIGHT = False
ball_pos = [300, 200]
ball_vel = [0,0]
paddle1_pos = [[PAD_WIDTH/2, HEIGHT/2-HALF_PAD_HEIGHT],
                 [PAD_WIDTH/2, HEIGHT/2+HALF_PAD_HEIGHT]]
paddle2_pos = [[(WIDTH - PAD_WIDTH/2), HEIGHT/2-HALF_PAD_HEIGHT],
            [(WIDTH - PAD_WIDTH/2), HEIGHT/2+HALF_PAD_HEIGHT]
            ]
paddle1_vel = [0]
paddle2_vel = [0]
score1 = 0
score2 = 0
acceleration = 5

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left

def spawn_ball(direction):
    global ball_pos, ball_vel, LEFT, RIGHT
    ball_vel[0] = randrange(120,240)/100.
    ball_vel[1] = randrange(60,180)/100.
    if (direction == LEFT) == True:
        ball_pos = [300, 200]
        ball_vel[0] *= -1		# so that ball travels left
        ball_vel[1] *= -1 		# so that ball travels up
    elif (direction == RIGHT) == True:
        ball_pos = [300, 200]
        ball_vel[1] *= -1		# so that ball travels up
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2
    score1 = 0
    score2 = 0
    paddle1_pos = [[PAD_WIDTH/2, HEIGHT/2-HALF_PAD_HEIGHT],
                 [PAD_WIDTH/2, HEIGHT/2+HALF_PAD_HEIGHT]]
    paddle2_pos = [[(WIDTH - PAD_WIDTH/2), HEIGHT/2-HALF_PAD_HEIGHT],
            [(WIDTH - PAD_WIDTH/2), HEIGHT/2+HALF_PAD_HEIGHT]
            ]
    # left or right spawn is random for each new game
    x = randrange(2)
    if x == 1:
        spawn_ball(LEFT)
    else:
        spawn_ball(RIGHT)

# Changing paddle speeds
def plus_accel():
    global acceleration
    if acceleration <= 10:
        acceleration += 1
    
def minus_accel():
    global acceleration
    if acceleration > 1:
        acceleration -= 1
        
def faster_ball():
    global ball_pos, ball_vel
    ball_vel[0] += ball_vel[0] * 1.05
    ball_vel[1] += ball_vel[1] * 1.05
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, pad1_pos
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White") #left
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White") #middle
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # draw ball
    canvas.draw_circle([ball_pos[0], ball_pos[1]], BALL_RADIUS, 1, "white", "white")

    # keep paddle on the screen    
    if paddle1_pos[0][1] < 0:
        paddle1_pos = [[PAD_WIDTH/2,0],[PAD_WIDTH/2,PAD_HEIGHT]]
    if paddle1_pos[1][1] > 400:
        paddle1_pos = [[PAD_WIDTH/2,HEIGHT-PAD_HEIGHT],[PAD_WIDTH/2,HEIGHT]]
    if paddle2_pos[0][1] < 0:
        paddle2_pos = [[(WIDTH - PAD_WIDTH/2),0],[(WIDTH - PAD_WIDTH/2),PAD_HEIGHT]]
    if paddle2_pos[1][1] > 400:
        paddle2_pos = [[(WIDTH - PAD_WIDTH/2),HEIGHT-PAD_HEIGHT],[(WIDTH - PAD_WIDTH/2),HEIGHT]]
    
    # update paddle's vertical position
    paddle1_pos[0][1] += paddle1_vel[0]
    paddle1_pos[1][1] += paddle1_vel[0]
    paddle2_pos[0][1] += paddle2_vel[0]
    paddle2_pos[1][1] += paddle2_vel[0]
    
    # draw paddles
    canvas.draw_line(paddle1_pos[0], paddle1_pos[1], PAD_WIDTH, "White")
    canvas.draw_line(paddle2_pos[0], paddle2_pos[1], PAD_WIDTH, "White")

    # draw scores
    canvas.draw_text(str(score1), [200,100], 40, "White")
    canvas.draw_text(str(score2), [400,100], 40, "White")
    
    # Collide and reflect off walls:
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
    if ball_pos[1] >= (HEIGHT-1)-BALL_RADIUS:
        ball_vel[1] = -ball_vel[1]
        
    # Reflect off paddle1 or score on gutter1
    middle = (paddle1_pos[0][1] + paddle1_pos[1][1])/2
    distance1 = sqrt((ball_pos[0] - PAD_WIDTH)**2 + (ball_pos[1] - middle)**2) - BALL_RADIUS
    if distance1 <= 12 and ball_pos[0] <= BALL_RADIUS:
        ball_vel[0] = ball_vel[0] * -1.1
    elif ball_pos[0] <= BALL_RADIUS:
        score2 += 1
        spawn_ball(RIGHT)
        
    # Reflect off paddle2 or score on gutter2
    middle2 = (paddle2_pos[0][1] + paddle2_pos[1][1]) / 2
    distance2 = sqrt((ball_pos[0] - (WIDTH - PAD_WIDTH))**2 + (ball_pos[1] - middle2)**2)-BALL_RADIUS
    if distance2 <= 12 and ball_pos[0] >= (WIDTH-PAD_WIDTH-1)-BALL_RADIUS:
        ball_vel[0] = ball_vel[0] * -1.1
    elif ball_pos[0] >= (WIDTH-PAD_WIDTH-1)-BALL_RADIUS:
        score1 += 1
        spawn_ball(LEFT)
        

    
def keydown(key):
    global paddle1_vel, paddle2_vel
    global acceleration
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel[0] -= acceleration
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[0] += acceleration
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel[0] -= acceleration
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[0] += acceleration

def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel[0] = 0
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel[0] = 0
    elif key == simplegui.KEY_MAP["w"]:
        paddle1_vel[0] = 0
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel[0] = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart Game", new_game, 100)
frame.add_label("")
frame.add_label("Not satisfied with the paddle speed? Change it!")
frame.add_label("")
frame.add_button("Increase Paddle Speed", plus_accel, 150)
frame.add_button("Decrease Paddle Speed", minus_accel, 150)
frame.add_label("")
frame.add_label("Note: Paddle speed is not reset if game is reset.")
frame.add_label("")
frame.add_label("Speed things up!")
frame.add_button("Increase Ball Speed", faster_ball, 150)



# start frame
new_game()
frame.start()
