import Adafruit_DHT
from time import sleep
from firebase import firebase


#API KEY
firebase = firebase.FirebaseApplication('https://webapptest-97c23.firebaseio.com', None)


...
sensor = Adafruit_DHT.DHT11
pin = 4
humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

print("Let's start with getting python to read from the sensor..")
print("humidity is", humidity)
print("teperature is", temperature)

#####


print("Now let's upload that to Firebase")
#Patches on extra data from our temp and humidity variables at the top of the program, simulated sensor readings
result = firebase.patch('/sensor/dht/', {'Temperature': temperature, 'Humidity': humidity})

sleep(2)
print("Give it a second...")
sleep(2)

print("Okay Done")
print("Now seeing if we can read from the database")

print("The last uploaded temperature was:")
result = firebase.get('/sensor/dht/Temperature', None)
print(result)

print("The last uploaded humidity was:")
result = firebase.get('/sensor/dht/Humidity', None)
print(result)

sleep(3)
print("program done")