import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/health")
def health():
    return jsonify(status="ok", version=os.environ.get("APP_VERSION", "dev"))

@app.route("/hello/<name>")
def hello(name):
    return f"Hello {name} !"