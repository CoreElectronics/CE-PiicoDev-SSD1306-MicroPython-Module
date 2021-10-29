from PiicoDev_SSD1306 import *
display = create_PiicoDev_SSD1306()

display.hline(10,10, 80, 1) # horizontal line 80px long from (10,10)
display.vline(10,10, 35, 1) # vertical line 35px long from (10,10)
display.line(10,45, 90,10, 1) # two-point line from (10,35) to (90,10)

display.show()