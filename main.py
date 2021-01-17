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
    # View up to the previous 10 roll history.
    global x
    if check_history():
        return
    else: 
        basic.clear_screen()
        
        while True:
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
        x = len(history) - 1
    else: 
        x =- 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    # Displays the next history number.
    global x
    if check_history():
        return
    elif x == len(history) - 1:
        x = 1
    else:
        x =+ 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def check_history():
    # "Cancels" an action if there is no history. 
    if len(history) == 0:
        return True
    else:
        return False

x = 1 # DO NOT TOUCH! History element default.
display = None # DO NOT TOUCH! What to display by default.

history: List[number] = [] # Explicitly state type of list.
hist_len = 10 # Ensure memory doesn't overflow with this value