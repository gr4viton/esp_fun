# import machine
import time
from flash.demo_led import demo_led
from flash.demo_socket import demo_socket
from flash.demo_servo import demo_servo
from flash.peripherals import led_blue as led


def wifi_setup(pwd):
    print("wifi_setup")
    import network
    ap = network.WLAN(network.AP_IF)
    ssid = ap.config('essid')
    print(ssid)
    ap.active()
    ap.active(True)
    ap.config(essid="esp8", authmode=network.AUTH_WPA_WPA2_PSK, password=pwd)


def demo_lcd():
    print("demo_lcd")
    import flash.demo_lcd  # noqa


def demo_led_on_wifi_active():
    print("demo_led_on_wifi_active")
    import network
    ap = network.WLAN(network.AP_IF)

    led.off()
    time.sleep(1)
    wifi_on = ap.active()
    led.value(wifi_on)

    print("wifi_on", wifi_on)
    time.sleep(60)


def main():

    demo_servo()
    # demo_led_on_wifi_active()
    demo_led(5, 1)
    # demo_led(10)
