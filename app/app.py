from flask import Flask, jsonify, request
import random, time

app = Flask(__name__)

@app.route("/score")
def score():
    error_mode = request.args.get("error", "false").lower() == "true"
    if error_mode:
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
    # Minimal Prometheus metrics
    return "# HELP app_requests_total Total requests\n# TYPE app_requests_total counter\napp_requests_total 1\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)