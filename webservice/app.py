from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    message = os.getenv('SERVICE_MESSAGE', 'Default message')
    return f"<h1>{message}</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
