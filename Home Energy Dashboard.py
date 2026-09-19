from flask import Flask, render_template, jsonify
from energy_monitor import get_energy_data

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/energy")
def energy():
    return jsonify(get_energy_data())


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
