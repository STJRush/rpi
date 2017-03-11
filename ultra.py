import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23 
ECHO = 24

print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print "Waiting For Sensor To Settle"
time.sleep(2)


def distcheck():

  GPIO.output(TRIG, True)  #fires a pulse
  time.sleep(0.00001)
  GPIO.output(TRIG, False)

  while GPIO.input(ECHO)==0:  #measure some times
    pulse_start = time.time()

  while GPIO.input(ECHO)==1:
    pulse_end = time.time()

  pulse_duration = pulse_end - pulse_start  #does the maths

  distance = pulse_duration * 17150

  distance = round(distance, 2)

  print "Distance:",distance,"cm"

  
#the new bit that measures speed
  
distcheck()
dist1=distance

time.sleep(0.5)

distcheck()
dist2=distance

displacement=dist2-dist1
velocity=displacement/0.5

velocity = round(velocity, 2)

print("Your velocity is")
print(velocity)

GPIO.cleanup()


