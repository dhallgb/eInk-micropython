# MicroPython library for Waveshare 4.3 e-ink display
# Converted from the file epd.cpp released by Waveshare
# Doug Hall, 2016
#
# TBC:
#    - eink_init (add pins wakeup and reset to high)?
#    - eink_wakeup
#    - eink_reset
#

from machine import UART
from ustruct import pack_into
from ustruct import pack

# commands
_cmd_handshake       = b"\xA5\x00\x09\x00\xCC\x33\xC3\x3C\xAC"
_cmd_set_baud        = b"\xA5\x00\x0D\x01\x00\x00\x00\x00\xCC\x33\xC3\x3C"
_cmd_read_baud       = b"\xA5\x00\x09\x02\xCC\x33\xC3\x3C\xAE"
_cmd_set_memory      = b"\xA5\x00\x0A\x07\x00\xCC\x33\xC3\x3C"
_cmd_stopmode        = b"\xA5\x00\x09\x08\xCC\x33\xC3\x3C\xA4"
_cmd_update          = b"\xA5\x00\x09\x0A\xCC\x33\xC3\x3C\xA6"
_cmd_screen_rotation = b"\xA5\x00\x0A\x0D\x00\xCC\x33\xC3\x3C"
_cmd_load_font       = b"\xA5\x00\x09\x0E\xCC\x33\xC3\x3C\xA2"
_cmd_load_pic        = b"\xA5\x00\x09\x0F\xCC\x33\xC3\x3C\xA3"
_cmd_set_colour      = b"\xA5\x00\x0B\x10\x00\x00\xCC\x33\xC3\x3C"
_cmd_set_en_font     = b"\xA5\x00\x0A\x1E\x00\xCC\x33\xC3\x3C"
_cmd_set_ch_font     = b"\xA5\x00\x0A\x1F\x00\xCC\x33\xC3\x3C"
_cmd_draw_pixel      = b"\xA5\x00\x0D\x20\x00\x00\x00\x00\xCC\x33\xC3\x3C"
_cmd_draw_line       = b"\xA5\x00\x11\x22\x00\x00\x00\x00\x00\x00\x00\x00\xCC\x33\xC3\x3C"
_cmd_fill_rect       = b"\xA5\x00\x11\x24\x00\x00\x00\x00\x00\x00\x00\x00\xCC\x33\xC3\x3C"
_cmd_draw_rect       = b"\xA5\x00\x11\x25\x00\x00\x00\x00\x00\x00\x00\x00\xCC\x33\xC3\x3C"
_cmd_draw_circle     = b"\xA5\x00\x0F\x26\x00\x00\x00\x00\x00\x00\xCC\x33\xC3\x3C"
_cmd_fill_circle     = b"\xA5\x00\x0F\x27\x00\x00\x00\x00\x00\x00\xCC\x33\xC3\x3C"
_cmd_draw_triangle   = b"\xA5\x00\x15\x28\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xCC\x33\xC3\x3C"
_cmd_fill_triangle   = b"\xA5\x00\x15\x29\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xCC\x33\xC3\x3C"
_cmd_clear           = b"\xA5\x00\x09\x2E\xCC\x33\xC3\x3C\x82"
_cmd_draw_string     = b"\xA5\x00\x00\x30\x00\x00\x00\x00"
_cmd_draw_bitmap     = b"\xA5\x00\x00\x70\x00\x00\x00\x00"

# colours
WHITE       = 0x03
GRAY        = 0x02
DARK_GRAY   = 0x01
BLACK       = 0x00

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
EPD_NORMAL      = 0
EPD_INVERSION   = 1

# pins
uartnum = 1
Tx = 'G12'
Rx = 'G13'
wake_up = 2
reset = 3

def printhex(s):
    print(type(s),len(s),":".join("{:02x}".format(c) for c in s))

def send(cmd):
#    if __debug__:
#        printhex(cmd)
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
        packet.append(parity)
        return(packet)
    elif type(packet) == str:
        for i in packet:
            parity ^= ord(i)
        return(''.join((packet, chr(parity))))    
    else:
        return None

def eink_init():
    global uart
    uart = UART(uartnum, baudrate=115200, pins=(Tx, Rx))

