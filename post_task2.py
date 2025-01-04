#One should take only string (not a JSON)
from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to handle plain string data
@app.route('/post_task2', methods=['POST'])
def handle_string():
    data = request.data.decode('utf-8')  # Parse raw string data
    return jsonify({
        "message": "String received successfully!",
        "data": data
    })
    
if __name__ == "__main__":
    app.run(debug=True, port=2201)