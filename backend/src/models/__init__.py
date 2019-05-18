#!/usr/bin/env python
"""
views.py - Serve webpages
"""

from flask import Blueprint, redirect, url_for

models = Blueprint('models', __name__)


@models.route('/status')
def status():
    """Root page
    """
    return redirect(url_for('tiles.json'))
