#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 21:59:23 2023

@author: chloehage
"""

from flask import *
import sqlite3

# CrÃ©ation d'un objet application web Flask
app = Flask(__name__)

def cacher(image_front, image_back):
    """
    Cette fonction récupère les codes r,v,b de chaque pixel
    des deux images (image_front et image_back) et  les convertie
    en binaire pour les redistribuer et creer les pixels d'une troisième image
    (img_coder).
    """
    pixels_image = image_front.size
    img_coder = Image.new(mode="RGB", size=(pixels_image))
    for x in range(pixels_image[0]):
        for y in range(pixels_image[1]):
            # on récupère les pixels à la position x,y de image_front
            (r_fake, v_fake, b_fake) = image_front.getpixel((x, y))
            # conversion du code RVB en binaire
            r_wait = bin(r_fake)
            v_wait = bin(v_fake)
            b_wait = bin(b_fake)
            r_wait = str(r_wait[2:])
            v_wait = str(v_wait[2:])
            b_wait = str(b_wait[2:])
            if len(r_wait) < 8:
                r_wait = (8 - len(r_wait)) * "0" + r_wait
            if len(v_wait) < 8:
                v_wait = (8 - len(v_wait)) * "0" + v_wait
            if len(b_wait) < 8:
                b_wait = (8 - len(b_wait)) * "0" + b_wait
            # découpage du code RVB pour récupérer les 5 bits de point fort
            r_fort = r_wait[:5]
            v_fort = v_wait[:5]
            b_fort = b_wait[:5]
            # on récupère les pixels à la position x,y de image_back
            (r2_cacher, v2_cacher, b2_cacher) = image_back.getpixel((x, y))
            # conversion du code RVB en binaire
            r2_wait = bin(r2_cacher)
            v2_wait = bin(v2_cacher)
            b2_wait = bin(b2_cacher)
            r2_wait = str(r2_wait[2:])
            v2_wait = str(v2_wait[2:])
            b2_wait = str(b2_wait[2:])
            if len(r2_wait) < 8:
                r2_wait = (8 - len(r2_wait)) * "0" + r2_wait
            if len(v2_wait) < 8:
                v2_wait = (8 - len(v2_wait)) * "0" + v2_wait
            if len(b2_wait) < 8:
                b2_wait = (8 - len(b2_wait)) * "0" + b2_wait
            # découpage du code RVB pour récupérer les 3 bits de point faible
            r2_fort = r2_wait[:3]
            v2_fort = v2_wait[:3]
            b2_fort = b2_wait[:3]
            # on assemble les 5 bits de image_front et les 3 de image_back
            r = r_fort + r2_fort
            v = v_fort + v2_fort
            b = b_fort + b2_fort
            # assemblage du code RVB pour l'image finale
            list_pixel[0] = r
            list_pixel[1] = v
            list_pixel[2] = b
            # reconversion en décimal
            rconv = int(list_pixel[0], 2)
            vconv = int(list_pixel[1], 2)
            bconv = int(list_pixel[2], 2)
            # formation du pixel sur l'image finale
            img_coder.putpixel((x, y), (rconv, vconv, bconv))
    img_coder.save("img_code.bmp","BMP")
    img_coder.show()

@app.route("/stegano1")
def stegano1():
    """Affiche la page web"""
    return render_template("stegano.html")


@app.route("/stegano2")
def stegano2():
    return render_template("stegano2.html")

@app.route('/form', methods=['GET', 'POST'])
def form(): 
    if request.method == 'POST':
        email = request.form['email']
        destinataire = request.form['destinataire']

        connexion = sqlite3.connect('Data.db')
        curseur = connexion.cursor()
        curseur.execute('INSERT INTO Mail (TonMail, Destinataire) VALUES (?, ?)', (email, destinataire))
        connexion.close()
        return render_template('confirmation.html', dest=destinataire)
    else:
        return render_template('form.html')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1665, debug=True)