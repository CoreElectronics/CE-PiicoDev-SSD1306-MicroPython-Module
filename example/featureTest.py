# PiicoDev SSD1306 minimal example code
# This program writes to PiicoDev SSD1306 OLED display driver

import math
import os
_SYSNAME = os.uname().sysname

from PiicoDev_SSD1306 import *

if _SYSNAME == 'microbit':
    from microbit import * # uses Image, Display
    from time import sleep
    from utime import ticks_ms
elif _SYSNAME == 'Linux':
    pass
else:
    import sys
    from time import sleep
    from utime import ticks_ms

display = create_PiicoDev_SSD1306()
WIDTH = display.width
HEIGHT = display.height

print(type(display))

delay=500

display.rotate(True)
display.invert(False)

print('Test Pattern Fill 1')
display.fill(1)
display.show()
sleep_ms(delay)

print('Test Pattern Fill 0')
display.fill(0)
display.show()
sleep_ms(delay)

print('Test Pattern Pixel Range')
display.fill(0)
display.pixel(0,0,1)
display.pixel(1,1,1)
display.pixel(2,2,1)
display.pixel(127,0,1)
display.pixel(126,1,1)
display.pixel(0,63,1)
display.pixel(1,62,1)
display.pixel(126,62,1)
display.pixel(127,63,1)
display.show()
sleep_ms(delay)

print('Test Pattern Pixel Range Inverted')
display.fill(1)
display.pixel(0,0,0)
display.pixel(1,1,0)
display.pixel(2,2,0)
display.pixel(127,0,0)
display.pixel(126,1,0)
display.pixel(0,63,0)
display.pixel(1,62,0)
display.pixel(126,62,0)
display.pixel(127,63,0)
display.show()
sleep_ms(delay)

print('Test Pattern Horizontal Lines')
display.fill(0)
display.hline(0, 1, WIDTH,1)
display.hline(31, 31, 64, 1)
display.hline(0, 62, WIDTH, 1)
display.show()
sleep_ms(delay)

print('Test Pattern Horizontal Lines Inverted')
display.fill(1)
display.hline(0, 1, WIDTH, 0)
display.hline(31, 31, 64, 0)
display.hline(0, 62, WIDTH, 0)
display.show()

print('Test Pattern Vertical Lines')
display.fill(0)
display.vline(1, 0, HEIGHT, 1)
display.vline(63, 15, 32, 1)
display.vline(126, 0, HEIGHT, 1)
display.show()
sleep_ms(delay)

print('Test Pattern Vertical Lines Inverted')
display.fill(1)
display.vline(1, 0, HEIGHT, 0)
display.vline(63, 15, 32, 0)
display.vline(126, 0, HEIGHT, 0)
display.show()
sleep_ms(delay)

print('Test Pattern Lines')
display.fill(0)
display.line(0, 0, WIDTH, HEIGHT, 1)
display.line(0, HEIGHT, WIDTH, 0, 1)
display.show()
sleep_ms(delay)

print('Test Pattern Lines Inverted')
display.fill(1)
display.line(0, 0, WIDTH, HEIGHT, 0)
display.line(0, HEIGHT, WIDTH, 0, 0)
display.show()
sleep_ms(delay)

print('Test Pattern Rectangle')
display.fill(0)
display.rect(53, 16, 20, 30, 1)
display.show()
sleep_ms(delay)

print('Test Pattern Rectangle Inverted')
display.fill(1)
display.rect(53, 16, 20, 30, 0)
display.show()
sleep_ms(delay)

print('Test Pattern Filled Rectangle')
display.fill(0)
display.fill_rect(53, 16, 20, 30, 1)
display.show()
sleep_ms(delay)

print('Test Pattern Filled Rectangle Inverted')
display.fill(1)
display.fill_rect(53, 16, 20, 30, 0)
display.show()
sleep_ms(delay)

print('Test Pattern Text')
display.fill(0)
display.text('PiicoDev',32,22,1)
display.show()
sleep_ms(delay)

print('Test Pattern Text Inverted')
display.fill(1)
display.text('PiicoDev',32,22,0)
display.show()
sleep_ms(delay)

print('Test Pattern Arc and Circle')
display.fill(0)
display.circ(20,20,8)
display.circ(128-20,20,8)
display.arc(64,-10,70,60,120,0)
display.show()
sleep_ms(delay)

print('Test Pattern Bitmap')
display.fill(0)
display.load_pbm('piicodev-logo.pbm', 1)
display.show()
sleep_ms(delay)

print('Test Pattern Bitmap Inverted')
display.fill(1)
display.load_pbm('piicodev-logo.pbm', 0)
display.show()
sleep_ms(delay)

print('Test Pattern Example')
display.fill(0)
display.load_pbm('weather.pbm', 1)
display.text('26 degC',0,15)
display.text('90 %', 0, 30)
display.text('1015 hPa', 0, 45)
display.show()
sleep_ms(3000)

print('Test Pattern Maths')
display.fill(0)
x_prev=0.0
y_prev=HEIGHT/2.0
for x in range(WIDTH):
    y = int(math.sin(x/10.0)*HEIGHT/2+HEIGHT/2.0)
    display.line(int(x_prev), int(y_prev), int(x), int(y), 1)
    x_prev=x
    y_prev=y
display.show()
if _SYSNAME == 'rp2' or _SYSNAME == 'LoPy4':
    for x in range(WIDTH):
        display.scroll(-1,0)
        display.show()
    display.text('PiicoDev',32,22,1)
    display.show()
    
graph1 = display.graph2D()
graph2 = display.graph2D()
sleep_ms(1000)
for x in range(1000):
    y = int(math.sin(x/10.0)*HEIGHT+HEIGHT+30)
    z = int(math.cos(x/10.0)*HEIGHT+HEIGHT+30)
    display.fill(0)
    display.updateGraph2D(graph1,y)
    display.updateGraph2D(graph2,z)
    display.show()
    sleep_ms(1)
