from flask import Flask, jsonify, request

app = Flask(__name__)


#This is in context if we want to Delete a json formatted dataset
@app.route('/delete-intro', methods=['DELETE'])
def delete_intro():
    data = request.get_json()  # Parse JSON data
    return jsonify({
        "message": "JSON data deleted successfully!",
        "data": data
    })


if __name__ == "__main__":
    app.run(debug=True, port=3301)