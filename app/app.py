from flask import Flask, jsonify, request, Response
import random, time
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

# Metrics
REQUEST_COUNTER = Counter('app_requests_total', 'Total requests to /score')
ERROR_COUNTER = Counter('app_errors_total', 'Total simulated errors')

@app.route("/score")
def score():
    REQUEST_COUNTER.inc()  # Increment total requests

    error_mode = request.args.get("error", "false").lower() == "true"
    if error_mode:
        ERROR_COUNTER.inc()  # Increment error counter
        return jsonify({"error": "Simulated failure"}), 500

    return jsonify({
        "home_team": "Raptors",
        "away_team": "Lakers",
        "home_score": random.randint(50, 120),
        "away_score": random.randint(50, 120),
        "timestamp": time.time()
    })

@app.route("/metrics")
def metrics():
    # Return Prometheus metrics
    return Response(generate_latest(), mimetype='text/plain')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)