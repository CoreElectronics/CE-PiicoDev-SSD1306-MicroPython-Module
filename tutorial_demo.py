# PiicoDev SSD1306 minimal example code
# This program writes to PiicoDev SSD1306 OLED display driver

import math
from random import uniform
from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms

display = create_PiicoDev_SSD1306()

WIDTH=127 # Dimensions of the OLED (px)
HEIGHT=63

print('Black')
display.fill(0)
display.show()
sleep_ms(1000)
# 
print('White')
display.fill(1)
display.show()
sleep_ms(1000)

print('Rectangle')
y = 30
width = 20
height = 35
for x in range(0, 129):
    y = y - 0.3
    display.fill(0)
    display.fill_rect(x, round(y), width, height, 1)
    display.show()
    # no sleep necessary, the frame update time is enough


# Bouncy Square
square = 15   # square edge length (px)
x = WIDTH/2   # starting position
y = HEIGHT/2  # starting y position

v = {'x': 2.3, # Starting velocity (pixels per animation frame)
     'y': 3.5}

collisionCount = 0
while True:
    display.fill(0) # empty the frame buffer
    
    # Next position = Current Position + Velocity
    x = x + v['x']
    y = y + v['y']
    
    # Check for boundary collision
    if x > WIDTH-square or x < 0:
        v['x']=-v['x'] # reverse the x-velocity
        collisionCount = collisionCount + 1
    if y >= HEIGHT-square or y < 0:
        v['y']=-v['y'] # reverse the x-velocity
        collisionCount = collisionCount + 1
    
    # draw the rectangle
    display.fill_rect(round(x), round(y), square, square, 1)
    
    # draw boundaries
    display.line(0,0,WIDTH,0, 1)
    display.line(0,0,0,HEIGHT, 1)
    display.line(WIDTH,0,WIDTH,HEIGHT, 1)
    display.line(0,HEIGHT,WIDTH,HEIGHT, 1)
    
    # show the collision count
    display.text(str(collisionCount),10,round(HEIGHT/2), 1)
    display.show()
    sleep_ms(10)
    
print('Test Pattern Filled Rectangle Inverted')
display.fill(1)
display.fill_rect(10, 10, 20, 30, 0)
display.show()
sleep_ms(1000)

#display.setContrast(0xFF)
display.text('PiicoDev',0,0)
display.text('Uptime',0,20)
display.text('Hello World!',0,55)
display.show()
sleep_ms(1000)
display.fill(0)
display.show()
# sleep_ms(100)
# if _SYSNAME == "microbit":
#     pass
# elif _SYSNAME == "Linux":
#     display.hline(0, 12, WIDTH, 255)
#     display.hline(0, 50, WIDTH, 255)
#     display.imagesend(display.image)
# else:
#     display.hline(0, 10, WIDTH, 0xffff)
#     display.hline(0, 50, WIDTH, 0xffff)




