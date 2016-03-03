import time
import picamera
import RPi.GPIO as io
io.setmode(io.BCM)

pir_pin = 18
lockLow = False
oldtime = time.time();

io.setup(pir_pin, io.IN)

print("Calibrating motion sensor.")


while True:
	if io.input(pir_pin) and Not(lockLow):
		print("Motion Detected!")
		with picamera.PiCamera() as camera:
			camera.resolution = (1024, 768)
			camera.start_preview()
			time.sleep(2)
			camera.capture('testPic.jpg')
		lockLow = True
		oldtime = time.time()
	elif(time.time() - oldtime >= 60) and lockLow:
		print("Unlocking")
		lockLow = False
		oldtime = time.time()	
