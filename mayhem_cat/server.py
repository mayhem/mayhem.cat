#!/usr/bin/env python

import os
from flask import Flask, render_template
import config

STATIC_PATH = "/static"
STATIC_FOLDER = "../static"
TEMPLATE_FOLDER = "../templates"

app = Flask(__name__,
            static_url_path = STATIC_PATH,
            static_folder = STATIC_FOLDER,
            template_folder = TEMPLATE_FOLDER)

@app.route('/')
def index():
    try:
        with open(os.path.join(config.CACHE_DIR, "twat"), "r") as f:
            twat = f.read().strip()
    except IOError:
        twat = "No tweets! What??"

    try:
        with open(os.path.join(config.CACHE_DIR, "mayhem_url"), "r") as f:
            mayhem_url = f.read().strip()
    except IOError:
        mayhem_url = ""

    try:
        with open(os.path.join(config.CACHE_DIR, "hair_url"), "r") as f:
            hair_url = f.read().strip()
    except IOError:
        hair_url = ""

    return render_template("index", twat = twat, hair_url = hair_url, mayhem_url = mayhem_url)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
