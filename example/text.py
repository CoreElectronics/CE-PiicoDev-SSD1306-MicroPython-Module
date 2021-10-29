from PiicoDev_SSD1306 import *
display = create_PiicoDev_SSD1306()

myString = "this is me"
myNumber = 123.4567

display.text("Hello, World!", 0,0, 1) # literal string
display.text(myString, 0,15, 1) # string variable
display.text(str(myNumber), 0,30, 1) # print a variable
display.text("{:.2f}".format(myNumber), 0,45, 1) # use formatted-print
display.show()