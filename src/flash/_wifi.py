import network
import utime

def wifi_connect(essid, password):
    # Connect to the wifi. Based on the example in the micropython
    # documentation.
    wlan = network.WLAN(network.STA_IF) 

    while not wlan.isconnected():
#	wlan.disconnect()
        print('waiting for connection...')
	wlan.active(True)
	wlan.connect(essid, password)
        utime.sleep(4)
        print('checking connection...')
        print('Wifi connect successful, network config: %s' % repr(wlan.ifconfig()))

    print('testing...')
    import urequests
    r = urequests.get('http://ip-api.com/json').json()
    print(r)

def do_connect(essid, password):
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(essid, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
