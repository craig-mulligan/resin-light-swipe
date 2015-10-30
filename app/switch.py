#!/usr/bin/env python
import skywriter
import signal
import lifx

# Create the LIFX connection
lights = lifx.Lifx()

@skywriter.flick()
def flick(start, finish):
    print('Got a flick!', start, finish)

@skywriter.tap()
def tap(position):
    print('Tap!', position)
    if lights.is_on() == 0:
        lights.on()
    else:
        lights.off()

signal.pause()