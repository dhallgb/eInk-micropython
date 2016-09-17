#
# This is a MicroPython library for the Waveshare 4.3 e-ink display
# Converted from the file eink.cpp released by Waveshare
# Doug Hall, 2016
#

#include <Arduino.h> - not converted yet, used for the serial interface

CMD_SIZE = 512
LEADING_FRAME = 0xA5
FRAME_E0 = 0xCC
FRAME_E1 = 0x33
FRAME_E2 = 0xC3
FRAME_E3 = 0x3C

# colors
WHITE = 0x03
GRAY = 0x02
DARK_GRAY = 0x01
BLACK = 0x00

# commands
CMD_HANDSHAKE = 0x00
CMD_SET_BAUD = 0x01
CMD_READ_BAUD = 0x02
CMD_MEMORYMODE = 0x07
CMD_STOPMODE = 0x08
CMD_UPDATE = 0x0A
CMD_SCREEN_ROTATION = 0x0D
CMD_LOAD_FONT = 0x0E
CMD_LOAD_PIC = 0x0F
CMD_SET_COLOR = 0x10
CMD_SET_EN_FONT = 0x1E
CMD_SET_CH_FONT = 0x1F
CMD_DRAW_PIXEL = 0x20
CMD_DRAW_LINE = 0x22
CMD_FILL_RECT = 0x24
CMD_DRAW_CIRCLE = 0x26
CMD_FILL_CIRCLE = 0x27
CMD_DRAW_TRIANGLE = 0x28
CMD_FILL_TRIANGLE = 0x29
CMD_CLEAR = 0x2E
CMD_DRAW_STRING = 0x30
CMD_DRAW_BITMAP = 0x70

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
EPD_NORMAL = 0
EPD_INVERSION = 1

# commands
_cmd_handshake[8] = {0xA5, 0x00, 0x09, CMD_HANDSHAKE, 0xCC, 0x33, 0xC3, 0x3C};
_cmd_read_baud[8] = {0xA5, 0x00, 0x09, CMD_READ_BAUD, 0xCC, 0x33, 0xC3, 0x3C};
_cmd_stopmode[8] = {0xA5, 0x00, 0x09, CMD_STOPMODE, 0xCC, 0x33, 0xC3, 0x3C};
_cmd_update[8] = {0xA5, 0x00, 0x09, CMD_UPDATE, 0xCC, 0x33, 0xC3, 0x3C};
_cmd_load_font[8] = {0xA5, 0x00, 0x09, CMD_LOAD_FONT, 0xCC, 0x33, 0xC3, 0x3C};
_cmd_load_pic[8] = {0xA5, 0x00, 0x09, CMD_LOAD_PIC, 0xCC, 0x33, 0xC3, 0x3C};
_cmd_buff[CMD_SIZE]

# pins
wake_up = 2
reset = 3


static void _putchars( unsigned char * ptr, n)
	int i, x
	for(i = 0; i < n; i++)
		x = ptr[i]
		Serial.write(x)

static unsigned char _verify( void * ptr, n)
	int i
	unsigned char p = (unsigned char *)ptr
	unsigned char result
	for(i = 0, result = 0; i < n; i++)
		result ^= p[i]
	return result





def eink_init(self, void):
	Serial.begin(115200)
	pinMode(wake_up, HIGH)
	pinMode(reset, HIGH)

def eink_reset(self, void):
	digitalWrite(reset, LOW)
	delayMicroseconds(10)
	digitalWrite(reset, HIGH)
	delayMicroseconds(500)
	digitalWrite(reset, LOW)
	delay(3000)

def eink_wakeup(self, void):
	digitalWrite(wake_up, LOW)
	delayMicroseconds(10)
	digitalWrite(wake_up, HIGH)
	delayMicroseconds(500)
	digitalWrite(wake_up, LOW)
	delay(10)


