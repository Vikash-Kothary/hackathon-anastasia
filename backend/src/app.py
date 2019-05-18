#!/usr/bin/env python3
"""
app.py - Create web server
"""

from flask import Flask


def create_app():
    """Initialise flask web server
    """
    app = Flask(__name__, static_folder="./models", static_url_path="")
    return app
