import board
import digitalio
import time


# Setup the LED pin to be output
led = digitalio.DigitalInOut(board.D13)
led.switch_to_output()


while True:
    # Turn the LED on and off each 0.5 s
    led.value = not led.value
    time.sleep(0.5)
