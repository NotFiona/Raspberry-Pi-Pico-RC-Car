"""A class for controlling a DC motor"""

from machine import PWM, Pin, 
from time import sleep

class Motor:
    """Model for the DC motors and connections"""
    
    def __init__(self, pin_pos, pin_neg):
        """initialize the motor controller pins on the RPi Pico and speed
        
        pin_pos is the postive PWM pin to control the motor
        pin_neg is the negative PWM pin to control the motor
        freq - the frequency of the PWM
        speed -- should be in range (-100 - 100) with |100.0| being max speed, defaults to 0
        note: the idea is to only use change_speed method to keep from instantaneously reversing the motor 
                but I left forward and backward public for testing purposes, and maybe reversing the motor isn't terrible??
        """
        
        self.freq = 100
        self.pin_pos = PWM(Pin(pin_pos))
        self.pin_pos.freq(self.freq)
        self.pin_neg = PWM(Pin(pin_neg))
        self.pin_neg.freq(self.freq)
        self.speed = 0
        
    def forward(self, speed):
        if speed < 0:
            print("error, speed < 0 on call to forward")    
        else:
            if speed > 100:
                speed = 100
            self.speed = speed
            self.pin_pos.duty_u16(self.speed * 650)
            self.pin_neg.duty_u16(0)
            print(f"forward speed={self.speed}")
        
    def backward(self, speed):
        if speed > 0:
            print("error, speed > 0 on call to backward")
        else:
            if speed < -100:
                speed = -100
            self.speed = speed
            self.pin_pos.duty_u16(0)
            self.pin_neg.duty_u16(-650 * self.speed)
            print(f"backward speed={self.speed}")

    def stop(self):
        self.pin_pos.duty_u16(0)
        self.pin_neg.duty_u16(0)
        self.speed = 0
        
    def change_speed(self, delta_speed):
        new_speed = self.speed + delta_speed
        old_speed = self.speed
        
        if new_speed > 100:
            self.speed = 100
        elif new_speed < -100:
            self.speed = -100
        else:
            self.speed = new_speed
        
        if old_speed * self.speed <= 0: # reversing direction
            temp_speed = self.speed # storing since stop will set it to 0
            self.stop() #stop first
            sleep(0.2) #short pause
            self.speed = temp_speed
            
            if self.speed > 0:
                self.forward(self.speed)
            else:
                self.backward(self.speed)
        else:
            if self.speed > 0:
                self.forward(self.speed)
            else:
                self.backward(self.speed)


