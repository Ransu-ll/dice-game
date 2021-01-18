def on_gesture_shake():
    # Roll the dice.
    roll = randint(0, 20)
    basic.show_number(roll)
    history.append(roll)
    if len(history) == hist_len + 1: #
        history.remove_at(0)
    pause(1000)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    # View up to the previous [x] roll history.
    global x
    global loop_hist
    loop_hist = True
    if check_history():
        return
    else: 
        basic.clear_screen()
        pause(200)
        while loop_hist:
            display = history[len(history) - x]
            basic.show_string("#" + x)
            basic.show_number(display)
            basic.clear_screen()
            pause(1000)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_a():
    # Displays the previous history number.
    global x
    if check_history():
        return
    elif x == 1:
        x = len(history)
    else: 
        x = x - 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    # Displays the next history number.
    global x
    if check_history():
        return
    elif x == len(history):
        x = 1
    else:
        x = x + 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_logo_event_pressed():
    # Escape the AB history loop.
    global loop_hist
    loop_hist = False
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_event_pressed)

def check_history():
    # "Cancels" an action if there is no history. 
    if len(history) == 0:
        return True
    else:
        return False

# DO NOT TOUCH section
x = 1 # History element default.
display = None # What to display by default.
loop_hist = True
history: List[number] = [] # Explicitly state type of list.

# Config
hist_len = 10 # Ensure memory doesn't overflow with this value