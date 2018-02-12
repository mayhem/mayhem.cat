#!/usr/bin/env python

import os
import json
from flask import Flask, render_template

STATIC_PATH = "/static"
STATIC_FOLDER = "static"
TEMPLATE_FOLDER = "templates"

app = Flask(__name__,
            static_url_path = STATIC_PATH,
            static_folder = STATIC_FOLDER,
            template_folder = TEMPLATE_FOLDER)

@app.route('/')
def index():
    try:
        with open(os.path.join(TEMPLATE_FOLDER, "content.json"), "r") as f:
            d = f.read()
            content = json.loads(d)
    except IOError:
        content = {}
    return render_template("index", content=content)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8081)
