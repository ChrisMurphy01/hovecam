 #!/usr/bin/env python
from picamera import PiCamera
from twython import Twython
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET
import time 

api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

camera = PiCamera()
#camera.resolution = (1280, 780)
camera.zoom = (0.25, 0.2, 0.5, 0.5)
#camera.start_preview()
time.sleep(5)
camera.capture("webcam.jpg")
#camera.stop_preview()

photo = open('webcam.jpg', 'rb')

api.update_status_with_media(media=photo, status='')
