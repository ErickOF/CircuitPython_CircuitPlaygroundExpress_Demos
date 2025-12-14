import random
import time

from adafruit_circuitplayground.express import cpx


def f(n):
    """Frequency of the nth note

    Args:
        n (int): 

    Returns:
        float: 
    """
    return pow(pow(2, 1 / 12), n - 49) * 440

cpx.pixels.brightness = 0.05
pixel = 0
note = 0
tempo = 128


def decompose_note(note_info):
    notes_duration = {
        'w': 4 * 60 / tempo,
        'h': 2 * 60 / tempo,
        'q': 60 / tempo,
        'e': 0.5 * 60 / tempo,
        't': (1 / 3) * 60 / tempo,
        's': 0.25 * 60 / tempo,
    }

    scale_notes = {
        'A': 1,
        'A#': 2,
        'Bb': 3,
        'B': 3,
        'C': 4,
        'C#': 5,
        'Db': 5,
        'D': 6,
        'D#': 7,
        'E': 8,
        'F': 9,
        'F#': 10,
        'G': 11,
        'G#': 12,
    }

    note_value = ''
    duration = ''

    if 's' in note_info:
        note_value = -1
        duration = notes_duration[note_info[1]]
    elif 'b' in note_info or '#' in note_info:
        note_value = scale_notes[note_info[0:2]] + 12 * int(note_info[2])
        duration = notes_duration[note_info[3]]
    else:
        note_value = scale_notes[note_info[0]] + 12 * int(note_info[1])
        duration = notes_duration[note_info[2]]

    return note_value, duration

# Little Star
#song = [
#    'G5e', 'G5e', 'G6e', 'G6e', 'A6e', 'A6e', 'G6q',
#    'F6e', 'F6e', 'E6e', 'E6e', 'D6e', 'D6e', 'C6q',
#    'G6e', 'G6e', 'F6e', 'F6e', 'E6e', 'E6e', 'D6q',
#    'G6e', 'G6e', 'F6e', 'F6e', 'E6e', 'E6e', 'D6q',
#    'G5e', 'G5e', 'G6e', 'G6e', 'A6e', 'A6e', 'G6q',
#    'F6e', 'F6e', 'E6e', 'E6e', 'D6e', 'D6e', 'C6q',
#]

# Tibet
song = [
    'E4h', 'B4q', 'E5e', 'F#5e',
    'G#5q', 'B6q', 'B6t', 'C#6t', 'B6t', 'G#6e', 'B6e',
    'B6h', 'sq', #'se', 'C#6e'
]

TOTAL_NOTES = len(song)

while True:
    cpx.pixels[pixel] = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    note_n, note_duration = decompose_note(song[note])

    if note_n == -1:
        time.sleep(note_duration)
    else:
        cpx.play_tone(f(note_n), note_duration)

    pixel = (pixel + 1) % 10
    note = (note + 1) % TOTAL_NOTES
