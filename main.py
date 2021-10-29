# PiicoDev SSD1306 demo code
# Show off some features of the PiicoDev OLED driver

import math
from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms

display = create_PiicoDev_SSD1306()

# Text and numbers
for counter in range(0,101):
    display.fill(0)
    display.text("PiicoDev",30,20, 1)
    display.text(str(counter),50,35, 1)
    display.show()
sleep_ms(500)


# Bargraphs
thick = 15 # thickness of the bar
for val in range(WIDTH+1):
    display.fill(0)
    display.text("Bargraphs", 20, 10, 1)
    display.fill_rect(0, HEIGHT-thick, val, thick, 1) # Filled bar graph
    display.rect(0, int(HEIGHT-2*thick - 5), int(val/2), thick, 1) # no-fill
    display.show()
sleep_ms(500)


# Plots
graphSin = display.graph2D()
graphCos = display.graph2D()
for x in range(128):
    s = int(math.sin(x/10.0)*HEIGHT+HEIGHT+30)
    c = int(math.cos(x/10.0)*HEIGHT+HEIGHT+30)
    display.fill(0)
    display.text("Plots", 50, 10, 1)
    display.updateGraph2D(graphSin,s)
    display.updateGraph2D(graphCos,c)
    display.show()
sleep_ms(1000)


# Bouncy Square animation
square = 15   # square edge length (px)
x = (WIDTH-1)/2   # starting position
y = (HEIGHT-1)/2  # starting y position

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
    display.hline(0,0,WIDTH,1)
    display.vline(0,0,HEIGHT,1)
    display.vline(WIDTH-1,0,HEIGHT, 1)
    display.hline(0,HEIGHT-1,WIDTH, 1)
    
    # show the collision count
    display.text(str(collisionCount),10,round(HEIGHT/2), 1)
    display.show()
    sleep_ms(10)
