from sense_hat import SenseHat
from time import sleep
from random import randint

delay = 0.5

sense = SenseHat()

message = "hi!!!.....bye!!!"

def random_color():
    return (randint(0,255),
            randint(0,255),
            randint(0,255))

while True:
    for x in message:
        sense.show_letter(x,
                          text_colour=random_color(),
                          back_colour=random_color())
        sleep(delay)
