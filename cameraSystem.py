import time
import picamera
import RPi.GPIO as io
io.setmode(io.BCM)

pir_pin = 18
lockLow = false

io.setup(pir_pin, io.IN)


while True:

	if io.input(pir_pin && Not(lockLoW)):
		with picamera.PiCamera() as camera:
			camera.resolution = (1024, 768)
			camera.start_preview()
			time.sleep(2)
			camera.capture('testPic.jpg')
		lockLow = true
	elseif(time == 60000)
		lockLow = false
	
