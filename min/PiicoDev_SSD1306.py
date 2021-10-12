_C='Linux'
_B='microbit'
_A=None
_SET_CONTRAST=129
_SET_ENTIRE_ON=164
_SET_NORM_INV=166
_SET_DISP=174
_SET_MEM_ADDR=32
_SET_COL_ADDR=33
_SET_PAGE_ADDR=34
_SET_DISP_START_LINE=64
_SET_SEG_REMAP=160
_SET_MUX_RATIO=168
_SET_IREF_SELECT=173
_SET_COM_OUT_DIR=192
_SET_DISP_OFFSET=211
_SET_COM_PIN_CFG=218
_SET_DISP_CLK_DIV=213
_SET_PRECHARGE=217
_SET_VCOM_DESEL=219
_SET_CHARGE_PUMP=141
WIDTH=128
HEIGHT=64
from PiicoDev_Unified import *
compat_str='\nUnified PiicoDev library out of date.  Get the latest module: https://piico.dev/unified \n'
_SYSNAME=os.uname().sysname
if _SYSNAME==_B:from microbit import *;from utime import sleep_ms;from ustruct import pack_into
elif _SYSNAME==_C:from PIL import Image,ImageDraw,ImageFont;from struct import pack_into
else:import framebuf
if _SYSNAME==_B or _SYSNAME==_C:
	class framebuf:
		class FrameBuffer:
			def _set_pos(self,col=0,page=0):self.write_cmd(176|page);c1,c2=col*2&15,col>>3;self.write_cmd(0|c1);self.write_cmd(16|c2)
			def fill(self,c=0):
				for i in range(0,1024):
					if c>0:self.buffer[i]=255
					else:self.buffer[i]=0
			def pixel(self,x,y,color):x=x&WIDTH-1;y=y&HEIGHT-1;page,shift_page=divmod(y,8);ind=x+page*128;b=self.buffer[ind]|1<<shift_page if color else self.buffer[ind]&~(1<<shift_page);pack_into('>B',self.buffer,ind,b);self._set_pos(x,page)
			def line(self,x1,y1,x2,y2,c):
				steep=abs(y2-y1)>abs(x2-x1)
				if steep:tmp=x1;x1=y1;y1=tmp;tmp=y2;y2=x2;x2=tmp
				if x1>x2:tmp=x1;x1=x2;x2=tmp;tmp=y1;y1=y2;y2=tmp
				dx=x2-x1;dy=abs(y2-y1);err=dx/2
				if y1<y2:ystep=1
				else:ystep=-1
				while x1<=x2:
					if steep:self.pixel(y1,x1,c)
					else:self.pixel(x1,y1,c)
					err-=dy
					if err<0:y1+=ystep;err+=dx
					x1+=1
			def hline(self,x,y,l,c):self.line(x,y,x+l,y,c)
			def vline(self,x,y,h,c):self.line(x,y,x,y+h,c)
			def rect(self,x,y,w,h,c):self.hline(x,y,w,c);self.hline(x,y+h,w,c);self.vline(x,y,h,c);self.vline(x+w,y,h,c)
			def fill_rect(self,x,y,w,h,c):
				for i in range(y,y+h):self.hline(x,i,w,c)
			def text(self,text,x,y,c=1):
				fontFile=open('font-pet-me-128.dat','rb');font=bytearray(fontFile.read())
				for text_index in range(0,len(text)):
					ind=0
					for col in range(8):
						fontDataPixelValues=font[(ord(text[text_index])-32)*8+col]
						for i in range(0,7):
							if fontDataPixelValues&1<<i!=0:
								x_coordinate=x+col+text_index*8;y_coordinate=y+i
								if x_coordinate<WIDTH and y_coordinate<HEIGHT:self.pixel(x_coordinate,y_coordinate,c)
