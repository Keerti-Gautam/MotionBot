
# Make sure this library is installed.
import RPi.GPIO as GPIO
import time
import requests
import json

# Set Pin Number as per BCM(GPIO) Scheme.
# See https://pinout.xyz/ for the same.
GPIO.setmode(GPIO.BCM)
pin = 7

# PUD_DOWN Scheme: No Signal : 0, Signal : 1
GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN)

url = "https://api.ciscospark.com/v1/messages"
head = {"Content-Type": "application/json", "Authorization": "Bearer *******Bearer token goes here*****"}
d = {"toPersonEmail": "someemail@example.com", "text": "Someone's in the house!"}

try:
	while(True):
		# Will help in determining 0/1 state clearly (It should!)
		if GPIO.input(pin):
			print("This should be 1")
			r = requests.post(url, headers=head, data = json.dumps(d))
			# print r.json() to see the response
		else:
			print("This should be 0")
		time.sleep(.200)
except KeyboardInterrupt:
	GPIO.cleanup()
	print("Exiting")
