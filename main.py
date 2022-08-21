from machine import Pin, UART
from motor import Motor
from time import sleep

#initialize bluetooth serial comms
uart = UART(0,9600)

# set up motors
left_motor = Motor(16, 17)
right_motor = Motor(20, 21)


def turn_right():
    left_motor.change_speed(-10)
    right_motor.change_speed(10)
    
def turn_left():
    left_motor.change_speed(10)
    right_motor.change_speed(-10)
    
def stop():
    left_motor.stop()
    right_motor.stop()
    
def speed_inc():
    left_motor.change_speed(10)
    right_motor.change_speed(10)
    
def speed_dec():
    left_motor.change_speed(-10)
    right_motor.change_speed(-10)

def check_command(command):
    if command == b's':
        stop()
        #print("stop CMD rcvd")
    elif command == b"i":
        speed_inc()
        #print("inc CMD rcvd")
    elif command == b"d":
        speed_dec()
        #print("dec CMD rcvd")
    elif command == b"r":
        turn_right()
        #print("right CMD rcvd")
    elif command == b"l":
        turn_left()
        #print("left CMD rcvd")
    else:
        print("invalid command received")    

while True:
    if uart.any():
        command = uart.readline()
        print(command)
        check_command(command)
        #sleep(1)
        

