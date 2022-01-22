from flask import Flask, jsonify
import os

app = Flask(__name__)

def generate_nonce():
    serial = int.from_bytes(os.urandom(10), byteorder="big")
    print (serial)
    return serial

@app.route("/", methods=["GET"])
def index():
    return jsonify(serial = int(generate_nonce()))