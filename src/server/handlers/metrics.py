# External modules
from flask import Response
from prometheus_client import Gauge, generate_latest, CONTENT_TYPE_LATEST


example_gauge = Gauge(
    "example_metric",
    "Example Metric Description",
    [
        "example_metric_lable1",
        "example_metric_lable2",
    ],
)

def handler():
    generate_gauges()
    data = generate_latest()
    resp = Response(data)
    resp.headers["Content-Type"] = CONTENT_TYPE_LATEST
    resp.headers["Content-Length"] = str(len(data))
    resp.status = "OK"
    resp.status_code = 200
    return resp

def generate_gauges():
    example_gauge.labels("example_val_1", "example_val_2").set(999)
