import time

from flash.peripherals import led_blue as led


def demo_led(off_seconds=5, on_seconds=1):
    print("demo_led")

    while True:
        led.off()
        time.sleep(off_seconds)
        led.on()
        time.sleep(on_seconds)
