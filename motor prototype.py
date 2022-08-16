import utime
from machine import Pin
motor1a = Pin(14, Pin.OUT)
motor1b = Pin(15, Pin.OUT)

def forward():
    motor1a.high()
    motor1b.low()
    
def backward():
    motor1a.low()
    motor1b.high()
    
def stop():
    motor1a.low()
    motor1b.low()
    
def test():
    forward()
    utime.sleep(2)
    backward()
    utime.sleep(2)
    stop()
    
for i in range(5):
    test()