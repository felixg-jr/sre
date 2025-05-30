🧪 What Is Flask?

Flask is a lightweight web framework for Python that lets you build web applications and APIs easily.

Think of it like:

🧱 “Lego blocks for building web apps in Python — you only use what you need.”

🧭 Why SREs Use Flask in Labs and Demos
	•	It’s perfect for mocking up a web service to simulate traffic, latency, or expose metrics.
	•	It makes it easy to integrate Prometheus metrics using the prometheus_client library.
	•	You can write a working app in just 10 lines of Python.

How to high frequency requests?

Open a terminal and run this to simulate high-frequency requests:

while true; do curl -s http://localhost:8000 > /dev/null; done

Let it run for 10–20 seconds to generate steady traffic into Prometheus' recent [1m] window.

🛠 Why It Matters for You

As an SRE:
	•	You often need to simulate services to test observability, metrics, alerting, etc.
	•	Flask lets you do that without waiting on devs or needing a full stack.
	•	It’s great for building throwaway apps for testing dashboards, error rates, SLOs, and latency thresholds.

This mock demo gives you
1. Real http_requests_total metrics (used for availability SLIs)
2. Real http_request_duration_seconds metrics (used for latency SLIs)
