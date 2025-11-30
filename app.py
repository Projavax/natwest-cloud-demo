from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # This is what the user sees when they visit the website
    return "Hello NatWest! This app is running inside a Docker container."

if __name__ == '__main__':
    # '0.0.0.0' means it listens on all public IPs, which is required for Docker
    app.run(host='0.0.0.0', port=5001)