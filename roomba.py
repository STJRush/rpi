#Only in PYTHON2.7 as it uses readchar
import RPi.GPIO as GPIO #GPIO Libraries
from time import sleep #Sleep Functions
import readchar #allows you to hold down a key instead of hitting enter.
import random


GPIO.setwarnings(False)#Blocks error warnings
GPIO.setmode(GPIO.BCM) #Setting Up

GPIO.setup(23, GPIO.OUT) #reverse
GPIO.setup(24, GPIO.OUT) #forwards
GPIO.setup(17, GPIO.OUT) #left
GPIO.setup(27, GPIO.OUT) #right

GPIO.setup(22, GPIO.IN)  #Reads output from the IR motion sensor

def sensorf():  #SENSOR CODE
    i = 0           #resets count to zero
    while i < 20:    #checks sensor 5 times.

        sensor=GPIO.input(22)

        if sensor==1: #When output from motion sensor is LOW
            print("No Obstructions!!")
            sleep(0.1)
        elif sensor==0: #When output from motion sensor is HIGH
            print("Obstruction detected")
            
            GPIO.output(23, GPIO.LOW)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(17, GPIO.LOW)
            GPIO.output(27, GPIO.LOW)

	        sleep(1)    #stares down the object blocking it's path

            GPIO.output(23, GPIO.HIGH) #reverses after detecting obstacle
            sleep(1)
            GPIO.output(23, GPIO.LOW) #reverses after detecting obstacle


    	elif i==20:
		    break

        i = i+1


def auto(): #AUTOROBOT MODE

    while True:

        number=random.random()
        number=10*number

        if number > 5:
            GPIO.output(24, GPIO.HIGH)  #forward and left robot mode
            GPIO.output(17, GPIO.HIGH)
            sensor(f)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(17, GPIO.HIGH)

        if number < 5:
            GPIO.output(24, GPIO.HIGH)  #forward and left robot mode
            GPIO.output(17, GPIO.HIGH)
            sensor(f)
            GPIO.output(24, GPIO.LOW)
            GPIO.output(17, GPIO.HIGH)

#PROGRAM STARTS HERE
print("Code for Toy car. ReadChar. Sense. Python 2.7")
print("select control method")
print("To hold down keys to drive, type... h")
print("To hit enter each time to drive, type... y")
choice=raw_input("Type now.")


while True: #MODE SELECTION MENU

    if choice=="h":

        key=readchar.readkey()  #choose "hold down key" steering mode

    elif choice=="y":
        key=raw_input("Enter command")  #choose hit "enter" steering mode
    elif choice=="n":
        auto()

        #MOTOR CONTROLS

    if key=="w": #forward
        print("forward")
        GPIO.output(24, GPIO.HIGH)       
        sensorf()        
        GPIO.output(24, GPIO.LOW)        

    elif key=="a": #left
        print("left")
        GPIO.output(17, GPIO.HIGH)
        sensorf()
        GPIO.output(17, GPIO.LOW)

    elif key=="q": #forward and left
        print("forward and left")
        GPIO.output(24, GPIO.HIGH)
	    GPIO.output(17, GPIO.HIGH)
        sensorf()
        GPIO.output(24, GPIO.LOW)
	    GPIO.output(17, GPIO.LOW)

    elif key=="e": #forward and right
        print("forward and right")
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)
	    sensorf()
        GPIO.output(24, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)

    elif key=="d": #right
        print("right")
        GPIO.output(27, GPIO.HIGH)
        sensorf()
        GPIO.output(27, GPIO.LOW)

    elif key=="s": #reverse
        print("reverse")
        GPIO.output(23, GPIO.HIGH)
        sensorf()
        GPIO.output(23, GPIO.LOW)

    elif key=="c": #reverse and right
        print("reverse and right")
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)
	    sensorf()
        GPIO.output(23, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)

    elif key=="z": #reverse and right
        print("Forward and right")
        GPIO.output(23, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)
	    sensorf()
        GPIO.output(23, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)

    elif key=="0": #Everything off
        GPIO.output(23, GPIO.LOW)
        GPIO.output(24, GPIO.LOW)
        GPIO.output(17, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)

        
    elif key=="k":
        GPIO.cleanup()
        print("shutting down motors...")
        sleep(1)
        break   
