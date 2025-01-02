# Import modules
from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

@app.route("/task3", methods=["GET"])
def home():
    if request.method == "GET":
        data = [
            {
                "color": "purple",
                "type": "minivan",
                "registration": datetime(2017, 1, 3).strftime('%Y-%m-%d'),
                "capacity": 7
            },
            {
                "color": "red",
                "type": "station wagon",
                "registration": datetime(2018, 3, 3).strftime('%Y-%m-%d'),
                "capacity": 5
            }
        ]
        return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, port=6000)
