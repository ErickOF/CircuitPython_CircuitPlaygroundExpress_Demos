import time

from adafruit_circuitplayground.express import cpx


# Configure the pixel brightness
cpx.pixels.brightness = 0.25
# Configure the movement, color and what is the first pixel
direction = 1
color = (0, 0, 255)
pixel = 0

while True:
    # Clear all the pixels
    cpx.pixels.fill(0)

    # Select the current pixel color
    cpx.pixels[pixel] = color

    if cpx.button_a:
        direction = 1
    elif cpx.button_b:
        direction = -1

    pixel += direction
    pixel = 0 if (pixel > 9) else 9 if (pixel < 0) else pixel

    time.sleep(0.5)
