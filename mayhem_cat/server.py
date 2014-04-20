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
            twat = f.read()
    except IOError:
        twat = "No tweets! What??"

    return render_template("index", twat = twat)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8080)