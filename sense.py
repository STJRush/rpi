#Only in PYTHON2.7
import RPi.GPIO as GPIO #GPIO Libraries
from time import sleep #Sleep Functions
import readchar #keyboards

GPIO.setwarnings(False)#Blocks error warnings
GPIO.setmode(GPIO.BCM) #Setting Up

GPIO.setup(23, GPIO.OUT) #back right
GPIO.setup(24, GPIO.OUT) #front right
GPIO.setup(17, GPIO.OUT) #front left
GPIO.setup(27, GPIO.OUT) #back left
GPIO.setup(26, GPIO.OUT) #red led
GPIO.setup(16, GPIO.OUT) #green led
GPIO.setup(21, GPIO.IN)  #Reads output from the IR motion sensor

def sensorf():
    i = 1
    while i < 6:

        sensor=GPIO.input(21)

        if sensor==1: #When output from motion sensor is LOW
            print("No Obstructions!!")
            sleep(1)
        elif sensor==0: #When output from motion sensor is HIGH
            print("Obstruction detected")
            sleep(1)
            GPIO.output(23, GPIO.LOW) #back right
            GPIO.output(24, GPIO.LOW) #front right
            GPIO.output(17, GPIO.LOW) #front left
	    GPIO.output(27, GPIO.LOW) #back left

	elif i==5:
		break

        i = i+1




print("Toy car. ReadChar. Sense.")
sleep(2)

while True:

    key=readchar.readkey()

    if key=="w": #forward
        
        GPIO.output(24, GPIO.HIGH)
        
        sensorf()
        
        GPIO.output(24, GPIO.LOW)
        


    elif key=="a": #left
        GPIO.output(17, GPIO.HIGH)
        sensorf()
        GPIO.output(17, GPIO.LOW)

    elif key=="q": #forward and left
        GPIO.output(24, GPIO.HIGH)
	GPIO.output(17, GPIO.HIGH)
        sensorf()
        GPIO.output(24, GPIO.LOW)
	GPIO.output(17, GPIO.LOW)

    elif key=="d": #right
        GPIO.output(27, GPIO.HIGH)
        sensorf()
        GPIO.output(27, GPIO.LOW)

    elif key=="s": #reverse 
        GPIO.output(23, GPIO.HIGH)
        sensorf()
        GPIO.output(23, GPIO.LOW)

    elif key=="e": #forward and right
        GPIO.output(24, GPIO.HIGH)
        GPIO.output(27, GPIO.HIGH)
	sensorf()
        GPIO.output(24, GPIO.LOW)
        GPIO.output(27, GPIO.LOW)
        

    elif key=="z":
        GPIO.cleanup()
        sleep(1)
        break   
