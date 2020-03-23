from sense_hat import SenseHat
from time import sleep
from flask import Flask
app = Flask(__name__)
sense = SenseHat()

red = (255,0,0)
blue = (0,0,255)
white = (255,255,255)
green = (0,255,0)
yellow = (255,255,0)

rotation = [0, 90, 180, 270]

@app.route("/")
def hello():
    pressure = round(sense.get_pressure(),2)
    temp = round((sense.get_temperature() * (9/5)) + 32,1)
    humidity = round(sense.get_humidity(),2)
    
    html = """<html>
            <head>
            <script>
            setTimeout(function() {
                    location.reload();
            }, 30000);
            </script>
            </head>
            <body>
            <div><p><h1>Temp: """
    html += str(temp)
    html += """</h1></p>
                <p><h1>Pressure: """
    html += str(pressure)
    html += """</h1></p>
                <p><h1>Humidity: """
    html += str(humidity)
    html += """</h1></p>
            </div>
            </body>
            </html>"""
    return html

if __name__ == "__main__":
        app.run(host='0.0.0.0')
