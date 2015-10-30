#!/usr/bin/env python
import skywriter
import signal
import lifx
from helpers import *

# Create the LIFX connection
lights = lifx.Lifx()

# Settings 
brightness_list = listify(lifx.Brightness.__dict__)
colour_list = listify(lifx.Colour.__dict__)
print brightness_list
print colour_list

def change_brightness(direction):
	colours = lights.get_colours()
	hue = colours[0]
	brightness = colours[2]
	brightness_current = get_state(lifx.Brightness, brightness)
	brightness_next = get_next_element(brightness_current, brightness_list, direction)
	print colour_next
	brightness_next = eval("lifx.Brightness." + brightness_next)
	print brightness_next
	lights.set_colour(hue, brightness = brightness_next)

def change_colour(direction):
	colours = lights.get_colours()
	hue = colours[0]
	brightness = colours[2]
	colour_current = get_state(lifx.Colour, hue)
	colour_next = get_next_element(colour_current, colour_list, direction)
	print colour_next
	colour_next = eval("lifx.Colour." + colour_next)
	print colour_next
	lights.set_colour(colour_next, brightness = brightness)

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
    elif start == "west" and finish == "east":
    	change_colour(operator.add)
    elif start == "east" and finish == "west":
    	change_colour(operator.sub)

signal.pause()