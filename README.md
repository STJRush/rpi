# USEFUL CODE

For raspberry pi projects.


**2ircar.py**
Code for the **2 motor** toy car that you can drive about. Has an IR LED sensor. Stops if it seems something.
Best run in python 2.7

**2ircarRoomba.py**
Similar to the code above except that it has an Auto mode. It drives itself, detects an object,
then reverses. Tries again.

**4rov.py**
Code to contol the **4 motor** Breadboard rover using the keyboard. Best run in python3.

**4rovBOARD.py**
Same as above except it uses the BOARD GPIO pin naming system instead of BCM.

**4rovIR.py**
Same as above except with an Infrared (IR) sensor that tries to stop you hitting things.

**4rovIR_AUTO.py**
Same as the IR rover above but with a Roomba Autosteer mode. Proper robot.

**4rovULTRA.py**
Same as 4rovIR_AUTO.py above but upgraded to a longer range UltraSonic sensor instead of the IR sensor.

**gpiotest.py**
Spins all 4 motors on the GPIO to test your motors are working correctly.

**ultravelocity.py**
Uses the ultrasonic sensor to measure the velocity (the speed in a direction).


