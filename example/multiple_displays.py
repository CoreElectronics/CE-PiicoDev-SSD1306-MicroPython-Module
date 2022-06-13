# This example drives two OLED modules independently.
# Each OLED module requires a unique address, set by the ADDR Jumper or ASW Switch
from PiicoDev_SSD1306 import *
oledA = create_PiicoDev_SSD1306(asw=0) 
oledB = create_PiicoDev_SSD1306(asw=1) # set up each device using the address-switch argument. 0:Open, 1:Closed

# advanced users may prefer using explicit I2C addresses, which can be set using the 'address' argument as follows:
# oledB = oledB = create_PiicoDev_SSD1306(address=0x3D)

# Load a different string onto each display
oledA.text("Display A", 0,0, 1) 
oledB.text("Display B", 0,40, 1)

oledA.show()
oledB.show()