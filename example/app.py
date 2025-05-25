from flask import Flask, Response
from prometheus_client import Counter, Histogram, generate_latest

app = Flask(__name__)

REQUEST_COUNT = Counter("http_requests_total", "Total HTTP requests")
REQUEST_LATENCY = Histogram("http_request_duration_seconds", "Request latency")

@app.route("/")
@REQUEST_LATENCY.time()
def homepage():
    REQUEST_COUNT.inc()
    return "Hello, SRE World!"

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
