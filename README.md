# esp8266

## hw

- esp8266 MOD AI TINKER
https://www.esp8266.com/wiki/doku.php?id=esp8266-module-family


## sw

### esptool

- esptool use without sudo - add yourself to tty group
https://github.com/esp8266/source-code-examples/issues/26
```bash
groups  # your groups
compgen -G  # available groups
sudo usermod -a -G tty dialout $USER  # add yourself to groups tty and dialout (ubuntu)
# (optional) kill all tmux sessions
# logout from whole desktop session
# login
groups  # should contain tty and dialout
```
steps
http://docs.micropython.org/en/latest/esp8266/tutorial/intro.html#deploying-the-firmware

firmware
https://cuneyt.aliustaoglu.biz/en/installing-micropython-for-esp8266/
