#POST Request in Python API
#One should take keys as JSON
from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to handle JSON data
@app.route('/post_task1', methods=['POST'])
def handle_json():
    data = request.get_json()  # Parse JSON data
    return jsonify({
        "message": "JSON received successfully!",
        "data": data
    })
    
if __name__ == "__main__":
    app.run(debug=True, port=2201)