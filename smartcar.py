#!/usr/bin/env python

import RPi.GPIO as io
import time,curses

# pins attribution
# motor A | left
in1_pin =
in2_pin = 

# motor B | right
int3_pin =
int4_pin = 

# always stop motors after xx seconds..
securetime = 10 

#GPIO inits
io.setmode(io.BOARD)
io.setup(in1_pin, io.OUT)
io.setup(in2_pin, io.OUT)
io.setup(in3_pin, io.OUT)
io.setup(in4_pin, io.OUT)

# motor A | forward
def forwardA():
    io.output(in1_pin,io.HIGH)
    io.output(in2_pin,io.LOW)

# motor A | backward
def backwardA():
    io.output(in1_pin,io.LOW)
    io.output(in2_pin,io.HIGH)

# motor A | reset
def resetA():
    io.output(in1_pin,io.LOW)
    io.output(in2_pin,io.LOW)
    
# motor B | forward
def forwardB():
    io.output(in3_pin,io.HIGH)
    io.output(in4_pin,io.LOW)

# motor B | backward
def backwardB():
    io.output(in3_pin,io.LOW)
    io.output(in4_pin,io.HIGH)

# motor B | reset
def resetB():
    io.output(in3_pin,io.LOW)
    io.output(in4_pin,io.LOW)

#-------------car direction part-------------    
    
# forward
def forward():
    forwardA()
    forwardB()
    time.sleep(1)
    resetA()
    resetB()

# backward
def backward():
    backwardA()
    backwardB()
    time.sleep(1)
    resetA()
    resetB()
    
# turn left
def left():
    backwardA()
    forwardB()
    time.sleep(1)
    resetA()
    resetB()

# turn right
def right():
    forwardA()
    backwardB()
    time.sleep(1)
    resetA()
    resetB()

# stop car
def stop():
    resetA()
    resetB()

# get keyboard input char
def input_char(message):
    try:
        win = curses.initscr()
        win.addstr(0, 0, message)
        while True: 
            ch = win.getch()
            if ch in range(32, 127): break
            time.sleep(0.05)
    except: raise
    finally:
        curses.endwin()
    return chr(ch)

# main loop
# w - forward
# s - backward
# a - left
# d - right
# q - stop
try:
    while True:
        #cmd = raw_input("ws - ad - q : ")
        dir = input_char("ws - ad - q : ")
        if dir == "w":
            forward()
        elif dir == "s":
            backward()
        elif dir == "a":
            left()
        elif dir == "d":
            right()
        elif dir == "q":
            stop()
        else:
            stop()
except Exception:
    stop()

    
