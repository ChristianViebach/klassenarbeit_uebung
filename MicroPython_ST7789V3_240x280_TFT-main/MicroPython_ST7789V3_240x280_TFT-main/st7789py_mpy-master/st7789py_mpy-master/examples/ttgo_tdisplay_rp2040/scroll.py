"""
scroll.py

    Smoothly scrolls all font characters up the screen on the LILYGO® TTGO
    T-Display. Only works with fonts with heights that are even multiples of
    the screen height, (i.e. 8 or 16 pixels high)

"""
import utime
import random
from machine import Pin, SoftSPI
import st7789py as st7789

# choose a font

# from romfonts import vga1_8x8 as font
# from romfonts import vga2_8x8 as font
# from romfonts import vga1_8x16 as font
# from romfonts import vga2_8x16 as font
# from romfonts import vga1_16x16 as font
# from romfonts import vga1_bold_16x16 as font
# from romfonts import vga2_16x16 as font
from romfonts import vga2_bold_16x16 as font


def main():
    Pin(22, Pin.OUT, value=1)

    spi = SoftSPI(
        baudrate=20000000,
        polarity=1,
        phase=0,
        sck=Pin(2),
        mosi=Pin(3),
        miso=Pin(13))

    tft = st7789.ST7789(
        spi,
        135,
        240,
        reset=Pin(0, Pin.OUT),
        cs=Pin(5, Pin.OUT),
        dc=Pin(1, Pin.OUT),
        backlight=Pin(4, Pin.OUT),
        rotation=0)

    last_line = tft.height - font.HEIGHT
    tfa = 40
    tfb = 40
    tft.vscrdef(tfa, 240, tfb)

    tft.fill(st7789.BLUE)
    scroll = 0
    character = 0
    while True:
        tft.fill_rect(0, scroll, tft.width, 1, st7789.BLUE)

        if scroll % font.HEIGHT == 0:
            tft.text(
                font,
                '\\x{:02x}= {:s} '.format(character, chr(character)),
                0,
                (scroll + last_line) % tft.height,
                st7789.WHITE,
                st7789.BLUE)

            character = character + 1 if character < 256 else 0

        tft.vscsad(scroll + tfa)
        scroll += 1

        if scroll == tft.height:
            scroll = 0

        utime.sleep(0.01)


main()
