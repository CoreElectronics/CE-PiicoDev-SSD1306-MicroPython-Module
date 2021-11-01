# Circular path animation

from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms # cross-platform compatible sleep function
from math import sin, cos
display = create_PiicoDev_SSD1306()

r = 20 # radius of the path (px)

theta = 0
while True:
    display.fill(0)
    
    theta = theta + 0.02 # increment theta by a small amount
    
    # convert polar coordinates (r, theta) to cartesian coordinates (x, y)
    x = WIDTH/2  + r * cos(theta) 
    y = HEIGHT/2 + r * sin(theta)
    
    display.fill_rect(round(x), round(y), 10, 10, 1)
#     display.line(round(WIDTH/2)+5, round(HEIGHT/2)+5, round(x+5), round(y+5), 1) # uncomment for a bonus!
    display.show()
    
    
#     sleep_ms(10) # sleep optional. Updating the display takes long enough