#This is the code for a raspberry pi breadboard rover.
#Run this in python3

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.OUT)    # motors setup
GPIO.setup(17, GPIO.OUT)    # You may need to change the w,a,s,d to match
GPIO.setup(27, GPIO.OUT)    # the wires on your rover. Do this by trial and error.
GPIO.setup(23, GPIO.OUT)    


while True:

        key=input("Type in your command")
              
        if key == "w":
                GPIO.output(17, GPIO.HIGH)      # forward
                GPIO.output(24, GPIO.HIGH)
                sleep(1)                        # goes for 2 seconds 
                GPIO.output(17, GPIO.LOW)
                GPIO.output(24, GPIO.LOW)
                
        elif key == "a":
                GPIO.output(17, GPIO.HIGH)      # left
                sleep(1)                        # goes for 2 seconds  
                GPIO.output(17, GPIO.LOW) 
                                                 
        elif key == "d":
                GPIO.output(24, GPIO.HIGH)      # right
                sleep(1)                        # goes for 2 seconds  
                GPIO.output(24, GPIO.LOW) 
                        
        elif key == "s":
                GPIO.output(27, GPIO.HIGH)      #reverse
                GPIO.output(23, GPIO.HIGH)
                sleep(1)                        # goes for 2 seconds  
                GPIO.output(27, GPIO.LOW)
                GPIO.output(23, GPIO.LOW)

        elif key == "z":                        #quits
                GPIO.cleanup()
                print("Powering down motors")
                print("Have a nice day!")
                            
