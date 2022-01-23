from flask import Flask, jsonify, request, redirect, url_for
import os

app = Flask(__name__)

def generate_nonce():
    serial = int.from_bytes(os.urandom(10), byteorder="big")
    print (serial)
    return serial

#@app.route("/",  methods=['GET','POST'])
#def post():
#    if request.method=='POST':
#        return jsonify(message = "Welcome to eth signin, please sign this message to confirm.", nonce = int(generate_nonce()))

@app.route('/nonce',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nonce']
      return jsonify(message = "Welcome to eth signin, please sign this message to confirm.", nonce = int(generate_nonce()))
      
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

@app.route("/",  methods=['GET'])
def index():
    return jsonify(nonce = int(generate_nonce()))