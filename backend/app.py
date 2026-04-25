from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return {"message": "Backend is running"}

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    print("Received:", data)

    return jsonify({
    "message": f"Received {data.get('name')} with email {data.get('email')}"
})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)