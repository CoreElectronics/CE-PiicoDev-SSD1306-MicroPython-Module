from PiicoDev_SSD1306 import *
display = create_PiicoDev_SSD1306()

myString = "this is me"
myNumber = 123.4567

display.print(0, "Hello, World!") # literal string
display.print(1, myString) # string variable
display.print(2, str(myNumber)) # print a variable
display.print(3, "{:.2f}".format(myNumber)) # use formatted-print
display.print(4, "4")
display.print(5, "5")
display.print(6, "6 Room for a 7 lines")
display.show()

sleep_ms(2000)
display.printConsole('1')
display.show()
sleep_ms(2000)
display.printConsole('2')
display.show()
sleep_ms(2000)
display.printConsole('3')
display.show()
sleep_ms(2000)
display.printConsole('4')
display.show()
