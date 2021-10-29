from PiicoDev_SSD1306 import *
from math import sin, cos, pi

display = create_PiicoDev_SSD1306()
graph1 = display.graph2D(minValue=-1, maxValue=1) # create two graph2D objects
graph2 = display.graph2D(minValue=-4, maxValue=4)

for x in range(WIDTH):
    y = sin(2*pi*x/WIDTH) # a sinewave of amplitude 1, and wavelength equal to the screen width
    z = (2*cos(6*pi*x/WIDTH)) # a cosinewave with amplitude 3, and wavelength one-third the screen width
    
    display.fill(0)
    display.updateGraph2D(graph1, y)
    display.updateGraph2D(graph2, z)
    display.hline(0,int(HEIGHT/2),128,1) # draw a zero-axis
    
    display.show()
