from flask import Flask, jsonify, make_response

app = Flask(__name__)

def add_cors_headers(response):
    # Add headers to handle ngrok browser warning
    response.headers['ngrok-skip-browser-warning'] = 'true'
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

@app.route('/')
def home():
    response = make_response(jsonify({
        "message": "Hello, World!",
        "status": "success"
    }))
    return add_cors_headers(response)

@app.route('/health')
def health():
    response = make_response(jsonify({
        "status": "healthy"
    }))
    return add_cors_headers(response)

# This is only used when running with Flask's development server
if __name__ == '__main__':
    app.run(debug=True) 