def eink_handshake(self, void):
	memcpy(_cmd_buff, _cmd_handshake, 8)
	_cmd_buff[8] = _verify(_cmd_buff, 8)

	_putchars(_cmd_buff, 9)

def eink_set_baud(self, baud):
	_cmd_buff[0] = LEADING_FRAME
	_cmd_buff[1] = 0x00
	_cmd_buff[2] = 0x0D
	_cmd_buff[3] = CMD_SET_BAUD
	_cmd_buff[4] = (baud >> 24) & 0xFF
	_cmd_buff[5] = (baud >> 16) & 0xFF
	_cmd_buff[6] = (baud >> 8) & 0xFF
	_cmd_buff[7] = baud & 0xFF
	_cmd_buff[8] = FRAME_E0
	_cmd_buff[9] = FRAME_E1
	_cmd_buff[10] = FRAME_E2
	_cmd_buff[11] = FRAME_E3
	_cmd_buff[12] = _verify(_cmd_buff, 12)
	_putchars(_cmd_buff, 13)
	delay(10)
	Serial.begin(baud)

def eink_read_baud(self, void):
	memcpy(_cmd_buff, _cmd_read_baud, 8)
	_cmd_buff[8] = _verify(_cmd_buff, 8)
	_putchars(_cmd_buff, 9)

'''******************************************************************************
* Function Name  : void eink_set_memory(unsigned char mode)
* Description    :
* Input          :
* Output         : None
* Return         :
* Attention		   : None
******************************************************************************'''
def eink_set_memory(self, char mode):
	_cmd_buff[0] = LEADING_FRAME

	_cmd_buff[1] = 0x00
	_cmd_buff[2] = 0x0A

	_cmd_buff[3] = CMD_MEMORYMODE

	_cmd_buff[4] = mode

	_cmd_buff[5] = FRAME_E0
	_cmd_buff[6] = FRAME_E1
	_cmd_buff[7] = FRAME_E2
	_cmd_buff[8] = FRAME_E3
	_cmd_buff[9] = _verify(_cmd_buff, 9)

	_putchars(_cmd_buff, 10)


'''******************************************************************************
* Function Name  : void eink_enter_stopmode(void)
* Description    :
* Input          :
* Output         : None
* Return         :
* Attention		   : None
******************************************************************************'''
def eink_enter_stopmode(self, void):
	memcpy(_cmd_buff, _cmd_stopmode, 8)
	_cmd_buff[8] = _verify(_cmd_buff, 8)

	_putchars(_cmd_buff, 9)

'''******************************************************************************
* Function Name  : void eink_udpate(void)
* Description    :
* Input          :
* Output         : None
* Return         :
* Attention		   : None
******************************************************************************'''
def eink_udpate(self, void):
	memcpy(_cmd_buff, _cmd_update, 8)
	_cmd_buff[8] = _verify(_cmd_buff, 8)

	_putchars(_cmd_buff, 9)

'''******************************************************************************
* Function Name  : void eink_screen_rotation(unsigned char mode)
* Description    :
* Input          :
* Output         : None
* Return         :
* Attention		   : None
******************************************************************************'''
def eink_screen_rotation(self, char mode):
	_cmd_buff[0] = LEADING_FRAME

	_cmd_buff[1] = 0x00
	_cmd_buff[2] = 0x0A

	_cmd_buff[3] = CMD_SCREEN_ROTATION

	_cmd_buff[4] = mode

	_cmd_buff[5] = FRAME_E0
	_cmd_buff[6] = FRAME_E1
	_cmd_buff[7] = FRAME_E2
	_cmd_buff[8] = FRAME_E3
	_cmd_buff[9] = _verify(_cmd_buff, 9)

	_putchars(_cmd_buff, 10)

'''******************************************************************************
* Function Name  : void eink_load_font(void)
* Description    :
* Input          :
* Output         : None
* Return         :
* Attention		   : None
******************************************************************************'''
def eink_load_font(self, void):
	memcpy(_cmd_buff, _cmd_load_font, 8)
	_cmd_buff[8] = _verify(_cmd_buff, 8)

	_putchars(_cmd_buff, 9)

