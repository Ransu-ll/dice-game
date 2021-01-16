history = [-1.1]
x = 0

def on_gesture_shake():
    roll = randint(0, 20)
    basic.show_number(roll)
    if history[0] == -1.1:
        history[0] = roll
    else:
        history.append(roll)
    if len(history) == 11:
        history.remove_at(0)
    pause(500)
    basic.clear_screen()
    
input.on_gesture(Gesture.Shake, on_gesture_shake)


def on_button_pressed_ab():
    basic.clear_screen()
    basic.show_number(history[len(history) - 1])

input.on_button_pressed(Button.AB, on_button_pressed_ab)

