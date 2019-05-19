#!/usr/bin/env python3
"""
config.py -
"""

import os

ENVIRONMENT = os.getenv('ENVIRONMENT', '')

SESSION_FILE_DIR = os.getenv('SESSION_FILE_DIR', '/tmp')