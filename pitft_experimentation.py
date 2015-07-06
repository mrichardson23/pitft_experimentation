#!/usr/bin/python
from PIL import Image, ImageDraw, ImageFont, ImageColor
import socket
import os
import RPi.GPIO as GPIO
from time import sleep
refreshNeeded = True;

buttonA = 17
buttonB = 22
buttonC = 23
buttonD = 27
buttonPressed = None

OptionAColor = (255,255,255,255)
OptionBColor = (255,255,255,255)
OptionCColor = (255,255,255,255)
OptionDColor = (255,255,255,255)

GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonB, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonC, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonD, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# get a font
fnt = ImageFont.truetype('/usr/share/fonts/truetype/roboto/Roboto-Medium.ttf', 30)
# get a drawing context


try:
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(('8.8.8.8', 0))
	local_ip_address = s.getsockname()[0]
except:
	local_ip_address = "No IP"

while (refreshNeeded):
	canvas = Image.new('RGBA', (240,320), (255,255,255,0))
	d = ImageDraw.Draw(canvas)

	d.rectangle([0,0,240,320], fill=(0,0,0))



	d.text((10,5), "Option A", font=fnt, fill=OptionAColor)
	d.text((10,95), "Option B", font=fnt, fill=OptionBColor)
	d.text((10,185), "Option C", font=fnt, fill=OptionCColor)
	if (local_ip_address == "No IP"):
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect(('8.8.8.8', 0))
			local_ip_address = s.getsockname()[0]
			refreshNeeded = True
		except:
			local_ip_address = "No IP"
	d.text((10,275), local_ip_address, font=fnt, fill=OptionDColor)
	canvas = canvas.rotate(90)
	canvas.save("/tmp/test.png")

	if (refreshNeeded):
		print "Refreshing Display..."
		os.system('sudo fbi -T 2 -d /dev/fb1 -noverbose /tmp/test.png')
		refreshNeeded = False
	sleep(.3)
	while (refreshNeeded == False):
		if not GPIO.input(buttonA):
			print "Button A Pressed."
			buttonPressed = "A"
			refreshNeeded = True
			OptionAColor = (255,0,0,255)
			OptionBColor = (255,255,255,255)
			OptionCColor = (255,255,255,255)
			OptionDColor = (255,255,255,255)
		if not GPIO.input(buttonB):
			print "Button B Pressed."
			buttonPressed = "B"
			refreshNeeded = True
			OptionAColor = (255,255,255,255)
			OptionBColor = (255,0,0,255)
			OptionCColor = (255,255,255,255)
			OptionDColor = (255,255,255,255)
		if not GPIO.input(buttonC):
			print "Button C Pressed."
			buttonPressed = "C"
			refreshNeeded = True
			OptionAColor = (255,255,255,255)
			OptionBColor = (255,255,255,255)
			OptionCColor = (255,0,0,255)
			OptionDColor = (255,255,255,255)
		if not GPIO.input(buttonD):
			print "Button D Pressed."
			buttonPressed = "D"
			refreshNeeded = True
			OptionAColor = (255,255,255,255)
			OptionBColor = (255,255,255,255)
			OptionCColor = (255,255,255,255)		
			OptionDColor = (255,0,0,255)

		sleep(.1)




