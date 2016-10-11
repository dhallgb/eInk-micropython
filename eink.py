# MicroPython library for Waveshare 4.3 e-ink display
# Converted from the file epd.cpp released by Waveshare
# Doug Hall, 2016
#

from time import sleep
from machine import UART
from ustruct import pack_into
from ustruct import pack

DEBUG	= True

# commands
_cmd_read_baud			= b"\xA5\x00\x09\x02\xCC\x33\xC3\x3C\xAE"
_cmd_stopmode			= b"\xA5\x00\x09\x08\xCC\x33\xC3\x3C\xA4"
_cmd_load_font			= b"\xA5\x00\x09\x0E\xCC\x33\xC3\x3C\xA2"
_cmd_load_pic			= b"\xA5\x00\x09\x0F\xCC\x33\xC3\x3C\xA3"
_cmd_handshake			= b"\xA5\x00\x09\x00\xCC\x33\xC3\x3C\xAC"
_cmd_update				= b"\xA5\x00\x09\x0A\xCC\x33\xC3\x3C\xA6"
_cmd_clear				= b"\xA5\x00\x09\x2E\xCC\x33\xC3\x3C\x82"
_cmd_draw_circle		= b"\xA5\x00\x0F\x26\x00\x00\x00\x00\x00\x00\xCC\x33\xC3\x3C"
_cmd_fill_circle		= b"\xA5\x00\x0F\x27\x00\x00\x00\x00\x00\x00\xCC\x33\xC3\x3C"
_cmd_set_memory			= b"\xA5\x00\x0A\x07\x00\xCC\x33\xC3\x3C"
_cmd_screen_rotation	= b"\xA5\x00\x0A\x0D\x00\xCC\x33\xC3\x3C"
_cmd_set_colour			= b"\xA5\x00\x0B\x10\x00\x00\xCC\x33\xC3\x3C"
_cmd_set_en_font		= b"\xA5\x00\x0A\x1E\x00\xCC\x33\xC3\x3C"
_cmd_set_ch_font		= b"\xA5\x00\x0A\x1F\x00\xCC\x33\xC3\x3C"
_cmd_draw_pixel			= b"\xA5\x00\x0D\x20\x00\x00\x00\x00\xCC\x33\xC3\x3C"
_cmd_set_baud			= b"\xA5\x00\x0D\x01\x00\x00\x00\x00\xCC\x33\xC3\x3C"
_cmd_draw_line			= b"\xA5\x00\x11\x22\x00\x00\x00\x00\x00\x00\x00\x00\xCC\x33\xC3\x3C"
_cmd_fill_rect			= b"\xA5\x00\x11\x24\x00\x00\x00\x00\x00\x00\x00\x00\xCC\x33\xC3\x3C"
_cmd_draw_triangle		= b"\xA5\x00\x0F\x28\x00\x00\x00\x00\x00\x00\xCC\x33\xC3\x3C"
_cmd_fill_triangle		= b"\xA5\x00\x0F\x29\x00\x00\x00\x00\x00\x00\xCC\x33\xC3\x3C"

# colours
WHITE		= 0x03
GRAY 		= 0x02
DARK_GRAY 	= 0x01
BLACK 		= 0x00

# commands
CMD_DRAW_STRING 	= 0x30
CMD_DRAW_BITMAP		= 0x70

# fonts
GBK32 = 0x01
GBK48 = 0x02
GBK64 = 0x03
ASCII32 = 0x01
ASCII48 = 0x02
ASCII64 = 0x03

# memory
MEM_NAND = 0
MEM_TF = 1

# display
EPD_NORMAL		= 0
EPD_INVERSION	= 1

# pins
wake_up = 2
reset = 3

def printhex(s):
    print(type(s),len(s),":".join("{:02x}".format(c) for c in s))

def send(cmd):
	if DEBUG:
		printhex(cmd)
	uart.write(cmd)

def addparity(packet):
    parity = 0
    if type(packet) == bytes:
        for b in packet:
            parity ^= b
        return(b''.join((packet,pack('!B',parity))))
    elif type(packet) == bytearray:
        for b in packet:
            parity ^= b
        return(b''.join((packet,bytearray(pack('!B',parity)))))
    elif type(packet) == str:
        for i in packet:
            parity ^= ord(i)
        return(''.join((packet, chr(parity))))    
    else:
        return None

def eink_init():
	global uart
	uart = UART(0, baudrate=115200, pins=('GP12', 'GP13'))
#	TBC
#	pinMode(wake_up, HIGH)
#	pinMode(reset, HIGH)

def eink_reset(self, void):
	pass
#	TBC
#	digitalWrite(reset, LOW)
#	delayMicroseconds(10)
#	digitalWrite(reset, HIGH)
#	delayMicroseconds(500)
#	digitalWrite(reset, LOW)
#	delay(3000)

def eink_wakeup(self, void):
	pass
#	TBC
#	digitalWrite(wake_up, LOW)
#	delayMicroseconds(10)
#	digitalWrite(wake_up, HIGH)
#	delayMicroseconds(500)
#	digitalWrite(wake_up, LOW)
#	delay(10)

def eink_handshake():
	send(_cmd_handshake)

def eink_set_baud(baud):
	bcmd=bytearray(_cmd_set_baud)
    pack_into('!i',bcmd,4,baud)
    send(addparity(bcmd))
