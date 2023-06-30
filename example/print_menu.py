from PiicoDev_SSD1306 import *
from PiicoDev_Unified import sleep_ms

import utime

display = create_PiicoDev_SSD1306()

textYCoords = display._init_print_text_func(font_size=[8,8],spacing=[0,0,0])

def menuSelect(lineNum,display,textYCoords,font_height=8):
    dispParams = display.displaySize
    display.fill_rect(0,textYCoords[lineNum-1],dispParams[0],font_height,1)

def showMenu(mn_opt,hv_ln):
    for i, item in enumerate(mn_opt):
        if i == hv_ln-1:
            display.print(item,line_num=i+1,c=0,blanking=False)
        else:
            display.print(item,line_num=i+1,c=1,blanking=False)

hover_line = 1

menu_options = ['option1','option2','option3','option4','option5']


for i in range(1,len(menu_options)):
    display.fill(0)
    menuSelect(hover_line,display,textYCoords)
    showMenu(menu_options,hover_line)
    hover_line = hover_line + 1
    display.show()
    sleep_ms(700)

for i in range(len(menu_options)+1,1,-1):
    display.fill(0)
    menuSelect(hover_line,display,textYCoords)
    showMenu(menu_options,hover_line)
    hover_line = hover_line-1
    display.show()
    sleep_ms(700)
