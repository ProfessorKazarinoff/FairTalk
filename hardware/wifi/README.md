# Fair Talk Booster WiFi Component

## Load Micropython onto ESP8266

## Test Micropython REPL, turn on/off ESP8266 LED

on Linux:

```
$ screen /dev/ttyUSB0 115200
#[ENTER or ctrl-d or ctrl-c]

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

# upload main.py, run.py and simple_server.py onto the board
$ ampy -p /dev/ttyUSB0 put main.py
$ ampy -p /dev/ttyUSB0 put run.py
$ ampy -p /dev/ttyUSB0 put wifitools.py
$ ampy -p /dev/ttyUSB0 put ENV.py
$ ampy -p /dev/ttyUSB0 put simple_server.py
$ ampy -p /dev/ttyUSB0 ls
boot.py
ENV.py
main.py
run.py
simple_server.py
wifitools.py
```

Unplug ESP8266 and replug back in. Navigate browser to:

> the IP address of the ESP8266

the above still needs work