#	TBC
#	delay(10)
#	Serial.begin(baud)

def eink_read_baud():
	send(_cmd_read_baud)

def eink_set_memory(mode):
	bcmd=bytearray(_cmd_set_memory)
    pack_into('!B',bcmd,4,mode)
    send(addparity(bcmd))

def eink_enter_stopmode():
	send(_cmd_stopmode)

def eink_update():
	send(_cmd_update)

def eink_screen_rotation(mode):
	bcmd=bytearray(_cmd_set_memory)
    pack_into('!B',bcmd,4,mode)
    send(addparity(bcmd))

def eink_load_font():
	send(_cmd_load_font)

def eink_load_pic():
	send(_cmd_load_pic)

def eink_set_color(colour, bkcolour):
	bcmd=bytearray(_cmd_set_colour)
    pack_into('!BB',bcmd,4,colour,bkcolour)
    send(addparity(bcmd))

def eink_set_en_font(font):
	bcmd=bytearray(_cmd_set_en_font)
    pack_into('!B',bcmd,4,font)
    send(addparity(bcmd))

def eink_set_ch_font(font):
	bcmd=bytearray(_cmd_set_ch_font)
    pack_into('!B',bcmd,4,font)
    send(addparity(bcmd))

def eink_draw_pixel(x, y):
	bcmd=bytearray(_cmd_draw_pixel)
    pack_into('!hh',bcmd,4,x,y)
    send(addparity(bcmd))

def eink_draw_line(x0, y0, x1, y1):
	bcmd=bytearray(_cmd_draw_line)
    pack_into('!hhhh',bcmd,4,x0,y0,x1,y1)
    send(addparity(bcmd))

def eink_fill_rect(x0, y0, x1, y1):
	bcmd=bytearray(_cmd_fill_rect)
    pack_into('!hhhh',bcmd,4,x0,y0,x1,y1)
    send(addparity(bcmd))

def eink_draw_circle(x, y, r):
	bcmd=bytearray(_cmd_draw_circle)
    pack_into('!hhh',bcmd,4,x,y,r)
    send(addparity(bcmd))

def eink_fill_circle(x, y, r):
	bcmd=bytearray(_cmd_fill_circle)
    pack_into('!hhh',bcmd,4,x,y,r)
    send(addparity(bcmd))

def eink_draw_triangle(x0, y0, x1, y1, x2, y2):
	bcmd=bytearray(_cmd_draw_triangle)
    pack_into('!hhh',bcmd,4,x,y,r)
    send(addparity(bcmd))

def eink_fill_triangle(x0, y0, x1, y1, x2, y2):
	bcmd=bytearray(_cmd_fill_triangle)
    pack_into('!hhh',bcmd,4,x,y,r)
    send(addparity(bcmd))

def eink_clear()
	send(_cmd_clear)
	send(_cmd_update)

def eink_disp_char(ch, x0, y0):
	eink_disp_string(ch, x0, y0)

def eink_disp_string(s, x0, y0):
	pass
#	int string_size
#	unsigned char ptr = (unsigned char *)p
#	string_size = strlen(( char *)ptr)
#	string_size += 14
#	_cmd_buff[0] = LEADING_FRAME
#	_cmd_buff[1] = (string_size >> 8) & 0xFF
#	_cmd_buff[2] = string_size & 0xFF
#	_cmd_buff[3] = CMD_DRAW_STRING
#	_cmd_buff[4] = (x0 >> 8) & 0xFF
#	_cmd_buff[5] = x0 & 0xFF
#	_cmd_buff[6] = (y0 >> 8) & 0xFF
#	_cmd_buff[7] = y0 & 0xFF
#	strcpy((char *)(&_cmd_buff[8]), ( char *)ptr)
#	string_size -= 5
#	_cmd_buff[string_size] = FRAME_E0
#	_cmd_buff[string_size + 1] = FRAME_E1
#	_cmd_buff[string_size + 2] = FRAME_E2
#	_cmd_buff[string_size + 3] = FRAME_E3
#	_cmd_buff[string_size + 4] = _verify(_cmd_buff, string_size + 4)
#	writeDisplay(_cmd_buff, string_size + 5)

def eink_disp_bitmap(bitmap, x, y):
	pass
#	int string_size
#	unsigned char ptr = (unsigned char *)p
#	string_size = strlen(( char *)ptr)
#	string_size += 14
#	_cmd_buff[0] = LEADING_FRAME
#	_cmd_buff[1] = (string_size >> 8) & 0xFF
#	_cmd_buff[2] = string_size & 0xFF
#	_cmd_buff[3] = CMD_DRAW_BITMAP
#	_cmd_buff[4] = (x0 >> 8) & 0xFF
#	_cmd_buff[5] = x0 & 0xFF
#	_cmd_buff[6] = (y0 >> 8) & 0xFF
#	_cmd_buff[7] = y0 & 0xFF
#	strcpy((char *)(&_cmd_buff[8]), ( char *)ptr)
#	string_size -= 5
#	_cmd_buff[string_size] = FRAME_E0
#	_cmd_buff[string_size + 1] = FRAME_E1
#	_cmd_buff[string_size + 2] = FRAME_E2
#	_cmd_buff[string_size + 3] = FRAME_E3
#	_cmd_buff[string_size + 4] = _verify(_cmd_buff, string_size + 4)
#	writeDisplay(_cmd_buff, string_size + 5)