def eink_reset():
    pass

def eink_wakeup():
    pass

def eink_handshake():
    send(_cmd_handshake)

def eink_set_baud(baud):
    bcmd = bytearray(_cmd_set_baud)
    pack_into('!i',bcmd,4,baud)
    send(addparity(bcmd))

def eink_read_baud():
    send(_cmd_read_baud)

def eink_set_memory(mode):
    bcmd = bytearray(_cmd_set_memory)
    pack_into('!B',bcmd,4,mode)
    send(addparity(bcmd))

def eink_enter_stopmode():
    send(_cmd_stopmode)

def eink_update():
    send(_cmd_update)

def eink_screen_rotation(mode):
    bcmd = bytearray(_cmd_set_memory)
    pack_into('!B',bcmd,4,mode)
    send(addparity(bcmd))

def eink_load_font():
    send(_cmd_load_font)

def eink_load_pic():
    send(_cmd_load_pic)

def eink_set_color(colour, bkcolour):
    bcmd = bytearray(_cmd_set_colour)
    pack_into('!BB',bcmd,4,colour,bkcolour)
    send(addparity(bcmd))

def eink_set_en_font(font):
    bcmd = bytearray(_cmd_set_en_font)
    pack_into('!B',bcmd,4,font)
    send(addparity(bcmd))

def eink_set_ch_font(font):
    bcmd = bytearray(_cmd_set_ch_font)
    pack_into('!B',bcmd,4,font)
    send(addparity(bcmd))

def eink_draw_pixel(x, y):
    bcmd = bytearray(_cmd_draw_pixel)
    pack_into('!hh',bcmd,4,x,y)
    send(addparity(bcmd))

def eink_draw_line(x0, y0, x1, y1):
    bcmd = bytearray(_cmd_draw_line)
    pack_into('!hhhh',bcmd,4,x0,y0,x1,y1)
    send(addparity(bcmd))

def eink_draw_rect(x0, y0, x1, y1):
    bcmd = bytearray(_cmd_draw_rect)
    pack_into('!hhhh',bcmd,4,x0,y0,x1,y1)
    send(addparity(bcmd))

def eink_fill_rect(x0, y0, x1, y1):
    bcmd = bytearray(_cmd_fill_rect)
    pack_into('!hhhh',bcmd,4,x0,y0,x1,y1)
    send(addparity(bcmd))

def eink_draw_circle(x, y, r):
    bcmd = bytearray(_cmd_draw_circle)
    pack_into('!hhh',bcmd,4,x,y,r)
    send(addparity(bcmd))

def eink_fill_circle(x, y, r):
    bcmd = bytearray(_cmd_fill_circle)
    pack_into('!hhh',bcmd,4,x,y,r)
    send(addparity(bcmd))

def eink_draw_triangle(x0, y0, x1, y1, x2, y2):
    bcmd = bytearray(_cmd_draw_triangle)
    pack_into('!hhhhhh',bcmd,4,x0,y0,x1,y1,x2,y2)
    send(addparity(bcmd))

def eink_fill_triangle(x0, y0, x1, y1, x2, y2):
    bcmd = bytearray(_cmd_fill_triangle)
    pack_into('!hhhhhh',bcmd,4,x0,y0,x1,y1,x2,y2)
    send(addparity(bcmd))

def eink_clear():
    send(_cmd_clear)
    send(_cmd_update)

def eink_disp_char(ch, x, y):
    eink_disp_string(ch, x, y)

def eink_disp_string(s, x, y):
    bcmd = bytearray(_cmd_draw_string)
    pack_into('!hh',bcmd,4,x,y)
    bcmd.extend(s.encode('hex'))
    bcmd.extend(b'\x00\xCC\x33\xC3\x3C')
    bcmd[2] = len(bcmd)+1
    send(addparity(bcmd))

def eink_disp_bitmap(bm, x, y):
    bcmd = bytearray(_cmd_draw_bitmap)
    pack_into('!hh',bcmd,4,x,y)
    bcmd.extend(bm.encode())
    bcmd.extend(b'\x00\xCC\x33\xC3\x3C')
    bcmd[2] = len(bcmd)+1
    send(addparity(bcmd))
