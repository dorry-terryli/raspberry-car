#!/usr/bin/python

# terry
# 2016.12.02

import time
import RPi.GPIO as io

# HY-SRF05

class Distance:
    pin_trigger = 0
    pin_echo = 0
    
    def __init__(self,pin_trigger,pin_echo):
        self.pin_trigger = pin_trigger
        self.pin_echo = pin_echo
        io.setmode(io.BOARD)
        io.setup(pin_trigger,io.OUT)
        io.setup(pin_echo,io.IN)
        
    def measure(self):
        io.output(self.pin_trigger,io.HIGH)
        time.sleef(0.00001)
        io.output(self.pin_trigger,io.LOW)
        start = time.time()

        while io.input(self.pin_echo) == 1 :
            stop = time.time()

        elapsed = stop-start
        distance = (elapsed * 34300)/2

        return distance
    
