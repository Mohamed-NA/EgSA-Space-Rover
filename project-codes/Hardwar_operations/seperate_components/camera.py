raspistill -o Desktop/image.jpg		# to take a picture after 5 seconds and save it in the desktop

raspistill -o Desktop/image-small.jpg -w 640 -h 480	# you can change the dimensions of the picture

raspivid -o Desktop/video.h264		# to record a video

sudo apt install python3-picamera		# to install camera library

# ===========================================

# python code using picamera library
# code to show camera preview for 5 seconds
from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview()
sleep(5)
camera.stop_preview()

# NOTE: camera preview works only when a monitor is connected. If SSH or VNC is used camera preview will not work

# ===========================================

# To rotate camera preview
camera = PiCamera()
camera.rotation = 180			# 90, 180, 270, 0


# Make the camera preview see-through by setting an alpha level
camera.start_preview(alpha=200)		# alpha can be any number berween 0, 250

# ===========================================

# To take a still picture after 5 sec
camera.start_preview()
sleep(5)				# note: sleep must be set for at least 2 sec to enable cam sensors to sense light
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()

# ===========================================

#
camera.start_preview()
for i in range(30):
    sleep(2)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)	# i to number the images (imag0, imag1, ...)
camera.stop_preview()

# ===========================================

# to record a video
camera.start_preview()
camera.start_recording('/home/pi/Desktop/video.h264')
sleep(5)
camera.stop_recording()
camera.stop_preview()

# ===========================================

# To change the camera resolution
# The maximum resolution is 2592×1944 for still photos, and 1920×1080 for video recording.
camera.resolution = (2592, 1944)
camera.framerate = 15			# to set the max resolution you must set the frame to 15
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/max.jpg')
camera.stop_preview()

# ===========================================

# to add text to your img
camera.start_preview()
camera.annotate_text = "Hello world!"		# added text
camera.annotate_text_size = 50		# to change the size of the text(form 6 to 160, the default 32)
sleep(5)
camera.capture('/home/pi/Desktop/text.jpg')
camera.stop_preview()

# ===========================================

# to change the text color: using color module from picamera library
from picamera import PiCamera, Color

camera.start_preview()
camera.annotate_background = Color('blue')
camera.annotate_foreground = Color('yellow')
camera.annotate_text = " Hello world "
sleep(5)
camera.stop_preview()

# ===========================================

# to change brightness: (from 0 to 100, the default is 50)
camera.start_preview()
camera.brightness = 70
sleep(5)
camera.capture('/home/pi/Desktop/bright.jpg')
camera.stop_preview()

# ===========================================

# to change the contrast of the preview
camera.start_preview()
for i in range(100):
    camera.annotate_text = "Contrast: %s" % i
    camera.contrast = i
    sleep(0.1)
camera.stop_preview()

# ===========================================

# to change camera image effect: default is none
'''
none
negative
solarize
sketch
denoise
emboss
oilpaint
hatch
gpen
pastel
watercolor
film
blur
saturation
colorswap
washedout
posterise
colorpoint
colorbalance
cartoon
deinterlace1
deinterlace2
'''

camera.start_preview()
camera.image_effect = 'colorswap'
sleep(5)
camera.capture('/home/pi/Desktop/colorswap.jpg')
camera.stop_preview()

# to make a loop to try all effects:
camera.start_preview()
for effect in camera.IMAGE_EFFECTS:
    camera.image_effect = effect
    camera.annotate_text = "Effect: %s" % effect
    sleep(5)
camera.stop_preview()

# ===========================================

# exposure mode: (default: auto)
'''
off
auto
night
nightpreview
backlight
spotlight
sports
snow
beach
verylong
fixedfps
antishake
fireworks
'''

camera.start_preview()
camera.exposure_mode = 'beach'
sleep(5)
camera.capture('/home/pi/Desktop/beach.jpg')
camera.stop_preview()

# to try all effects
camera.EXPOSURE_MODES

# ===========================================

# white balance: default auto
'''
off
auto
sunlight
cloudy
shade
tungsten
fluorescent
incandescent
flash
horizon
'''

camera.start_preview()
camera.awb_mode = 'sunlight'
sleep(5)
camera.capture('/home/pi/Desktop/sunlight.jpg')
camera.stop_preview()

# to try all effects
camera.AWB_MODES
# ===========================================
