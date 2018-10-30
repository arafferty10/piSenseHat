from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
# sense.clear()

#Basic Color Definitions
# blue = (0, 0, 255)
# red = (255, 0, 0)

#Setting Individual Pixels
#-----------------------------------------------
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
#-----------------------------------------------

#Rotating image
#-----------------------------------------------
# w = (150, 150, 150)
# b = (0, 0, 255)
# e = (0, 0, 0)
#
# image = [
# e,e,e,e,e,e,e,e,
# e,e,e,e,e,e,e,e,
# w,w,w,e,e,w,w,w,
# w,w,b,e,e,w,w,b,
# w,w,w,e,e,w,w,w,
# e,e,e,e,e,e,e,e,
# e,e,e,e,e,e,e,e,
# e,e,e,e,e,e,e,e
# ]
#
# sense.set_pixels(image)
#
# while True:
#     sleep(1)
#     sense.flip_h()
#-----------------------------------------------

#Smiley Pixels :)
#-----------------------------------------------
# Define some colours
g = (0, 255, 0) # Green
b = (0, 0, 0) # Black
w = (255, 255, 255) #White
u = (0, 0, 255) #Blue

# Set up where each colour will display
smile_pixels = [
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, u, u, g, g, u, u, g,
    g, u, u, g, g, u, u, g,
    g, g, g, g, g, g, g, g,
    g, u, g, g, g, g, u, g,
    g, g, u, u, u, u, g, g,
    g, g, g, g, g, g, g, g
]

# Display these colours on the LED matrix
sense.set_pixels(smile_pixels)
#-----------------------------------------------

#Enviornment sensor readings
#-----------------------------------------------
# pressure = sense.get_pressure()
# temp = sense.get_temperature()
# humid = sense.get_humidity()
#
# print "\nPressure: {0:.2f} Millibars\n".format(pressure)
# print "Temperature: {0:.2f} Celsius\n".format(temp)
# print "Humidity: {0:.2f}%\n".format(humid)

#-----------------------------------------------

#Create Scrolling text display of Enviornmental sensors
#-----------------------------------------------
while True:

  # Take readings from all three sensors
  t = sense.get_temperature()
  p = sense.get_pressure()
  h = sense.get_humidity()

  # Round the values to one decimal place
  t = round(t, 1)
  p = round(p, 1)
  h = round(h, 1)

  # Create the message
  # str() converts the value to a string so it can be concatenated
  message = "Temperature: " + str(t) + "C...  " + " Pressure: " + str(p) + "mB...  " + " Humidity: " + str(h) + "%"

  # Display the scrolling message
  sense.show_message(message, scroll_speed=0.05)
  #-----------------------------------------------
