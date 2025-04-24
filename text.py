import RPi.GPIO as GPIO
import time
#GPIO SETUP
channel = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
       if GPIO.input(channel):
                   print ("Water Detected!")
       else:
                   print ("Water Detected!")
GPIO.add_event_detect(channel, GPIO.BOTH, bouncettime=300) # let us know when the pin goes HIGH orLOW
GPIO.add_event_callback(channel, callback) # assign function to GPIO PIN, Run function on change
# infinite loop
while True:
               time.sleep(0)

