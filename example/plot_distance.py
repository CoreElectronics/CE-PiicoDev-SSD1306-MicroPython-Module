# Sample distance with a PiicoDev Distance Sensor and plot the data on a PiicoDev OLED

from PiicoDev_SSD1306 import *
from PiicoDev_VL53L1X import PiicoDev_VL53L1X
from PiicoDev_Unified import sleep_ms # cross-platform compatible sleep function

# Initialise distance sensor and display
display = create_PiicoDev_SSD1306()
distSensor = PiicoDev_VL53L1X()

distanceGraph = display.graph2D(height=HEIGHT-10, minValue=0, maxValue=500) # Initialise graph with scale 0 -> 500mm

while True:
    display.fill(0) # we need to clear the display every frame
    display.hline(0,HEIGHT-1,WIDTH,1); display.vline(0,0,HEIGHT,1) # draw some axes
    
    dist_mm = distSensor.read() # read the distance in millimetres
    display.text(str(dist_mm),95,3,1) # print the distance in the top right
    display.updateGraph2D(distanceGraph, dist_mm) # plot the distance
    display.show() # don't forget to show()!
    