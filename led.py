import time
from mraa import getGpioLookup
from grove.grove_ryb_led_button import GroveLedButton
from grove.button import Button

READ_TIMEOUT = 5
SLOT = 5 # digital

def main():
    button = GroveLedButton(SLOT)
    button.led.light(False)

    def on_event(index, event, tm):
        if event & Button.EV_SINGLE_CLICK:
            button.led.light(True)
            print('sc', event, index, tm)
        elif event & Button.EV_DOUBLE_CLICK:
            button.led.blink(True)
            print('dc', event, index, tm)
        elif event & Button.EV_LONG_PRESS:
            button.led.light(False)
            print('lc', event, index, tm)

    button.on_event = on_event

    while True:
        time.sleep(1)


if __name__ == '__main__':
    main()
