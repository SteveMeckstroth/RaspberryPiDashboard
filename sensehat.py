from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

red = (255,0,0)
blue = (0,0,255)
white = (255,255,255)
green = (0,255,0)
yellow = (255,255,0)

rotation = [0, 90, 180, 270]

while True:
        pressure = round(sense.get_pressure(),2)
        temp = round((sense.get_temperature() * (9/5)) + 32,1)
        humidity = round(sense.get_humidity(),2)
        message = f"Pressure: {pressure} Temp: {temp}F Humidity: {humidity}"
        if (temp < 120):
                color = blue
        elif (temp > 140):
                color = red
        else:
                temp = white

        sense.set_rotation(rotation[2])
        sense.show_message(message, scroll_speed=0.07, text_colour=color)
        sleep(0.1)
        sense.set_pixel(0, 0, (0, 0, 255))
        sense.set_pixel(0,7, blue)
        sense.set_pixel(7,0,blue)
        sense.set_pixel(7,7,blue)
        sleep(0.1)
        sense.clear((255,255,255))
