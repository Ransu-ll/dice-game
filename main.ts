input.onGesture(Gesture.Shake, function on_gesture_shake() {
    let roll = randint(0, 20)
    basic.showNumber(roll)
    history.push(roll)
    if (history.length == hist_len + 1) {
        // 
        history.removeAt(0)
    }
    
    pause(1000)
    basic.clearScreen()
})
input.onButtonPressed(Button.AB, function on_button_pressed_ab() {
    let display: number;
    
    if (check_history()) {
        return
    } else {
        basic.clearScreen()
        while (true) {
            display = history[history.length - x]
            basic.showString("#" + x)
            basic.showNumber(display)
            basic.clearScreen()
            pause(1000)
        }
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    
    if (check_history()) {
        return
    } else if (x == 1) {
        x = history.length - 1
    } else {
        x = x - 1
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    if (check_history()) {
        return
    } else if (x == history.length - 1) {
        x = 1
    } else {
        x = x + 1
    }
    
})
function check_history(): boolean {
    if (history.length == 0) {
        return true
    } else {
        return false
    }
    
}

let x = 1
let display = null
let roll = 0
let history : number[] = []
//  Explicitly state type of list.
let hist_len = 10
