from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms

import utime

display = create_PiicoDev_SSD1306()

display.print('show overflowing lines')
    
sleep_ms(1000)

show_delim = True
show_no_delim = False

if show_delim:
    display.print('this string should overflow a couple of times into the next line on the OLED',delim=True) # Default
    
if show_no_delim:
    display.print('this string should overflow a couple of times into the next line on the OLED',delim=False) # Raggedy
    
sleep_ms(2000)
for _ in range(8):
    display.print()
    
display.print('show how fast it takes to print lots of lines')
    
sleep_ms(1000)
    
start = utime.ticks_us()
for i in range(100):
    display.print('some text' + str(i))
    
   
display.print()
display.print()

outcome_str = str(round(utime.ticks_diff(utime.ticks_us(), start)/(100000000),2)) + ' seconds/print'
display.print(outcome_str)
print(outcome_str)



#display.print('inserted', auto_scroll=False,line_num=8)
