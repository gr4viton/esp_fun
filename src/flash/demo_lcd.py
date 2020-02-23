import time
import machine
from .esp8266_i2c_lcd import I2cLcd

i2c = machine.I2C(-1, machine.Pin(5), machine.Pin(4), freq=400000)
lcd = I2cLcd(i2c, 63, 2, 16)
lcd.clear()
ls = ['Eat', 'Sleep', 'Rave', 'Repeat']

i = 1
while True:
    if i % 2:
        index = int(i / 2) % 4
        txt = ls[index]

        lcd.putstr(txt)
        lcd.backlight_on()
        period = 0.5
    else:
        txt = ""
        lcd.clear()
        lcd.backlight_off()
        period = 0.2

    print(i, txt)
    time.sleep(period)
    i += 1
