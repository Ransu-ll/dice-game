let history = [-1.1]
let x = 0
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    let roll = randint(0, 20)
    basic.showNumber(roll)
    if (history[0] == -1.1) {
        history[0] = roll
    } else {
        history.push(roll)
    }
    
    if (history.length == 11) {
        history.removeAt(0)
    }
    
    pause(500)
    basic.clearScreen()
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.clearScreen()
    basic.showNumber(history[history.length - 1])
})
