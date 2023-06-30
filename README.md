# PiicoDev® OLED Module SSD1306 -  MicroPython Module

This is the firmware repo for the [Core Electronics PiicoDev® OLED Module](https://core-electronics.com.au/catalog/product/view/sku/CE07911)

This module depends on the [PiicoDev Unified Library](https://github.com/CoreElectronics/CE-PiicoDev-Unified), include `PiicoDev_Unified.py` in the project directory on your MicroPython device.


See the [Quickstart Guide](https://piico.dev/p14)


## Details
### `create_PiicoDev_SSD1306(bus=, freq=, sda=, scl=, addr=0x3C)`
Parameter | Type | Range | Default | Description
--- | --- | --- | --- | ---
bus | int | 0,1 | Raspberry Pi Pico: 0, Raspberry Pi: 1 | I2C Bus.  Ignored on Micro:bit
freq | int | 100-1000000 | Device dependent | I2C Bus frequency (Hz).  Ignored on Raspberry Pi
sda | Pin | Device Dependent | Device Dependent | I2C SDA Pin. Implemented on Raspberry Pi Pico only
scl | Pin | Device Dependent | Device Dependent | I2C SCL Pin. Implemented on Raspberry Pi Pico only
addr | int | 0x3C | 0x3C, 0x3D | This address needs to match the PiicoDev OLED SSD1306 hardware address configured by the jumper

### `PiicoDev_SSD1306.show()`
This command is required to send the image assembled using the commands below to the display for viewing.

### `PiicoDev_SSD1306.fill(c)`
Parameter | Type | Range | Description
--- | --- | --- | ---
c | int | 0 - 1 | Fill the display with a single colour (0: Black, 1: White)

### `PiicoDev_SSD1306.pixel(x, y, c)`
Parameter | Type | Range | Description
--- | --- | --- | ---
x | int | 0 - 127 | X coordinate
y | int | 0 - 63 | Y coordinate
c | int | 0 - 1 | Set the specified pixel to the given color (0: Black, 1: White)

### `PiicoDev_SSD1306.hline(x, y, l, c)`
Draw a horizontal line with a given length using the given colour and a thickness of 1 pixel.

Parameter | Type | Range | Description
--- | --- | --- | ---
x | int | 0 - 127 | X coordinate
y | int | 0 - 63 | Y coordinate
l | int | 1 - 128 | Length
c | int | 0 - 1 | Set the line to the given color (0: Black, 1: White)

### `PiicoDev_SSD1306.vline(x, y, h, c)`
Draw a vertical line with a given length using the given colour and a thickness of 1 pixel.

Parameter | Type | Range | Description
--- | --- | --- | ---
x | int | 0 - 127 | X coordinate
y | int | 0 - 63 | Y coordinate
l | int | 1 - 64 | Length
c | int | 0 - 1 | Set the line to the given color (0: Black, 1: White)

### `PiicoDev_SSD1306.line(x1, y1, x2, y2, c)`
Draw a line from a set of coordinates using the given colour and a thickness of 1 pixel up to a second set of coordinates.

Parameter | Type | Range | Description
--- | --- | --- | ---
x1 | int | 0 - 127 | X1 coordinate
y1 | int | 0 - 63 | Y1 coordinate
x2 | int | 0 - 127 | X2 coordinate
y2 | int | 0 - 63 | Y2 coordinate
c | int | 0 - 1 | Set the line to the given color (0: Black, 1: White)

### `PiicoDev_SSD1306.print(txt, c, line_num=None, auto_scroll=True, delim=True, font_size=[8,8], spacing=[0,0,0])`
Print text on the OLED, each subsequent call will increment the line number from the bottom of the display.

Parameter | Type | Range | Default | Description
--- | --- | --- | --- | ---
txt | string | Dependent | | Text to display.
c | int | 0 - 1 | 1 | The colour of the printed text
line_num | int | 0 - 8 (Dependent) | 0 | Optional: Prints on the requested line, default scrolls the text upwards
blanking | bool | True/False | True | When enabled each print() call redraws the display
delim | int | 0 - 16 | 1 | Set = 0/False to disable Delimiting
font_size | list of Integers | [1 - Font Width,1 - Font Height] | [8,8] | Used in calculations for the line spacing
spacing | list of Integers | [X-Starting Point, Y-Starting Point, Y-Spacing] | [0,0,0] | [X Starting Coordinate for all strings, Y Starting Coordinate for the first text write, Vertical spacing between Characters ]


### `PiicoDev_SSD1306.rect(x, y, w, h, c)`
Draw a rectangle at the given location, size and color. Draws only a 1 pixel outline.

Parameter | Type | Range | Description
--- | --- | --- | ---
x | int | 0 - 127 | X coordinate
y | int | 0 - 63 | Y coordinate
w | int | 1 - 128 | Width
h | int | 1 - 64 | Height
c | int | 0 - 1 | Set the line to the given color (0: Black, 1: White)

### `PiicoDev_SSD1306.fill_rect(x, y, w, h, c)`
Draw a rectangle at the given location, size and color. Draws both the outline and interior.

Parameter | Type | Range | Description
--- | --- | --- | ---
x | int | 0 - 127 | X coordinate
y | int | 0 - 63 | Y coordinate
w | int | 1 - 128 | Width
h | int | 1 - 64 | Height
c | int | 0 - 1 | Set the line to the given color (0: Black, 1: White)

### `PiicoDev_SSD1306.circ(x, y, r, t, c)`
Draw a circle at the given location, with radius and set thickness.
Parameter | Type | Range | Description
--- | --- | --- | ---
x | int | 0 - 127 | X coordinate
y | int | 0 - 63 | Y coordinate
r | int | 0 - 144 | Radius of the circle
t | float | 0.0 - 1.0 | How filled the circle is, starting from the outer edge, 0 being a line and 1 being fully filled
c | int | 0 - 1 | Set the line to the given color (0: Black, 1: White)

### `PiicoDev_SSD1306.arc(x, y, r, stAng, enAng, t, c)`
Draw an arc at the given location, with radius, start angle, end angle and set thickness.
Parameter | Type | Range | Description
--- | --- | --- | ---
x | int | 0 - 127 | X coordinate
y | int | 0 - 63 | Y coordinate
r | int | 0 - 144 | Radius of the arc
stAng | int | 0 - 359| Starting angle of the arc, must be less than the ending angle
enAng | int | 1 - 360| Ending angle of the arc, must be greater than the starting angle
t | float | 0.0 - 1.0 | How filled the arc is, starting from the outer edge, 0 being a line and 1 being fully filled
c | int | 0 - 1 | Set the line to the given color (0: Black, 1: White)

### `PiicoDev_SSD1306.text(s, x, y, c=1)`
Write text to the FrameBuffer using the the coordinates as the upper-left corner of the text.  
Dimensions are 8 x 8.  There is no way to change the font.

Parameter | Type | Range | Default | Description
--- | --- | --- | --- | ---
s | string | 16 characters max | | Text to display.  If the text is longer than 16 characters, it will be truncated.
x | int | 0 - 127 | | X coordinate
y | int | 0 - 127 | | Y coordinate
c | int | 0 - 1 | 1 | Set the line to the given color (0: Black, 1: White)

### `PiicoDev_SSD1306.load_pbm(filename, c)`
Load a pbm file to the FrameBuffer.  
It is recommended to use a pbm file generated by the GNU Image Manipulation Program (GIMP).

Parameter | Type | Range | Description
--- | --- | --- | ---
filename | string | | Image to display
c | int | 0 - 1 | Only pixels with this colour will be drawn (0: Black, 1: White)

### `PiicoDev_SSD1306.graph2D(originX, originY, width, height, minValue, maxValue, c, bgColour, bars)`
A graph2D object will be drawn to a rectangular region specified by the origin, width, and height.  
This graph type is explicitly designed to draw time series data.

Parameter | Type | Range | Default | Description
--- | --- | --- | --- | ---
originX  | int | 0 - 127 | 0 | The x coordinate of the graph's origin (lower left corner).
originY  | int | 0 - 63 | 63 | The y coordinate of the graph's origin (lower left corner).
width    | int | 1-128 | 128 | The width, in pixels, of the graph's drawing area.
height  	| int | 1-64 | 64 | The height, in pixels, of the graph's drawing area
minValue	| int | | 0 | The value which will be mapped to the bottom edge.
maxValue |	int | | 255 | The value which will be mapped to the upper edge.
c        |	int | 0 - 1 | 1 | Colour value. (0: Black, 1: White)
bars     | | | | Filled chart

### `PiicoDev_SSD1306.updateGraph2D(graph, value)`
Updates a 2D graph with a new value.

Parameter | Type | Description
--- | --- | ---
graph	| graph | A graph2D object created graph2D
value	| int | A new value to draw to the graph. This value will be drawn on the right edge and the oldest value will be deleted.

### `PiicoDev_SSD1306.scroll(xstep, ystep)` Raspberry Pi Pico & Pycom only
Raspberry Pi Pico and Pycom only.  Shift the contents of the FrameBuffer by the given vector.  This may leave a footprint of the previous colors in the FrameBuffer.

Parameter | Type | Range | Description
--- | --- | --- | ---
xstep | int | 0 - 127 | X coordinate
ystep | int | 0 - 63 | Y coordinate


### `PiicoDev_SSD1306.blit(fbuf, x, y, key)` Raspberry Pi Pico & Pycom only
Raspberry Pi Pico and Pycom only.  Draw another FrameBuffer on top of the current one at the given coordinates.  If key is specified then it should be a color integer and the corresponding color will be considered transparent: all pixels with that color value will not be drawn.

Parameter | Type | Range | Default | Description
--- | --- | --- | --- | ---
fbuf | FrameBuffer | 1024 bytes max  || Image to display
x | int | 0 - 127 | | X coordinate
y | int | 0 - 63 |  | Y coordinate
key | int | 0 - 1 | -1 | Key

### `PiicoDev_SSD1306.poweroff()`
Turns off the display.

### `PiicoDev_SSD1306.poweron()`
Turns on the display.

### `PiicoDev_SSD1306.setContrast(contrast)`
Parameter | Type | Range | Default | Description
--- | --- | --- | --- | ---
contrast | int | 0 - 255 | 255 | Set the contrast.

### `PiicoDev_SSD1306.rotate(rotate)`
Parameter | Type | Range | Default | Description
--- | --- | --- | --- | ---
rotate | int | 0 - 1 | 1 | Rotate the image by 180 degrees (1: Normal, 0: Inverted).

### `PiicoDev_SSD1306.invert(invert)`
Parameter | Type | Range | Default | Description
--- | --- | --- | --- | ---
invert | int | 0 - 1 | 0 | Invert the image so black is white and white is black (0: Normal, 1: Inverted).

# License
This project is open source - please review the LICENSE.md file for further licensing information.

If you have any technical questions, or concerns about licensing, please contact technical support on the [Core Electronics forums](https://forum.core-electronics.com.au/).

*\"PiicoDev\" and the PiicoDev logo are trademarks of Core Electronics Pty Ltd.*
