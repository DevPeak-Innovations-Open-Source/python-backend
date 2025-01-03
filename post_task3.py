#One should take only string (not a JSON)
from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to handle HTML data
@app.route('/post_task3', methods=['POST'])
def handle_html():
    data = request.data.decode('utf-8')  # Parse raw HTML data
    return f"<h2>HTML Received:</h2><div>{data}</div>", 200, {'Content-Type': 'text/html'}
    
if __name__ == "__main__":
    app.run(debug=True, port=2201)