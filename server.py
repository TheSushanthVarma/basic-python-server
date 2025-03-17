from waitress import serve
from app import app
import os
import ngrok

if __name__ == '__main__':
    # Get port from environment variable or use 8080 as default
    port = int(os.environ.get('PORT', 8080))
    
    # Start ngrok tunnel
    public_url = ngrok.connect(port).public_url
    print(f"ngrok tunnel created at: {public_url}")
    
    print(f"Starting server on port {port}...")
    serve(app, host='0.0.0.0', port=port) 