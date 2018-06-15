from sense_hat import SenseHat

sense = SenseHat()


bgcolor = (100,100,0)
fgcolor = (0,0,100)
speed=0.05 # default is 0.1

while True:
    sense.show_message("hi..bye", 
          text_colour=fgcolor, 
          back_colour=bgcolor, 
          scroll_speed=speed)

#while True:
#    r+=1
#    g+=1
#    b+=1
#    sense.clear((r%256,g%256,b%256))
