#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 21:59:23 2023

@author: chloehage
"""

from flask import *
from PIL.Image import *
from PIL import Image

# CrÃ©ation d'un objet application web Flask
app = Flask(__name__)

@app.route("/stegano1")
def stegano1():
    """Affiche la page web"""
    return render_template("stegano.html")

@app.route("/stegano2")
def stegano2():
    return render_template("stegano2.html")

@app.route("/form")
def form():
    return render_template("form.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1665, debug=True)