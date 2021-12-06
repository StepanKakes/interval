interval=randint(50, 2600)
interval = 0
touch = 0
release = 0
tvuj_interval = 0
def on_button_pressed_b():
    global interval
    interval=randint(50, 2600)
    music.play_tone(Note.C, interval)
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_button_pressed_a():
    music.play_tone(Note.C, interval)
input.on_button_pressed(Button.A, on_button_pressed_a)
def on_logo_touched():
    global touch
    touch=control.millis()
input.on_logo_event(TouchButtonEvent.TOUCHED, on_logo_touched)
def on_logo_released():
    global release, tvuj_interval
    release=control.millis()
    tvuj_interval=release-touch
    if tvuj_interval==interval:
        basic.show_icon(IconNames.YES)
    else:
        led.plot_bar_graph(tvuj_interval, interval)
input.on_logo_event(TouchButtonEvent.RELEASED, on_logo_released)