from flask import Flask, jsonify
import os

app = Flask(__name__)

def generate_nonce():
    serial = int.from_bytes(os.urandom(10), byteorder="big")
    print (serial)
    return serial

@app.route("/",  methods=["POST"])
def index():
    return jsonify(message = "Welcome to eth signin, please sign this message to confirm.", nonce = int(generate_nonce()))