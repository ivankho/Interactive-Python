# import modules
import simplegui

# define global variables
time = 0
right = 0
total = 0
score = str(right) + "/" + str(total)
timer_stopped = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    string_t = str(t)
    millisecond = string_t[-1]
    total_seconds = string_t[:-1]
    if total_seconds == "":
    	total_seconds = "0"
    seconds_int = int(total_seconds)
    minutes = seconds_int // 60
    d = minutes * 60
    seconds = seconds_int - d
    if len(str(seconds)) == 1:
        seconds = "0" + str(seconds)
    return str(minutes) + ":" + str(seconds) + "." + str(millisecond)

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    global timer_stopped
    timer_stopped = False
    timer.start()
    
    
def Stop():
    global time, right, total, score, timer_stopped
    timer.stop()
    time_string = str(time)
    millisecond = time_string[-1]
    millisecond = int(millisecond)
    if millisecond == 0 and timer_stopped == False:
        right += 1
        total += 1
        score = str(right) + "/" + str(total)
    elif millisecond != 0 and timer_stopped == False:
        total += 1
        score = str(right) + "/" + str(total)
    timer_stopped = True
    
def Reset():
    global time, timer_stopped, right, total, score
    timer_stopped = True
    timer.stop()
    time = 0
    right = 0
    total = 0
    score = str(right) + "/" + str(total)
    
# define event handler for timer with 0.1 sec interval
def timer():
    global time
    time += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), [90,125], 50, "White")
    canvas.draw_text(score, [232, 40], 50, "Red")
    canvas.draw_polygon([[53, 137], [53, 80], [252, 80], [252, 137] ], 2, 'Green')
    
# create frame
frame = simplegui.create_frame("Stopwatch",300,200)

# register event handlers
timer = simplegui.create_timer(100, timer)
frame.set_draw_handler(draw)
frame.add_button("Start", Start, 50)
frame.add_button("Stop", Stop, 50)
frame.add_button("Reset", Reset, 50)

# start frame
frame.start()
