import sys
import time
import smbus
from flask import Flask, Response
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Gauge, Counter, generate_latest

from capture_trh import get_trh

app = Flask(__name__)
# metrics = PrometheusMetrics(app)

CONTENT_TYPE_LATEST = str('text/plain; version=0.0.4; charset=utf-8')

number_of_requests = Counter(
    'number_of_requests',
    'The number of requests, its a counter so the value can increase or reset to zero.'
)
temperature = Gauge("current_temperature", "temperature", ["server"])
humidity = Gauge("current_humidity", "humidity", ["server"])


i2c = smbus.SMBus(1)


@app.route("/metrics", methods=['GET'])
def return_trh():
    number_of_requests.inc()
    try:
        t, h = get_trh(i2c)
        print('温度={}℃  湿度={}%'.format(t, h))
        temperature.labels("raspi3").set(t)
        humidity.labels("raspi3").set(h)
    except Exception as e:
        print("ERROR: " + str(e))
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9999)
