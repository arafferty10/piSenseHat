from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#Basic Color Definitions
blue = (0, 0, 255)
red = (255, 0, 0)

#Setting Individual Pixels
# sense.set_pixel(0, 2, blue)
# sense.set_pixel(7, 4, red)

# sense.set_pixel(2, 2, (0, 0, 255))
# sense.set_pixel(4, 2, (0, 0, 255))
# sense.set_pixel(3, 4, (100, 0, 0))
# sense.set_pixel(1, 5, (255, 0, 0))
# sense.set_pixel(2, 6, (255, 0, 0))
# sense.set_pixel(3, 6, (255, 0, 0))
# sense.set_pixel(4, 6, (255, 0, 0))
# sense.set_pixel(5, 5, (255, 0, 0))

#Rotating image
w = (150, 150, 150)
b = (0, 0, 255)
e = (0, 0, 0)

image = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
w,w,w,e,e,w,w,w,
w,w,b,e,e,w,w,b,
w,w,w,e,e,w,w,w,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

sense.set_pixels(image)

while True:
    sleep(1)
    sense.flip_h()
