from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/put-intro/<merc>", methods=["PUT"])
def put_intro(merc):
    if request.method == "PUT":
        print(merc, request.json)
        return jsonify({"message": merc})



if __name__ == "__main__":
    app.run(debug=True, port=3300)