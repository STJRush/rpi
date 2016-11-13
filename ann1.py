

import RPi.GPIO as GPIO  #GPIO's are General Purpose Inputs and Outputs. The pins.
import time
import readchar

GPIO.setmode(GPIO.BOARD) #chooses pin labeling system. We're going to use pin numbers.

GPIO.setup(7,GPIO.OUT) #sets pin 7 for servo pulse
GPIO.setup(8,GPIO.OUT) #sets pin 14 to forward motor output
GPIO.setup(10,GPIO.OUT) #sets pin 15 to reverse motor output
#GPIO.setup(11,GPIO.OUT) #sets pin 11 to drive 2nd motor forward, not sure what I'll use this for yet.
#GPIO.setup(13,GPIO.OUT) #sets pin 13 to drive 2nd motor forward not sure what I'll use this for yet.



p = GPIO.PWM(7,50)      #pulses pin 7. 50Hz means 50 pulses per second.
p.start(7.5)            #starts at duty cycle 7.5 (neutral position)

print("Welcome to Ann Droid v0.5")

print("   _                    ___           _     _ ")
print("  /_\  _ __  _ __      /   \_ __ ___ (_) __| |")
print(" //_\\| '_ \| '_ \    / /\ / '__/ _ \| |/ _` |")
print("/  _  \ | | | | | |  / /_//| | | (_) | | (_| |")
print("\_/ \_/_| |_|_| |_| /___,' |_|  \___/|_|\__,_|")
print("")
print("Welcome to Ann Droid v0.5")
print("")
print("Here are the controls:")
print("e = forward 1 second")
print("c = reverse 1 second")
print("a = steer wheel to 10 o clock position left")
print("w = steer wheel to 12 o clock position front")
print("d = steer wheel to 2 o clock position right")

try:
    while True:
        choice=readchar.readkey()
	if choice == "r":
		print("Moving forward")
		GPIO.output(8, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(8, GPIO.LOW)
	elif choice == "f":
		print("Moving backwards")
		GPIO.output(10, GPIO.HIGH)
		time.sleep(1)
		GPIO.output(10, GPIO.LOW)
        elif choice == "w":
		print("Aim forward")
		p.ChangeDutyCycle(8)  #neutral 90 degrees
		time.sleep(1)
        elif choice == "a":
		print("Aim left")
		p.ChangeDutyCycle(9.5)  #left towards 0 degrees
		time.sleep(1)
        elif choice == "d":
		print("Aim right")
		p.ChangeDutyCycle(6.5)  #right towards 180 degrees
		time.sleep(1)
	elif choice == "CTRL":
		print("This works?")
        elif choice == "z":
		print("Motors on standby")
		print("Press Ctrl Z to exit")
            	p.stop()
            	GPIO.cleanup()
            	break




except KeyboardInterrupt: #if you press ctrl z
   		 p.stop()              #pulses will stop

   		 GPIO.cleanup()        #stops all signals to pins

