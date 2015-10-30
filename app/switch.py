#!/usr/bin/env python
import skywriter
import signal
import lifx
from helpers import *

# Create the LIFX connection
lights = lifx.Lifx()

# Settings 
brightness_list = ["OFF", "DIM", "MOOD", "NORMAL", "FULL"]

def change_brightness(direction):
	colours = lights.get_colours()
	hue = colours[0]
	brightness = colours[2]
	brightness_current = get_state(lifx.Brightness, brightness)
	brightness_next = get_next_element(brightness_current, brightness_list, direction)
	brightness_next = eval("lifx.Brightness." + brightness_next)
	print brightness_next
	lights.set_colour(hue, brightness = brightness_next)

@skywriter.tap()
def tap(position):
    print('Tap!', position)
    if lights.is_on() == 0:
        lights.on()
    else:
        lights.off()

@skywriter.flick()
def flick(start, finish):
    print('Got a flick!', start, finish)
    if start == "north" and finish == "south":
    	change_brightness(operator.sub)
    elif start == "south" and finish == "north":
    	change_brightness(operator.add)

signal.pause()