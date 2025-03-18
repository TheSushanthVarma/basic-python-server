import ngrok

# Replace 'YOUR_AUTHTOKEN' with your actual ngrok authtoken
def setup_ngrok():
    # You can get your authtoken from https://dashboard.ngrok.com/get-started/your-authtoken
    ngrok.set_auth_token('') 
