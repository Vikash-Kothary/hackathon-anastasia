#!/usr/bin/env python3
"""
app.py - Create web server
"""

from flask import Flask, jsonify
import json

app = Flask(__name__, static_folder="./models", static_url_path="")

@app.route('/data.json')
def api():
    
    with open('./src/data/data.json') as file:
        data = json.load(file)
    data = str(data)
    return jsonify(dict(tiles=data))

app.run(host='0.0.0.0', port='5000')