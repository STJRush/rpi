#This program tells a raspberry pi rover to move around. See DCUish on youtube for video.


import RPi.GPIO as GPIO         #allows you to use GPIO (motors etc)
from time import sleep          #allows you to use sleep

GPIO.setmode(GPIO.BOARD)        #chooses "count the pins on the board" as pin names eg.1,2

GPIO.setup(11, GPIO.OUT)        #sets up switchs 11,13,16,18, ready to use.
GPIO.setup(13, GPIO.OUT)

GPIO.setup(16, GPIO.OUT) 
GPIO.setup(18, GPIO.OUT)

while True:     #loops the indented bit below to stop python exiting when done

        key=input("Type W,A,S or D and hit enter")   #records what you type and calls it "key"

        if key == "w":                  #forward
            GPIO.output(18, GPIO.HIGH)
            sleep(2)
            GPIO.output(18, GPIO.LOW)

        elif key == "s":                #reverse
            GPIO.output(16, GPIO.HIGH)
            sleep(2)
            GPIO.output(16, GPIO.LOW)

        elif key == "a":                #steers left
            GPIO.output(13, GPIO.HIGH)
            sleep(2)
            GPIO.output(13, GPIO.LOW)
            

        elif key == "d":                #steers right
            GPIO.output(11, GPIO.HIGH)
            sleep(2)
            GPIO.output(11, GPIO.LOW)
        
        elif key == "z":                #quits the program
            GPIO.cleanup()
            print("Motors on safe, exiting. Have a nice day!")
            sleep(1)
            break
