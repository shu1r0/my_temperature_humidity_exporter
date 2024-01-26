import smbus
from flask import Flask, Response
from prometheus_client import Gauge, Counter, generate_latest

from .capture_trh import get_trh

app = Flask(__name__)

CONTENT_TYPE_LATEST = str("text/plain; version=0.0.4; charset=utf-8")

number_of_requests = Counter("number_of_requests", "The number of requests")
temperature = Gauge("current_temperature", "temperature", ["server"])
humidity = Gauge("current_humidity", "humidity", ["server"])


i2c = smbus.SMBus(1)


@app.route("/metrics", methods=["GET"])
def return_trh():
    number_of_requests.inc()
    try:
        # t, h = get_trh(i2c)
        t, h = (20, 60)
        print("温度={}℃  湿度={}%".format(t, h))
        temperature.labels("raspi3").set(t)
        humidity.labels("raspi3").set(h)
    except Exception as e:
        print("ERROR: " + str(e))
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
