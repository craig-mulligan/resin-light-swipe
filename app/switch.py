#!/usr/bin/env python
import skywriter
import signal
import lifx
from helpers import *

# Create the LIFX connection
lights = lifx.Lifx()

# Settings 
brightness_list = ['DIM', 'MOOD', 'NORMAL', 'FULL']
colour_list = ['RED','ORANGE', 'YELLOW', 'WHITE','GREEN','PURPLE', 'BLUE']

def change_brightness(direction):
	colours = lights.get_colours()
	hue = colours[0]
	brightness = colours[2]
	brightness_current = get_state(lifx.Brightness, brightness)
	brightness_next = get_next_element(brightness_current, brightness_list, direction)
	print brightness_next
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
    	try:
    		change_brightness(operator.sub)
    	except: 
  			pass
    elif start == "south" and finish == "north":
    	try:
    		change_brightness(operator.add)
    	except: 
  			pass
    elif start == "west" and finish == "east":
    	try:
    		change_colour(operator.add)
    	except: 
  			pass
    elif start == "east" and finish == "west":
    	try:
    		change_colour(operator.sub)
    	except: 
  			pass
  			
signal.pause()