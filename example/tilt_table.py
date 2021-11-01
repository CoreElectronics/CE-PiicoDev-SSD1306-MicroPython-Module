# Draw a square to indicate the tilt angle of an IMU - requires a PiicoDev Motion Sensor
from PiicoDev_SSD1306 import *
from PiicoDev_MPU6050 import PiicoDev_MPU6050
from PiicoDev_Unified import sleep_ms # cross-platform compatible sleep function

display = create_PiicoDev_SSD1306() # initialise PiicoDev modules
motion = PiicoDev_MPU6050()

while True:
    display.fill(0) # clear the screen every frame
    
    tilt = motion.read_angle() # read the angle (radians)
    aX = tilt['x']
    aY = tilt['y']
    
    sensitivity = 50 # sets how far the square will move for a given tilt
    x = round( aY * sensitivity +  WIDTH/2) 
    y = round( aX * sensitivity + HEIGHT/2) # convert angles to x,y coordinates for the square
    print("{:.2f}   {:.2f}".format(aX , aY))
    
    display.rect(x-5,y-5,10,10,1) # draw the square
    display.show()
