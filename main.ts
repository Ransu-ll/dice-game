input.onGesture(Gesture.Shake, function on_gesture_shake() {
    //  Roll the dice.
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
    //  View up to the previous [x] roll history.
    
    
    loop_hist = true
    if (check_history()) {
        return
    } else {
        basic.clearScreen()
        pause(200)
        while (loop_hist) {
            display = history[history.length - x]
            basic.showString("#" + x)
            basic.showNumber(display)
            basic.clearScreen()
            pause(1000)
        }
    }
    
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    //  Displays the previous history number.
    
    if (check_history()) {
        return
    } else if (x == 1) {
        x = history.length
    } else {
        x = x - 1
    }
    
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    //  Displays the next history number.
    
    if (check_history()) {
        return
    } else if (x == history.length) {
        x = 1
    } else {
        x = x + 1
    }
    
})
input.onLogoEvent(TouchButtonEvent.Pressed, function on_logo_event_pressed() {
    //  Escape the AB history loop.
    
    loop_hist = false
})
function check_history(): boolean {
    //  "Cancels" an action if there is no history. 
    if (history.length == 0) {
        return true
    } else {
        return false
    }
    
}

//  DO NOT TOUCH section
let x = 1
//  History element default.
let display = null
//  What to display by default.
let loop_hist = true
let history : number[] = []
//  Explicitly state type of list.
//  Config
let hist_len = 10
