import time
import usb_hid
from adafruit_hid.mouse import Mouse
import board
import digitalio

mouse = Mouse(usb_hid.devices)

led = digitalio.DigitalInOut(board.GP25)
led.direction = digitalio.Direction.OUTPUT

led.value = False
time.sleep(2)

while True:
	led.value = True
	mouse.move(x=1)
	time.sleep(20)
	mouse.move(x=-1)
	time.sleep(20)