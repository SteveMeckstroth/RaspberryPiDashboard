from sense_hat import SenseHat
from time import sleep
from flask import Flask
app = Flask(__name__)
sense = SenseHat()

@app.route("/")
def hello():
    pressure = round(sense.get_pressure(),2)
    temp = round((sense.get_temperature() * (9/5)) + 32,1)
    humidity = round(sense.get_humidity(),2)
    message = "Pressure: {pressure} Temp: {temp}F Humidity: {humidity}".format(pressure, temp, humidity)
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
    return """
<html>
<head>
<script>
setTimeout(function() {
        location.reload();
}, 30000);
</script>
</head>
<body>
<div><p><h1>Temp: {temp}</h1></p>
    <p><h1>Pressure: {pressure}</h1></p>
    <p><h1>Humidity: {humidity}</h1></p>
</div>
</body>
</html>

""".format(temp, pressure, humidity)

if __name__ == "__main__":
        app.run(host='0.0.0.0')