'''******************************************************************************
* Function Name  : void eink_load_pic(void)
* Description    :
* Input          :
* Output         : None
* Return         :
* Attention		   : None
******************************************************************************'''
def eink_load_pic(self, void):
	memcpy(_cmd_buff, _cmd_load_pic, 8)
	_cmd_buff[8] = _verify(_cmd_buff, 8)

	_putchars(_cmd_buff, 9)

'''******************************************************************************
* Function Name  : void eink_set_color(unsigned char color, char bkcolor)
* Description    :
* Input          :
* Output         : None
* Return         :
* Attention		   : None
******************************************************************************'''
def eink_set_color(self, char color, char bkcolor):
	_cmd_buff[0] = LEADING_FRAME

	_cmd_buff[1] = 0x00
	_cmd_buff[2] = 0x0B

	_cmd_buff[3] = CMD_SET_COLOR

	_cmd_buff[4] = color
	_cmd_buff[5] = bkcolor

	_cmd_buff[6] = FRAME_E0
	_cmd_buff[7] = FRAME_E1
	_cmd_buff[8] = FRAME_E2
	_cmd_buff[9] = FRAME_E3
	_cmd_buff[10] = _verify(_cmd_buff, 10)

	_putchars(_cmd_buff, 11)

'''******************************************************************************
* Function Name  : void eink_set_en_font(unsigned char font)
* Description    :
* Input          :
* Output         : None
* Return         :
* Attention		   : None
******************************************************************************'''
def eink_set_en_font(self, char font):
	_cmd_buff[0] = LEADING_FRAME

	_cmd_buff[1] = 0x00
	_cmd_buff[2] = 0x0A

	_cmd_buff[3] = CMD_SET_EN_FONT

	_cmd_buff[4] = font

	_cmd_buff[5] = FRAME_E0
	_cmd_buff[6] = FRAME_E1
	_cmd_buff[7] = FRAME_E2
	_cmd_buff[8] = FRAME_E3
	_cmd_buff[9] = _verify(_cmd_buff, 9)

	_putchars(_cmd_buff, 10)

'''******************************************************************************
* Function Name  : void eink_set_ch_font(unsigned char font)
* Description    :
* Input          :
* Output         : None
* Return         :
* Attention		   : None
******************************************************************************'''
def eink_set_ch_font(self, char font):
	_cmd_buff[0] = LEADING_FRAME

	_cmd_buff[1] = 0x00
	_cmd_buff[2] = 0x0A

	_cmd_buff[3] = CMD_SET_CH_FONT

	_cmd_buff[4] = font

	_cmd_buff[5] = FRAME_E0
	_cmd_buff[6] = FRAME_E1
	_cmd_buff[7] = FRAME_E2
	_cmd_buff[8] = FRAME_E3
	_cmd_buff[9] = _verify(_cmd_buff, 9)

	_putchars(_cmd_buff, 10)

'''******************************************************************************
* Function Name  : void eink_draw_pixel(int x0, y0)
* Description    :
* Input          :
* Output         : None
* Return         :
* Attention		   : None
******************************************************************************'''
def eink_draw_pixel(self, x0, y0):
	_cmd_buff[0] = LEADING_FRAME

	_cmd_buff[1] = 0x00
	_cmd_buff[2] = 0x0D

	_cmd_buff[3] = CMD_DRAW_PIXEL

	_cmd_buff[4] = (x0 >> 8) & 0xFF
	_cmd_buff[5] = x0 & 0xFF
	_cmd_buff[6] = (y0 >> 8) & 0xFF
	_cmd_buff[7] = y0 & 0xFF

	_cmd_buff[8] = FRAME_E0
	_cmd_buff[9] = FRAME_E1
	_cmd_buff[10] = FRAME_E2
	_cmd_buff[11] = FRAME_E3
	_cmd_buff[12] = _verify(_cmd_buff, 12)

	_putchars(_cmd_buff, 13)

