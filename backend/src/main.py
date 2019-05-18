#!/usr/bin/env python3
"""
main.py - Run the complete application.
"""

from app import create_app
# from db import create_db
# from api import api
from views import views
# from models import *

def main():
    """Run application
    """
    app = create_app()
    # db = create_db()
    # db.create_tables()
    # app.register_blueprint(api)
    app.register_blueprint(views)
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__=="__main__":
    main()
