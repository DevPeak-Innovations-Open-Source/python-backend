#import modules
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/drishya", methods=["GET"])
def home():
    if(request.method=="GET"):
        return jsonify({"message": "Hello, World!"})


if __name__ == "__main__":
    app.run(debug=True,port=5000)