#!/usr/bin/env python
"""
views.py - Serve webpages
"""

from flask import Blueprint

views = Blueprint('views', __name__)


@views.route('/')
def root():
    """Root page
    """
    return 'Hello World'
