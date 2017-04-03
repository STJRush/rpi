#Only in PYTHON2.7 as it uses readchar
import RPi.GPIO as GPIO #GPIO Libraries
from time import sleep #Sleep Functions
import readchar #allows you to hold down a key instead of hitting enter.
import random


GPIO.setwarnings(False)#Blocks error warnings
GPIO.setmode(GPIO.BCM) #Setting Up

GPIO.setup(23, GPIO.OUT) #left wheels forward       #these may differ if wired another way
GPIO.setup(24, GPIO.OUT) #left wheels reverse
GPIO.setup(17, GPIO.OUT) #right wheels reverse
GPIO.setup(27, GPIO.OUT) #right wheels forward

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
            stop()
	    sleep(1)    #stares down the object blocking it's path
            rev()       #reverses after detecting obstacle
            sleep(4)
            stop()


    	elif i==20:
		    break

        i = i+1


def auto(): #AUTOROBOT MODE

    while True:

        number=random.random()
        number=10*number

        if number > 5:
            right()
            sleep(3)
            stop()
            fwd()
            sensorf()
            stop()

        if number < 5:
            left()
            sleep(3)
            stop()
            fwd()  #forward and left robot mode
            sensorf()
            stop()



#Which control functions are tied to GPIO switches

def fwd():
    GPIO.output(23, GPIO.HIGH)          #THESE ARE WHAT YOU SHOULD CHANGE IF
    GPIO.output(27, GPIO.HIGH)          #YOUR ROVER IS WIRED ANOTHER WAY
                                        #FIXING THESE WILL FIX EVERYTHING
def rev():
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(17, GPIO.HIGH)

def left():
    GPIO.output(24, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)

def right():
    GPIO.output(23, GPIO.HIGH)
    GPIO.output(27, GPIO.HIGH)

def stop():
    GPIO.output(23, GPIO.LOW)
    GPIO.output(24, GPIO.LOW)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)


#PROGRAM STARTS HERE
print("Code for Toy car. ReadChar. Sense. Python 2.7")
print("select control method")
print("To hold down keys to drive, type... h")
print("To hit enter each time to drive, type... y")
print("for auto robot drive, type n")
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
        fwd()
        sensorf()        
        stop()

    elif key=="a": #left
        print("left")
        left()
        sensorf()
        stop()

    elif key=="d": #right
        print("right")
        right()
        sensorf()
        stop()

    elif key=="s": #reverse
        print("reverse")
        rev()
        sensorf()
        stop()

    elif key=="c": #Everything off
        stop()
        
    elif key=="z":
        stop()
        GPIO.cleanup()
        print("shutting down motors...")
        sleep(1)
        break   
