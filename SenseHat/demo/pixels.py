from sense_hat import SenseHat
from time import sleep

delay = 0.5

def creeper(sense):
    g = (0,80,0)
    b = (0,0,0)

    creeper = [
        g, g, g, g, g, g, g, g,
        g, g, g, g, g, g, g, g,
        g, b, b, g, g, b, b, g,
        g, b, b, g, g, b, b, g,
        g, g, g, b, b, g, g, g,
        g, g, b, b, b, b, g, g,
        g, g, b, b, b, b, g, g,
        g, g, b, g, g, b, g, g
    ]

    sense.set_pixels(creeper)

    for x in range(0,5):
        sleep(delay)
        sense.set_rotation((4-x)*90%360)

    for x in range(0,4):
        sleep(delay)
        sense.set_rotation((x+1)*90%360)
        #sense.flip_v()

def steve(sense):
    
    B = (102,51,0)
    b = (0,0,255)
    S = (205,133,63)
    W = (255,255,255)

    steve = [
        B, B, B, B, B, B, B, B,
        B, B, B, B, B, B, B, B,
        B, S, S, S, S, S, S, B,
        S, S, S, S, S, S, S, S,
        S, W, b, S, S, b, W, S,
        S, S, S, B, B, S, S, S,
        S, S, B, S, S, B, S, S,
        S, S, B, B, B, B, S, S
    ]

    sense.set_pixels(steve)

    for x in range(0,255):
        sense.set_pixel(2,4,(x,0,0))
        sense.set_pixel(5,4,(x,0,0))
        sleep(0.05)
    
sense = SenseHat()

while True:
    steve(sense)
    sleep(delay)
    creeper(sense)
    sleep(delay)
