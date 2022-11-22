let Recent_roll = 0
let Last_roll = 0
let Dice_roll = 0
let Number_of_shakes = 0
basic.showString("Shake")
basic.forever(function () {
    if (input.isGesture(Gesture.Shake)) {
        basic.showLeds(`
            # . . . .
            . # . . .
            . . # . .
            . . . # .
            . . . . #
            `)
        basic.showLeds(`
            . . . . #
            . . . # .
            . . # . .
            . # . . .
            # . . . .
            `)
        Number_of_shakes += 1
        Dice_roll = randint(1, 6)
        basic.showNumber(Dice_roll)
        music.playMelody("C5 B A B - - - - ", 188)
        Last_roll = Dice_roll
        if (Last_roll == Recent_roll) {
            basic.showIcon(IconNames.Skull)
            basic.pause(1000)
            basic.showString("GAME OVER")
            basic.showString("SCORE")
            basic.showString("" + (Number_of_shakes))
            Recent_roll = 0
            Number_of_shakes = 0
            basic.showString("Roll Again")
        } else {
            Recent_roll = Last_roll
            Last_roll = 0
        }
    }
})
