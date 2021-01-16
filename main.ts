input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    basic.clearScreen()
    basic.showNumber(history[history.length - 1])
})
input.onGesture(Gesture.Shake, function on_gesture_shake() {
    
    roll = randint(0, 20)
    basic.showNumber(roll)
    history.push(roll)
    if (history.length == hist_len + 1) {
        // 
        history.removeAt(0)
    }
    
    pause(500)
    basic.clearScreen()
})
let roll = 0
let history : number[] = []
//  Explicitly state type of list.
let hist_len = 10
