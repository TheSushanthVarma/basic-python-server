from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Hello, World!",
        "status": "success"
    })

@app.route('/health')
def health():
    return jsonify({
        "status": "healthy"
    })

# This is only used when running with Flask's development server
if __name__ == '__main__':
    app.run(debug=True) 