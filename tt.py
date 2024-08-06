#!/usr/bin/python3

import json
import requests

if __name__ == "__main__":
    r = requests.get("http://0.0.0.0:5000/api/v1/status")
    print(r.headers.get("Content-Type").lower())
