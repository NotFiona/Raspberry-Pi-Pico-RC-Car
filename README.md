# Raspberry-Pi-Pico-RC-Car

<img src="https://github.com/NotFiona/Raspberry-Pi-Pico-RC-Car/blob/main/RC Car Prototype.jpg" width="591" height="443">

## Project information
This is the page for my first Raspberry Pi project, an RC Car built on Raspberry Pi Pico with Bluetooth control.
Why do this?  It's purely an educational endeavor to learn more about all of the components involved.
Why did I choose the parts?  The parts selection was also a learning experience, so there may be better parts.  I'm open to suggestions!!

## Parts list (work in progress)
- Raspberry Pi Pico

- [DC Gearbox Motor](https://www.adafruit.com/product/3777) (QTY 2)

- [L9110H Motor Driver chip](https://www.adafruit.com/product/4489) (QTY 2)

- [wheels](https://www.adafruit.com/product/4205) (QTY 2)

- HC05 Serial Bluetooth - various sites, I ordered this through Amazon

- USB battery (mine is a huge old one)

- AA batteries (QTY4)

- [4x AA Battery holder](https://www.adafruit.com/product/3859)

- Misc. parts like wires, extra "wheels", etc.

## Circuit Diagram
![Circuit Diagram](https://github.com/NotFiona/Raspberry-Pi-Pico-RC-Car/blob/main/Circuit-Diagram%20v0.1.png)

## The Code
- main.py contains the bluetooth monitoring and control code
- motor.py contains the Motor class used to set up the motors and control the speed and direction

## Controlling from the phone
The quickest way to control this seemed to be to use the app Serial Bluetooth Terminal.
Steps:
1. Download the app
2. Power up your device and use the phone's connection menu to connect HC-05 and use the default password/passkey either 0000 or 1234
3. Open the app, go to devices and select the HC-05
4. Program the buttons:  a long tap opens the button, and then change to the desired settings (see screenshots below)
5. Have fun controlling your RC car!!

<img src="https://github.com/NotFiona/Raspberry-Pi-Pico-RC-Car/blob/main/SBT-1.jpg" width="400" height="800"> <img src="https://github.com/NotFiona/Raspberry-Pi-Pico-RC-Car/blob/main/SBT-2.jpg" width="400" height="800">



## What is next? 
Other than designing and building it?  Figuring out how to do it better?  If I'm happy with it, maybe design a 3d printed chassis?
Playstation controller for steering?  Camera?  Full on autonomous vehicle!?!?!?  We'll see where this goes!! :P
