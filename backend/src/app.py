#!/usr/bin/env python3
"""
app.py - Create web server
"""

from flask import Flask, session, jsonify
#from flask.ext.session import Session
import json

app = Flask(__name__, static_folder="./models", static_url_path="")
#SESSION_TYPE = 'filesystem'
#app.config.from_object(__name__)
#sess = Session()
#sess.init_app(app)

@app.route('/')
def api():
    with open('./src/models/tiles.json') as file:
        data = json.load(file)
    return jsonify(data)

app.run(host='0.0.0.0', port='5000', debug=True)