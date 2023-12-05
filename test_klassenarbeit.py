"""
Datei: test_klassenarbeit
Autor: Christian V.
Datum: 05.12.23

Die Programm ist eine realisierung der Übung für die Klassenarbeit.
Mit betätigung des Tasters wir das Programm aktiv und misst die Luffeuchtigkeit und Temperatur und gibt diese auf dem Display aus.
Solange alles OK ist soll eine grüne LED leuchten, beim Überschreiten des Schwellwertes fängt eine rote LED an zu blinken.

Rote LED mit 220 Ohm Vorwiderstand an Pin42.
Grüne LED mit 220 Ohm Vorwiderstand an Pin1.
Taster(Pull UP) mit 10k Widerstand an Pin40.

Sensor SDA Pin15, SCL Pin16

Display SDA Pin11, SCL Pin13
ST7789_rst      Pin5
ST7789_dc       Pin4
SCL             Pin13
SDA             Pin11


Bibliotheken: "utime" für Zeitbefehl, "Pin und SoftI2C" für I2C kommunikation und Pin Deklaration, "ahtx0" für den aht10 Sensor.
    
"""

#-------------------------------------Bibliotheken------------------------------------------------------------------------------------------

import ahtx0                                                                    #Einbindung Sensor Bibliothek
from machine import Pin, SoftI2C

import uos                                                                      #Einbindung Display Bibliothek
import machine
import st7789py as st7789
from fonts import vga1_16x32 as font
import random
import ustruct as struct
import utime

#-------------------------------------LEDs--------------------------------------------------------------------------------------------------
led_rot = Pin(42, Pin.OUT)
led_gruen = Pin(1, Pin.OUT)

#-------------------------------------Sensor------------------------------------------------------------------------------------------------

i2c = SoftI2C(scl=Pin(16), sda=Pin(15))                                           #Anlegen einer Variable zur Benennung der I2C Leitungen
sensor = ahtx0.AHT10(i2c)                                                         #Anlegen einer Variable für den Sensorwert

temp = 0
hum = 0
temp_grenz = 25
hum_grenz = 50
#-------------------------------------Display----------------------------------------------------------------------------------------------

st7789_res = 5
st7789_dc  = 4
pin_st7789_res = machine.Pin(st7789_res, machine.Pin.OUT)
pin_st7789_dc = machine.Pin(st7789_dc, machine.Pin.OUT)

disp_width = 240
disp_height = 280
CENTER_Y = int(disp_width/2)
CENTER_X = int(disp_height/2)

print(uos.uname())
#spi2 = machine.SPI(2, baudrate=40000000, polarity=1)
pin_spi2_sck = machine.Pin(13, machine.Pin.OUT)
pin_spi2_mosi = machine.Pin(11, machine.Pin.OUT)
pin_spi2_miso = machine.Pin(19, machine.Pin.IN)
spi2 = machine.SPI(2, sck=pin_spi2_sck, mosi=pin_spi2_mosi, miso=pin_spi2_miso,
                   baudrate=40000000, polarity=1)
print(spi2)
display = st7789.ST7789(spi2, disp_width, disp_width,
                          reset=pin_st7789_res,
                          dc=pin_st7789_dc,
                          xstart=0, ystart=0, rotation=45)

#-------------------------------------Hauptteil--------------------------------------------------------------------------------------------
while True:
#-------------------------------------Schalter---------------------------------------------------------------------------------------------
    taster = Pin(40,Pin.IN)
    schalter = False
    
    if taster.value() == True and schalter == False:
        schalter = True
        sleep(0.5)
    else:
        schalter = False
        sleep(0.05)


#------------------------------------Hauptprogramm-----------------------------------------------------------------------------------------

    while schalter == True:
        if taster.value() == True and schalter == True:
            schalter = False
            display.fill(st7789.BLACK)
            led_gruen.off()
            led_rot.off()
            break
        
        else:
            sleep(0.05)
        
        temp = int(sensor.temperature)
        hum = int(sensor.relative_humidity)

        if temp >= temp_grenz or hum >= hum_grenz:
            display.fill(st7789.BLACK)
            display.text(font, "Temperatur", 10, 10)
            display.text(font, "\nTemperature: %0.0f C" % temp, 10, 40)
            display.text(font, "Luftfeuchte", 10, 70)
            display.text(font, "\nFeuchtigkeit: %0.0f %" % hum, 10, 100)
            led_rot.on()
            sleep(0.5)
            led_rot.off()
            sleep(0.5)
            led_rot.on()
            sleep(0.5)
            led_rot.off()
            sleep(0.5)
            led_rot.on()
            sleep(0.5)
            led_rot.off()
            sleep(0.5)
            led_rot.on()
            sleep(0.5)
            led_rot.off()
            sleep(0.5)
            led_rot.on()
            sleep(0.5)
            led_rot.off()
        else:
            display.fill(st7789.BLACK)
            display.text(font, "Temperatur", 10, 10)
            display.text(font, "\nTemperature: %0.0f C" % temp, 10, 40)
            display.text(font, "Luftfeuchte", 10, 70)
            display.text(font, "\nFeuchtigkeit: %0.0f %" % hum, 10, 100)
            led_gruen.on() 