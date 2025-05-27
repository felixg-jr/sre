from flask import Flask, Response
from prometheus_client import Counter, Histogram, generate_latest
import random
import time

app = Flask(__name__)

REQUEST_COUNT = Counter("http_requests_total", "Total HTTP requests", ["method", "endpoint", "status"])
REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "Request latency",
    buckets=[0.005, 0.01, 0.025, 0.05, 0.1, 0.2, 0.3, 0.5, 1, 2.5, 5, 10]
)

@app.route("/")
@REQUEST_LATENCY.time()
def homepage():
    status_code = 200
    if random.random() < 0.3: # 30% of the time
        time.sleep(0.5) # Delay for 500ms
    REQUEST_COUNT.labels(method="GET", endpoint="/", status=str(status_code)).inc()
    return "Hello, SRE World!", status_code

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
