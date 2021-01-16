def on_button_pressed_ab():
    basic.clear_screen()
    basic.show_number(history[len(history) - 1])
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_gesture_shake():
    global roll
    roll = randint(0, 20)
    basic.show_number(roll)
    history.append(roll)
    if len(history) == hist_len + 1: #
        history.remove_at(0)
    pause(500)
    basic.clear_screen()
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

roll = 0
history: List[number] = [] # Explicitly state type of list.
hist_len = 10 # Ensure memory doesn't overflow with this value