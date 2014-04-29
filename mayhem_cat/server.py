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

    images = {}
    try:
        with open(os.path.join(config.CACHE_DIR, "mayhem_url"), "r") as f:
            mayhem_url = f.readline().strip()
            mayhem_l = int(f.readline().strip())
        images['mayhem'] = { 'landscape' : mayhem_l, 'url' : mayhem_url }
    except IOError:
        pass

    try:
        with open(os.path.join(config.CACHE_DIR, "hair_url"), "r") as f:
            hair_url = f.readline().strip()
            hair_l = int(f.readline().strip())
        images['hair'] = { 'landscape' : hair_l, 'url' : hair_url }
    except IOError:
        pass

    return render_template("index", twat = twat, images = images)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)
