from PiicoDev_SSD1306 import *
display = create_PiicoDev_SSD1306()

display.rect(10, 10, 20, 50, 1) # unfilled rectangle
display.fill_rect(50, 10, 50, 40, 1) # filled rectangle (white)
display.fill_rect(60, 20, 30, 20, 0) # filled rectangle (black)
display.show()