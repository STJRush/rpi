#This is the code for a 4 motor raspberry pi breadboard rover with an IR sensor.
#You may need to change some of the GPIO numbers to match your rover's wires.

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(24, GPIO.OUT)    # motors setup
GPIO.setup(17, GPIO.OUT)    
GPIO.setup(27, GPIO.OUT)   
GPIO.setup(23, GPIO.OUT)    

GPIO.setup(25, GPIO.IN)     #sensor setup



########### the sensor check function ##########################
def  sensorcheck:()

    i=0                             #starts a counter at zero

    while i<5:   
        sensor=GPIO.input(25)       #this reads from the sensor

        if sensor==1:               #this means there is no signal
            print("ALL CLEAR")
            sleep(0.1)              #allows wheels to keep going

        elif sensor==0:             #this means there is a signal
            print("OH NOES! ICEBERG DEAD AHEAD SIR!")
            print("HALT MOTORS!")
            GPIO.output(17, GPIO.LOW)   #stops wheels
            GPIO.output(27, GPIO.LOW)
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
            
        elif i=5:                   # once the counter gets to five
            break                   # break out of the function, resume the program.
                
        i=i+1                       #counts to 5
    
##################################################################################
    
    

while True:

        key=input("Type in your command")
              
        if key == "w":
                GPIO.output(17, GPIO.HIGH)      # forward
                GPIO.output(24, GPIO.HIGH)
                sensorcheck()                   # runs the sensor check function 
                GPIO.output(17, GPIO.LOW)
                GPIO.output(24, GPIO.LOW)
                
        elif key == "a":
                GPIO.output(17, GPIO.HIGH)      # left
                sensorcheck()                   # runs the sensor check function 
                GPIO.output(17, GPIO.LOW) 
                                                 
        elif key == "d":
                GPIO.output(24, GPIO.HIGH)      # right
                sensorcheck()                   # runs the sensor check function 
                GPIO.output(24, GPIO.LOW) 
                        
        elif key == "s":
                GPIO.output(27, GPIO.HIGH)      #reverse
                GPIO.output(23, GPIO.HIGH)
                sensorcheck()                   #runs the sensor check function 
                GPIO.output(27, GPIO.LOW)
                GPIO.output(23, GPIO.LOW)

        elif key == "z":                        #quits
                GPIO.cleanup()
                print("Powering down motors")
                print("Have a nice day!")
                            
