import RPi.GPIO as GPIO
from flask import Flask

app = Flask(__name__)

LIGHT_GPIO = 9
BIG_LIGHT_GPIO = 2

GPIO.setmode(GPIO.BCM)

GPIO.setup(LIGHT_GPIO, GPIO.OUT)
GPIO.setup(BIG_LIGHT_GPIO, GPIO.OUT)

@app.route("/toggle")
def small_light():
    if GPIO.input(LIGHT_GPIO):
        GPIO.output(LIGHT_GPIO, GPIO.LOW)
    else:
        GPIO.output(LIGHT_GPIO, GPIO.HIGH)

    return "done"

@app.route("/toggle_big")
def big_light():
    if GPIO.input(BIG_LIGHT_GPIO):
        GPIO.output(BIG_LIGHT_GPIO, GPIO.LOW)
    else:
        GPIO.output(BIG_LIGHT_GPIO, GPIO.HIGH)

    return "done"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
