#!/usr/bin/python3
"""
A Flask applicaton
"""

from flask import Flask
import storage
import models
from api.v1.views import app_views

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def storage_close():
    """
    calls the storage.calls method
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, threaded=True)
