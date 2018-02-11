from gpiozero import CPUTemperature
import RPi.GPIO as GPIO

from time import sleep, strftime, time
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)
print ("Distance Measurement In Progress")

TRIG = 23 
ECHO = 24
distance = 0

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print ("Waiting For Sensor To Settle")
sleep(2)



cpu = CPUTemperature()

plt.ion()

x = []
y = []


def distcheck():

  GPIO.output(TRIG, True)  #fires a pulse
  sleep(0.00001)
  GPIO.output(TRIG, False)

  while GPIO.input(ECHO)==0:  #measure some times
    pulse_start = time()

  while GPIO.input(ECHO)==1:
    pulse_end = time()

  pulse_duration = pulse_end - pulse_start  #does the maths

  global distance; distance = pulse_duration * 17150

  global distance; distance = round(distance, 2)

  print ("Distance:",distance,"cm")
  return distance


def write_temp(temp):
    with open("cpu_temp.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(temp)))

def graph(temp):
    y.append(temp)
    x.append(time())
    plt.clf()
    plt.scatter(x,y)
    plt.plot(x,y)
    plt.draw()


while True:
    #temp = cpu.temperature
    distcheck()
    #write_temp(temp)
    with open("cpu_dist.csv", "a") as log:
        log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(distance)))

    y.append(distance)
    x.append(time())
    plt.clf()
    plt.scatter(x,y)
    plt.plot(x,y)
    plt.draw()
    
    #graph(temp)
    sleep(0.01)
