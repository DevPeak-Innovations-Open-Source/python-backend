#import modules
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/post1", methods=["POST"])
def home():
    if(request.method=="POST"):
        print(request.json)
        return jsonify({"message": request.json})


if __name__ == "__main__":
    app.run(debug=True, port=2200)