'''******************************************************************************
* Function Name  : void eink_draw_line(int x0, y0, x1, y1)
* Description    :
* Input          :
* Output         : None
* Return         :
* Attention		   : None
******************************************************************************'''
def eink_draw_line(self, x0, y0, x1, y1):
	_cmd_buff[0] = LEADING_FRAME

	_cmd_buff[1] = 0x00
	_cmd_buff[2] = 0x11

	_cmd_buff[3] = CMD_DRAW_LINE

	_cmd_buff[4] = (x0 >> 8) & 0xFF
	_cmd_buff[5] = x0 & 0xFF
	_cmd_buff[6] = (y0 >> 8) & 0xFF
	_cmd_buff[7] = y0 & 0xFF
	_cmd_buff[8] = (x1 >> 8) & 0xFF
	_cmd_buff[9] = x1 & 0xFF
	_cmd_buff[10] = (y1 >> 8) & 0xFF
	_cmd_buff[11] = y1 & 0xFF

	_cmd_buff[12] = FRAME_E0
	_cmd_buff[13] = FRAME_E1
	_cmd_buff[14] = FRAME_E2
	_cmd_buff[15] = FRAME_E3
	_cmd_buff[16] = _verify(_cmd_buff, 16)

	_putchars(_cmd_buff, 17)

'''******************************************************************************
* Function Name  : void eink_fill_rect(int x0, y0, x1, y1)
* Description    :
* Input          :
* Output         : None
* Return         :
* Attention		   : None
******************************************************************************'''
def eink_fill_rect(self, x0, y0, x1, y1):
	_cmd_buff[0] = LEADING_FRAME

	_cmd_buff[1] = 0x00
	_cmd_buff[2] = 0x11

	_cmd_buff[3] = CMD_FILL_RECT

	_cmd_buff[4] = (x0 >> 8) & 0xFF
	_cmd_buff[5] = x0 & 0xFF
	_cmd_buff[6] = (y0 >> 8) & 0xFF
	_cmd_buff[7] = y0 & 0xFF
	_cmd_buff[8] = (x1 >> 8) & 0xFF
	_cmd_buff[9] = x1 & 0xFF
	_cmd_buff[10] = (y1 >> 8) & 0xFF
	_cmd_buff[11] = y1 & 0xFF

	_cmd_buff[12] = FRAME_E0
	_cmd_buff[13] = FRAME_E1
	_cmd_buff[14] = FRAME_E2
	_cmd_buff[15] = FRAME_E3
	_cmd_buff[16] = _verify(_cmd_buff, 16)

	_putchars(_cmd_buff, 17)

'''******************************************************************************
* Function Name  : void eink_draw_circle(int x0, y0, r)
* Description    :
* Input          :
* Output         : None
* Return         :
* Attention		   : None
******************************************************************************'''
def eink_draw_circle(self, x0, y0, r):
	_cmd_buff[0] = LEADING_FRAME

	_cmd_buff[1] = 0x00
	_cmd_buff[2] = 0x0F

	_cmd_buff[3] = CMD_DRAW_CIRCLE

	_cmd_buff[4] = (x0 >> 8) & 0xFF
	_cmd_buff[5] = x0 & 0xFF
	_cmd_buff[6] = (y0 >> 8) & 0xFF
	_cmd_buff[7] = y0 & 0xFF
	_cmd_buff[8] = (r >> 8) & 0xFF
	_cmd_buff[9] = r & 0xFF


	_cmd_buff[10] = FRAME_E0
	_cmd_buff[11] = FRAME_E1
	_cmd_buff[12] = FRAME_E2
	_cmd_buff[13] = FRAME_E3
	_cmd_buff[14] = _verify(_cmd_buff, 14)

	_putchars(_cmd_buff, 15)

