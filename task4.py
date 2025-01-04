#import modules
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/task4", methods=["GET"])
def home():
    if(request.method=="GET"):
        return jsonify({"numbers": [40, 100, 1, 5, 25, 10]})


if __name__ == "__main__":
    app.run(debug=True, port=7000)