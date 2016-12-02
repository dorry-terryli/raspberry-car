#!/usr/bin/python

# L298N

import time
import RPi.GPIO as io

# control car motor drived by L298N 
class Car:
    pin1 = 0
    pin2 = 0
    pin3 = 0
    pin4 = 0
    
    def __init__(self,pin1,pin2,pin3,pin4):
        self.pin1 = pin1
        self.pin2 = pin2
        self.pin3 = pin3
        self.pin4 = pin4
        io.setmode(io.BOARD)
        io.setup(pin1,io.OUT)
        io.setup(pin2,io.OUT)
        io.setup(pin3,io.OUT)
        io.setup(pin4,io.OUT)
    
    def __forwardA(self):
        io.output(self.pin1,io.HIGH)
        io.output(self.pin2,io.LOW)

    def __backwardA(self):
        io.output(self.pin1,io.LOW)
        io.output(self.pin2,io.HIGH)
    
    def __forwardB(self):
        io.output(self.pin3,io.HIGH)
        io.output(self.pin4,io.LOW)

    def __backwardB(self):
        io.output(self.pin3,io.LOW)
        io.output(self.pin4,io.HIGH)

    def __resetA(self):
        io.output(self.pin1,io.LOW)
        io.output(self.pin2,io.LOW)

    def __resetB(self):
        io.output(self.pin3,io.LOW)
        io.output(self.pin4,io.LOW)

    #---------car controll-----------
    def forward():
        forwardA()
        forwardB()

    def backward():
        backwardA()
        backwardB()

    def left():
        resetA()
        forwardB()

    def right():
        forwardA()
        resetB()

    def clockwise():
        forwardA()
        backwardB()

    def counterclockwise():
        forwardB()
        backwardA()

    def stop():
        resetA()
        resetB()
        