'''******************************************************************************
* Function Name  : void eink_fill_circle(int x0, y0, r)
* Description    :
* Input          :
* Output         : None
* Return         :
* Attention		   : None
******************************************************************************'''
def eink_fill_circle(self, x0, y0, r):
	_cmd_buff[0] = LEADING_FRAME

	_cmd_buff[1] = 0x00
	_cmd_buff[2] = 0x0F

	_cmd_buff[3] = CMD_FILL_CIRCLE

	_cmd_buff[4] = (x0 >> 8) & 0xFF
	_cmd_buff[5] = x0 & 0xFF
	_cmd_buff[6] = (y0 >> 8) & 0xFF
	_cmd_buff[7] = y0 & 0xFF
	_cmd_buff[8] = (r >> 8) & 0xFF
	_cmd_buff[9] = r & 0xFF


	_cmd_buff[10] = FRAME_E0
	_cmd_buff[11] = FRAME_E1
	_cmd_buff[12] = FRAME_E2
	_cmd_buff[13] = FRAME_E3
	_cmd_buff[14] = _verify(_cmd_buff, 14)

	_putchars(_cmd_buff, 15)

'''******************************************************************************
* Function Name  : void eink_draw_triangle(int x0, y0, x1, y1, x2, y2)
* Description    :
* Input          :
* Output         : None
* Return         :
* Attention		   : None
******************************************************************************'''
def eink_draw_triangle(self, x0, y0, x1, y1, x2, y2):
	_cmd_buff[0] = LEADING_FRAME

	_cmd_buff[1] = 0x00
	_cmd_buff[2] = 0x15

	_cmd_buff[3] = CMD_DRAW_TRIANGLE

	_cmd_buff[4] = (x0 >> 8) & 0xFF
	_cmd_buff[5] = x0 & 0xFF
	_cmd_buff[6] = (y0 >> 8) & 0xFF
	_cmd_buff[7] = y0 & 0xFF
	_cmd_buff[8] = (x1 >> 8) & 0xFF
	_cmd_buff[9] = x1 & 0xFF
	_cmd_buff[10] = (y1 >> 8) & 0xFF
	_cmd_buff[11] = y1 & 0xFF
	_cmd_buff[12] = (x2 >> 8) & 0xFF
	_cmd_buff[13] = x2 & 0xFF
	_cmd_buff[14] = (y2 >> 8) & 0xFF
	_cmd_buff[15] = y2 & 0xFF

	_cmd_buff[16] = FRAME_E0
	_cmd_buff[17] = FRAME_E1
	_cmd_buff[18] = FRAME_E2
	_cmd_buff[19] = FRAME_E3
	_cmd_buff[20] = _verify(_cmd_buff, 20)

	_putchars(_cmd_buff, 21)

'''******************************************************************************
* Function Name  : void eink_fill_triangle(int x0, y0, x1, y1, x2, y2)
* Description    :
* Input          :
* Output         : None
* Return         :
* Attention		   : None
******************************************************************************'''
def eink_fill_triangle(self, x0, y0, x1, y1, x2, y2):
	_cmd_buff[0] = LEADING_FRAME

	_cmd_buff[1] = 0x00
	_cmd_buff[2] = 0x15

	_cmd_buff[3] = CMD_FILL_TRIANGLE

	_cmd_buff[4] = (x0 >> 8) & 0xFF
	_cmd_buff[5] = x0 & 0xFF
	_cmd_buff[6] = (y0 >> 8) & 0xFF
	_cmd_buff[7] = y0 & 0xFF
	_cmd_buff[8] = (x1 >> 8) & 0xFF
	_cmd_buff[9] = x1 & 0xFF
	_cmd_buff[10] = (y1 >> 8) & 0xFF
	_cmd_buff[11] = y1 & 0xFF
	_cmd_buff[12] = (x2 >> 8) & 0xFF
	_cmd_buff[13] = x2 & 0xFF
	_cmd_buff[14] = (y2 >> 8) & 0xFF
	_cmd_buff[15] = y2 & 0xFF

	_cmd_buff[16] = FRAME_E0
	_cmd_buff[17] = FRAME_E1
	_cmd_buff[18] = FRAME_E2
	_cmd_buff[19] = FRAME_E3
	_cmd_buff[20] = _verify(_cmd_buff, 20)

	_putchars(_cmd_buff, 21)

