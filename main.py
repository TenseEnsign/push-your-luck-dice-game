Recent_roll = 0
Last_roll = 0
Dice_roll = 0
Number_of_shakes = 0
basic.show_string("Shake")

def on_forever():
    global Number_of_shakes, Dice_roll, Last_roll, Recent_roll
    if input.is_gesture(Gesture.SHAKE):
        basic.show_leds("""
            # . . . .
                        . # . . .
                        . . # . .
                        . . . # .
                        . . . . #
        """)
        basic.show_leds("""
            . . . . #
                        . . . # .
                        . . # . .
                        . # . . .
                        # . . . .
        """)
        Number_of_shakes += 1
        Dice_roll = randint(1, 6)
        basic.show_number(Dice_roll)
        music.play_melody("C5 B A B - - - - ", 188)
        Last_roll = Dice_roll
        if Last_roll == Recent_roll:
            basic.show_icon(IconNames.SKULL)
            basic.pause(1000)
            basic.show_string("GAME OVER")
            basic.show_string("SCORE")
            basic.show_string("" + str((Number_of_shakes)))
            Recent_roll = 0
            Number_of_shakes = 0
            basic.show_string("Roll Again")
        else:
            Recent_roll = Last_roll
            Last_roll = 0
basic.forever(on_forever)
