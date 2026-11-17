from flask import Flask, jsonify
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Docker AWS Project</title>
    </head>
    <body style="font-family: Arial; text-align:center; padding:50px;">
        <h1>Welcome to My Docker Project!</h1>
        <h2>Successfully Deployed on AWS EC2</h2>
        <p>Application: Python Flask</p>
        <p>Containerized using Docker</p>
        <p>Infrastructure: AWS EC2</p>
    </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "hostname": socket.gethostname()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
