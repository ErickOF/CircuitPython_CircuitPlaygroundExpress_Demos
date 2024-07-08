import time

from adafruit_circuitplayground.express import cpx

cpx.pixels.brightness = 0.05
cpx.pixels.auto_write = False

def rainbow(pos):
    """Get the color of each pixel to generate a rainbow

    Args:
        pos (float): current pixel position by 255 / TOTAL_PIXELS

    Returns:
        Tuple[int, int, int]: color of the current pixel
    """
    edge = pos // 85
    pos = (pos % 85) * 3

    if edge == 0:
        return (255 - pos, pos, 0)
    elif edge == 1:
        return (0, 255 - pos, pos)
    else:
        return (pos, 0, 255 - pos)

TOTAL_PIXELS = 10

# Define the 10 colors for the rainbow
colors = [rainbow((255 / TOTAL_PIXELS) * i) for i in range(TOTAL_PIXELS)]
# First color
position = 0

while True:
    # Set the color of each pixel
    for i in range(TOTAL_PIXELS):
        cpx.pixels[i] = colors[(i + position) % TOTAL_PIXELS]

    cpx.pixels.show()

    # Next position
    position = (position + 1) % TOTAL_PIXELS

    # Wait 40ms
    time.sleep(0.04)
