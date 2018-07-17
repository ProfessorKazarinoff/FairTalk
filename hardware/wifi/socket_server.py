## from lab.whitequark.org
## url: https://lab.whitequark.org/notes/2016-10-20/controlling-a-gpio-through-an-esp8266-based-web-server/


## To add serial RX and TX writing to the LoRa in Circuit Python use bitbangio library from Adafruit
# http://circuitpython.readthedocs.io/en/latest/shared-bindings/bitbangio/I2C.html

from ENV import SSID, PWD

# Begin configuration
TITLE = "Air conditioner"
GPIO_NUM = 0
STA_SSID = SSID
STA_PSK = PWD
# End configuration

import network
import machine
import socket


def ok(socket, query):
    socket.write("HTTP/1.1 OK\r\n\r\n")
    socket.write("<!DOCTYPE html><title>" + TITLE + "</title><body>")
    socket.write(TITLE + " status: ")
    if pin.value():
        socket.write("<span style='color:green'>ON</span>")
    else:
        socket.write("<span style='color:red'>OFF</span>")
    socket.write("<br>")
    if pin.value():
        socket.write("<form method='POST' action='/off?" + query.decode() + "'>" +
                     "<input type='submit' value='turn OFF'>" +
                     "</form>")
    else:
        socket.write("<form method='POST' action='/on?" + query.decode() + "'>" +
                     "<input type='submit' value='turn ON'>" +
                     "</form>")


def err(socket, code, message):
    socket.write("HTTP/1.1 " + code + " " + message + "\r\n\r\n")
    socket.write("<h1>" + message + "</h1>")


def handle(socket):
    (method, url, version) = socket.readline().split(b" ")
    if b"?" in url:
        (path, query) = url.split(b"?", 2)
    else:
        (path, query) = (url, b"")
    while True:
        header = socket.readline()
        if header == b"":
            return
        if header == b"\r\n":
            break

    if version != b"HTTP/1.0\r\n" and version != b"HTTP/1.1\r\n":
        err(socket, "505", "Version Not Supported")
    elif method == b"GET":
        if path == b"/":
            ok(socket, query)
        else:
            err(socket, "404", "Not Found")
    elif method == b"POST":
        if path == b"/on":
            pin.high()
            ok(socket, query)
        elif path == b"/off":
            pin.low()
            ok(socket, query)
        else:
            err(socket, "404", "Not Found")
    else:
        err(socket, "501", "Not Implemented")


def main():
    from ENV import SSID, PWD
    STA_SSID = SSID
    STA_PSK = PWD
    ap_if = network.WLAN(network.AP_IF)
    if ap_if.active(): ap_if.active(False)
    sta_if = network.WLAN(network.STA_IF)
    if not ap_if.active(): sta_if.active(True)
    if not sta_if.isconnected(): sta_if.connect(STA_SSID, STA_PSK)



    import machine
    pins = [machine.Pin(i, machine.Pin.IN) for i in (0, 2, 4, 5, 12, 13, 14, 15)]

    html = """<!DOCTYPE html>
    <html>
        <head> <title>ESP8266 Pins</title> </head>
        <body> <h1>ESP8266 Pins</h1>
            <table border="1"> <tr><th>Pin</th><th>Value</th></tr> %s </table>
        </body>
    </html>
    """

    import socket
    addr = socket.getaddrinfo('0.0.0.0', 5000)[0][-1]

    s = socket.socket()
    s.bind(addr)
    s.listen(1)

    print('listening on', addr)

    while True:
        cl, addr = s.accept()
        print('client connected from', addr)
        cl_file = cl.makefile('rwb', 0)
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
        rows = ['<tr><td>%s</td><td>%d</td></tr>' % (str(p), p.value()) for p in pins]
        response = html % '\n'.join(rows)
        cl.send(response)
        cl.close()


if __name__ == "__main__":
    main()