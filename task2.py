#import modules
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/task2", methods=["GET"])
def home():
    if(request.method=="GET"):
        return jsonify({"cars": ["Saab", "Volvo", "BMW"]})


if __name__ == "__main__":
    app.run(debug=True, port=8000)