'''******************************************************************************
* Function Name  : void eink_clear(void)
* Description    :
* Input          :
* Output         : None
* Return         :
* Attention		   : None
******************************************************************************'''
def eink_clear(self, void):
	_cmd_buff[0] = LEADING_FRAME
	_cmd_buff[1] = 0x00
	_cmd_buff[2] = 0x09
	_cmd_buff[3] = CMD_CLEAR
	_cmd_buff[4] = FRAME_E0
	_cmd_buff[5] = FRAME_E1
	_cmd_buff[6] = FRAME_E2
	_cmd_buff[7] = FRAME_E3
	_cmd_buff[8] = _verify(_cmd_buff, 8)
	_putchars(_cmd_buff, 9)


'''******************************************************************************
* Function Name  : void eink_disp_char(unsigned char ch, x0, y0)
* Description    :
* Input          :
* Output         : None
* Return         :
* Attention		   : None
******************************************************************************'''
def eink_disp_char(self, char ch, x0, y0):
	unsigned char buff[2]

	buff[0] = ch
	buff[1] = 0

	eink_disp_string(buff, x0, y0)

def eink_disp_string(self, * p, x0, y0):
	int string_size
	unsigned char ptr = (unsigned char *)p
	string_size = strlen(( char *)ptr)
	string_size += 14

	_cmd_buff[0] = LEADING_FRAME

	_cmd_buff[1] = (string_size >> 8) & 0xFF
	_cmd_buff[2] = string_size & 0xFF

	_cmd_buff[3] = CMD_DRAW_STRING

	_cmd_buff[4] = (x0 >> 8) & 0xFF
	_cmd_buff[5] = x0 & 0xFF
	_cmd_buff[6] = (y0 >> 8) & 0xFF
	_cmd_buff[7] = y0 & 0xFF

	strcpy((char *)(&_cmd_buff[8]), ( char *)ptr)

	string_size -= 5

	_cmd_buff[string_size] = FRAME_E0
	_cmd_buff[string_size + 1] = FRAME_E1
	_cmd_buff[string_size + 2] = FRAME_E2
	_cmd_buff[string_size + 3] = FRAME_E3
	_cmd_buff[string_size + 4] = _verify(_cmd_buff, string_size + 4)

	_putchars(_cmd_buff, string_size + 5)

def eink_disp_bitmap(self, * p, x0, y0):
	int string_size
	unsigned char ptr = (unsigned char *)p

	string_size = strlen(( char *)ptr)
	string_size += 14

	_cmd_buff[0] = LEADING_FRAME

	_cmd_buff[1] = (string_size >> 8) & 0xFF
	_cmd_buff[2] = string_size & 0xFF

	_cmd_buff[3] = CMD_DRAW_BITMAP

	_cmd_buff[4] = (x0 >> 8) & 0xFF
	_cmd_buff[5] = x0 & 0xFF
	_cmd_buff[6] = (y0 >> 8) & 0xFF
	_cmd_buff[7] = y0 & 0xFF

	strcpy((char *)(&_cmd_buff[8]), ( char *)ptr)

	string_size -= 5

	_cmd_buff[string_size] = FRAME_E0
	_cmd_buff[string_size + 1] = FRAME_E1
	_cmd_buff[string_size + 2] = FRAME_E2
	_cmd_buff[string_size + 3] = FRAME_E3
	_cmd_buff[string_size + 4] = _verify(_cmd_buff, string_size + 4)

	_putchars(_cmd_buff, string_size + 5)
