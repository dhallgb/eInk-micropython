#!/usr/bin/env python
from eink import *
from time import sleep

def base_draw():

    eink_clear()
    for j in range(0, 600, 50):
        for i in range (0, 800, 50):
            eink_draw_pixel(i, j)
            eink_draw_pixel(i, j + 1)
            eink_draw_pixel(i + 1, j)
            eink_draw_pixel(i + 1, j + 1)
    eink_update()
    sleep(3)

    eink_clear()
    for i in range(0, 800, 100):
        eink_draw_line(0, 0, i, 599)
        eink_draw_line(799, 0, i, 599)
    eink_update()
    sleep(3)

    eink_clear()
    eink_set_color(BLACK, WHITE)
    eink_fill_rect(10, 10, 100, 100)
    eink_set_color(DARK_GRAY, WHITE)
    eink_fill_rect(110, 10, 200, 100)
    eink_set_color(GRAY, WHITE)
    eink_fill_rect(210, 10, 300, 100)
    eink_update()
    sleep(3)
    
    eink_set_color(BLACK, WHITE)
    eink_clear()
    
    for i in range(0, 300, 40):
        eink_draw_circle(399, 299, i)
    eink_update()
    sleep(3)
    
    eink_clear()
    for j in range(0, 6):
        for i in range(0, 8):
            eink_fill_circle(50 + i * 100, 50 + j * 100, 50)
    eink_update()
    sleep(3)
    
    eink_clear()
    for i in range(1, 5):
        eink_draw_triangle(399, 249 - i * 50, 349 - i * 50, 349 + i * 50, 449 + i * 50, 349 + i * 50)
    eink_update()
    sleep(3)

def draw_text_demo():
   buff = bytearray('G', 'B', 'K', '3', '2', ':', ' ', 0xc4, 0xe3, 0xba, 0xc3, 0xca, 0xc0, 0xbd, 0xe7, 0)
   eink_set_color(BLACK, WHITE)
   eink_clear()
   eink_set_ch_font(GBK32)
   eink_set_en_font(ASCII32)
   eink_disp_string(buff, 0, 50)
   eink_disp_string("ASCII32: Hello, World! ", 0, 300)
   eink_set_ch_font(GBK48)
   eink_set_en_font(ASCII48)
   buff[3] = '4'
   buff[4] = '8'
   eink_disp_string(buff, 0, 100)
   eink_disp_string("ASCII48: Hello, World! ", 0, 350)
   eink_set_ch_font(GBK64)
   eink_set_en_font(ASCII64)
   buff[3] = '6'
   buff[4] = '4'
   eink_disp_string(buff, 0, 160)
   eink_disp_string("ASCII64: Hello, World! ", 0, 450)
   eink_update()
   sleep(3)

def draw_bitmap_demo():
    eink_clear()
    eink_disp_bitmap("PIC4.BMP", 0, 0)
    eink_update()
    sleep(3)

    eink_clear()
    eink_disp_bitmap("PIC2.BMP", 0, 100)
    eink_disp_bitmap("PIC3.BMP", 400, 100)
    eink_update()
    sleep(3)

    eink_clear()
    eink_disp_bitmap("PIC7.BMP", 0, 0)
    eink_update()

eink_init()
base_draw()
#  draw_text_demo()
#  draw_bitmap_demo()
