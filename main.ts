let interval = randint(50, 2600)
interval = 0
let touch = 0
let release = 0
let tvuj_interval = 0
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    
    interval = randint(50, 2600)
    music.playTone(Note.C, interval)
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    music.playTone(Note.C, interval)
})
input.onLogoEvent(TouchButtonEvent.Touched, function on_logo_touched() {
    
    touch = control.millis()
})
input.onLogoEvent(TouchButtonEvent.Released, function on_logo_released() {
    
    release = control.millis()
    tvuj_interval = release - touch
    if (tvuj_interval == interval) {
        basic.showIcon(IconNames.Yes)
    } else {
        led.plotBarGraph(tvuj_interval, interval)
    }
    
})