class PiicoDev_SSD1306(framebuf.FrameBuffer):
	def init_display(self):
		self.width=WIDTH;self.height=HEIGHT;self.pages=HEIGHT//8;self.buffer=bytearray(self.pages*WIDTH)
		for cmd in (_SET_DISP,_SET_MEM_ADDR,0,_SET_DISP_START_LINE,_SET_SEG_REMAP|1,_SET_MUX_RATIO,HEIGHT-1,_SET_COM_OUT_DIR|8,_SET_DISP_OFFSET,0,_SET_COM_PIN_CFG,18,_SET_DISP_CLK_DIV,128,_SET_PRECHARGE,241,_SET_VCOM_DESEL,48,_SET_CONTRAST,255,_SET_ENTIRE_ON,_SET_NORM_INV,_SET_IREF_SELECT,48,_SET_CHARGE_PUMP,20,_SET_DISP|1):self.write_cmd(cmd)
	def poweroff(self):self.write_cmd(_SET_DISP)
	def poweron(self):self.write_cmd(_SET_DISP|1)
	def setContrast(self,contrast):self.write_cmd(_SET_CONTRAST);self.write_cmd(contrast)
	def invert(self,invert):self.write_cmd(_SET_NORM_INV|invert&1)
	def rotate(self,rotate):self.write_cmd(_SET_COM_OUT_DIR|(rotate&1)<<3);self.write_cmd(_SET_SEG_REMAP|rotate&1)
	def show(self):x0=0;x1=WIDTH-1;self.write_cmd(_SET_COL_ADDR);self.write_cmd(x0);self.write_cmd(x1);self.write_cmd(_SET_PAGE_ADDR);self.write_cmd(0);self.write_cmd(self.pages-1);self.write_data(self.buffer)
	def write_cmd(self,cmd):
		try:self.i2c.writeto_mem(self.addr,int.from_bytes(b'\x80','big'),bytes([cmd]));self.comms_err=False
		except:print(i2c_err_str.format(self.addr));self.comms_err=True
	def write_data(self,buf):
		try:self.write_list[1]=buf;self.i2c.writeto_mem(self.addr,int.from_bytes(self.write_list[0],'big'),self.write_list[1]);self.comms_err=False
		except:print(i2c_err_str.format(self.addr));self.comms_err=True
	def load_pbm(self,filename,c):
		with open(filename,'rb')as f:f.readline();f.readline();f.readline();data_piicodev=bytearray(f.read())
		for byte in range(WIDTH//8*HEIGHT):
			for bit in range(8):
				if data_piicodev[byte]&1<<bit!=0:
					x_coordinate=(8-bit+byte*8)%WIDTH;y_coordinate=byte*8//WIDTH
					if x_coordinate<WIDTH and y_coordinate<HEIGHT:self.pixel(x_coordinate,y_coordinate,c)
class PiicoDev_SSD1306_MicroPython(PiicoDev_SSD1306):
	def __init__(self,bus=_A,freq=_A,sda=_A,scl=_A,addr=60):self.i2c=create_unified_i2c(bus=bus,freq=freq,sda=sda,scl=scl);self.addr=addr;self.temp=bytearray(2);self.write_list=[b'@',_A];self.init_display();super().__init__(self.buffer,WIDTH,HEIGHT,framebuf.MONO_VLSB);self.fill(0);self.show()
class PiicoDev_SSD1306_MicroBit(PiicoDev_SSD1306):
	def __init__(self,bus=_A,freq=_A,sda=_A,scl=_A,addr=60):self.i2c=create_unified_i2c(bus=bus,freq=freq,sda=sda,scl=scl);self.addr=addr;self.temp=bytearray(2);self.write_list=[b'@',_A];self.init_display();self.fill(0);self.show()
class PiicoDev_SSD1306_Linux(PiicoDev_SSD1306):
	def __init__(self,bus=_A,freq=_A,sda=_A,scl=_A,addr=60):self.i2c=create_unified_i2c(bus=bus,freq=freq,sda=sda,scl=scl);self.addr=addr;self.temp=bytearray(2);self.write_list=[b'@',_A];self.image=Image.new('1',(WIDTH,HEIGHT));self.draw=ImageDraw.Draw(self.image);self.init_display();self.fill(0);self.show()
def create_PiicoDev_SSD1306(addr=60,bus=_A,freq=_A,sda=_A,scl=_A):
	try:
		if compat_ind>=1:0
		else:print(compat_str)
	except:print(compat_str)
	if _SYSNAME==_B:display=PiicoDev_SSD1306_MicroBit(addr=addr,freq=freq)
	elif _SYSNAME==_C:display=PiicoDev_SSD1306_Linux(addr=addr,freq=freq)
	else:display=PiicoDev_SSD1306_MicroPython(addr=addr,bus=bus,freq=freq,sda=sda,scl=scl)
	return display