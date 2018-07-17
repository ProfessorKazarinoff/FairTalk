# Fair Talk Booster WiFi Component

## Load Micropython onto ESP8266

## Test Micropython REPL

on Linux:

```
$ screen /dev/ttyUSB0 115200
#[ENTER or ctrl-D]

>>>import sys
>>> sys.version
'3.4.0'
>>> sys.implementation
(name='micropython', version=(1, 9, 4))
>>> sys.platform
'esp8266'
>>> import machine
>>> pin = machine.Pin(0, machine.Pin.OUT)
# LED ON
>>> pin.value(1)
# LED OFF
>>> pin.off()
>>> # LED ON
>>> pin.on()
>>> # LED OFF
```

## Upload .py file onto ESP8266

```
# activate virtual environment
$ conda activate fairtalk

# if virtual environment does not exhist run $ conda create -n fairtalk python=3.7
$ pip install ampy
$ ampy --help

# view .py files on the board
$ ampy -p /dev/ttyUSB0 ls

# upload the main.py file onto the board
$ ampy -p /dev/ttyUSB0 put main.py

# see if the file was uploaded
$ ampy -p /dev/ttyUSB0 ls
boot.py
main.py

# upload main.py, run.py and set_led_http_server.py onto the board
$ ampy -p /dev/ttyUSB0 put main.py
$ ampy -p /dev/ttyUSB0 put run.py
$ ampy -p /dev/ttyUSB0 put set_led_http_server.py
$ ampy -p /dev/ttyUSB0 ls
boot.py
main.py
run.py
set_led_http_server.py
```

Unplug ESP8266 and replug back in. Navigate browser to:

> http://192.168.4.1/


