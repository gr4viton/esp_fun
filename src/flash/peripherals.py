from machine import Pin, Signal

_led_pin = Pin(2, Pin.OUT)  # blue - has inverted
led_blue = Signal(_led_pin, invert=True)

# probly usb UART!  # do not ever do this
# led = machine.Pin(5, machine.Pin.OUT)

# 14   //D5 is GPIO14
pwm_d5 = Pin(14)
