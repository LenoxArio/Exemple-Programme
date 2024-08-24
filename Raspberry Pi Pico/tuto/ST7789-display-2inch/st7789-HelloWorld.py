"""
Raspberry Pi Pico/MicroPython exercise
240x240 ST7789 SPI LCD
using MicroPython library:
https://github.com/russhughes/st7789py_mpy

broche:
DC=8
CS=9
CLK=10
DIN=11
RST=12
BL=13

"""

import uos
import machine
import st7789py as st7789
import vga1_16x32 as font2
import time

# SPI(1) default pins
spi1_sck = 10    # CLK
spi1_mosi = 11   # DIN
spi1_miso = 8    # not used
spi1_cs = 9      # CS
st7789_res = 12  # RST
st7789_dc = 8    # DC
disp_width = 240
disp_height = 320

spi1 = machine.SPI(1, baudrate=40000000, polarity=1)
display = st7789.ST7789(spi1, disp_width, disp_height,
                        reset=machine.Pin(st7789_res, machine.Pin.OUT),
                        dc=machine.Pin(st7789_dc, machine.Pin.OUT),
                        cs=machine.Pin(spi1_cs, machine.Pin.OUT))

# Clear the screen
display.fill(st7789.BLACK)


while True:
    display.text(font2, "Hello World", 16, 16, color=st7789.color565(255, 255, 0))
    time.sleep(1)
    display.text(font2, "Hello World", 16, 16, color=st7789.color565(255, 0, 0))
    time.sleep(1)



