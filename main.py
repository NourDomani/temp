def on_forever():
    basic.show_string("" + str(input.temperature()))
    print("" + str(input.temperature()))
    basic.pause(100)
basic.forever(on_forever)
