# denotes scripts and functions to run
# run.py is called by main.py after boot.py runs

import set_led_http_server.py

def main():
    set_led_http_server.main()

if __name__ == "__main__":
    main()
