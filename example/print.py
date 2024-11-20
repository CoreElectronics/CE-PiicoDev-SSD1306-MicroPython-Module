from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms

import utime

display = create_PiicoDev_SSD1306()

delay = 3000

# Basic print statements
example_number = 210.2

display.print('Hello world')
display.print()
display.print(example_number) # Emulating printing sensor values
display.print()
display.print("Number: {}".format(example_number))

# Clear screen and internal lists
sleep_ms(delay)
for _ in range(8):
    display.print()

# Demonstrate printing text at specific lines (with background boxes)

display.print('Line 2 text',line_num=2)
display.print('Line 4 text',line_num=4)
display.fill_rect(0,40,128,8,1)
display.print('Spooky line', line_num=6,c=0,blanking=False)
display.show()


# Clear screen and internal lists
sleep_ms(delay)
for _ in range(8):
    display.print()

display.print('Show overflowing lines')
    
sleep_ms(int(delay/2))






# Clear screen and internal lists
sleep_ms(delay)
for _ in range(8):
    display.print()

# Demonstrating the delimiting text functionality
show_delim = True
show_no_delim = False

if show_delim:
    display.print('this string should overflow a couple of times into the next line on the OLED',delim=True) # Default
    
if show_no_delim:
    display.print('this string should overflow a couple of times into the next line on the OLED',delim=False) # Raggedy

# Clear screen and internal lists
sleep_ms(delay)
for _ in range(8):
    display.print()

# Running a benchmark for printing lines
display.print('show how fast it takes to print lots of lines')

sleep_ms(int(delay/2))

start = utime.ticks_us()
for i in range(100):
    display.print('some text' + str(i))
    
   
display.print()
display.print()

outcome_str = str(round(utime.ticks_diff(utime.ticks_us(), start)/(100000000),2)) + ' seconds/print'
display.print(outcome_str)
print(outcome_str)



