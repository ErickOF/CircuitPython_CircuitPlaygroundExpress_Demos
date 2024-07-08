import time

from adafruit_circuitplayground.express import cpx


def read_temperature(samples):
    """Read the temperature n number of sample and get the average

    Args:
        samples (int): number of samples

    Returns:
        float: average of the temperature
    """
    return sum(cpx.temperature for _ in range(samples)) / samples

# Pick up couple of colours to represent the temperature change
room_color = (0, 0, 255)
warm_color = (255, 0, 0)

# Measure the room temperature as a base
room_temperature = read_temperature(200)

# Configure pixel brightness
cpx.pixels.brightness = 0.05
# Avoid pixels to change before they are written
cpx.pixels.auto_write = False

# First pixel
pixel = 9
# Current color
color = room_color

while True:
    # Show the delta in the temperature
    temperature = read_temperature(10)
    color = room_color if (temperature - room_temperature) < 0.5 else warm_color

    # Clean and set the right colour
    cpx.pixels.fill(0)
    cpx.pixels[pixel] = color
    cpx.pixels.show()

    # Next pixel or restart if it is necessary
    pixel = pixel - 1 if pixel > 0 else 9

    # Wait some time
    time.sleep(0.05)
