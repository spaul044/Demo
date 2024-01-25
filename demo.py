""" Dèmonstration Interface Graphique """
import sys
#pylint: disable=global-statement, unused-import, c-extension-no-member, no-name-in-module
#pylint: disable=invalid-name, f-string-without-interpolation, line-too-long
import locale
from datetime import date
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtGui import QIcon, QPixmap, QPainter, QTextDocument
from PySide6.QtUiTools import QUiLoader

locale.setlocale(locale.LC_ALL, 'fr')

loader = QUiLoader()
app = QtWidgets.QApplication(sys.argv)
window = loader.load("demo.ui", None)
window.setWindowTitle("Demo")

count = 0

def mettre_a_jour_papillon():
    """ mettre a jour l'image du boutn Ogre """
    global count
    t_val = ["Papillon 1", "Papillon 2", "Papillon 3", "Papillon 4"]
    l_val = ["Papillon 1.JPG", "Papillon 2.JPG", "Papillon 3.JPG", "Papillon 4.JPG"]
    u_val = ["https://www.pexels.com/photo/blue-and-black-butterfly-on-green-leaves-89770/",
             "https://www.pexels.com/photo/gray-and-black-butterfly-sniffing-white-flower-91946/",
             "https://www.pexels.com/photo/close-up-shot-of-a-butterfly-206770/",
             "https://www.pexels.com/photo/macro-photography-of-spicebush-swallowtail-butterfly-1385761/"]
    hyperlien = f" <a href=\"{u_val[count]}\"> <font color=blue> {u_val[count]}</font> </a>"
    window.bouton_papillon.setIcon(QIcon(l_val[count]))
    window.texte_papillon.setText(t_val[count])
    window.url_papillon.setText(hyperlien)
    count += 1
    count = count%len(l_val)

def mettre_a_jour_glisseur():
    """ mettre a jour les couleurs des glisseurs """
    valeur_bleu  = window.glisseur_bleu.value()
    valeur_rouge = window.glisseur_rouge.value()
    valeur_vert  = window.glisseur_vert.value()

    window.texte_bleu.setText(f"Bleu ({valeur_bleu})")
    window.texte_rouge.setText(f"Rouge ({valeur_rouge})")
    window.texte_vert.setText(f"Vert ({valeur_vert})")

    couleur  = f"background:rgb({valeur_rouge},{valeur_vert},{valeur_bleu})"
    window.texte_couleur.setStyleSheet(couleur)

def mettre_a_jour_histoire():
    """ mettre a jour l'histoire """
    heros = window.ligne_heros.text()
    nombre_amis = window.compteur_amis.value()
    date_depart = window.date_depart.date()
    date_texte = QtCore.QLocale("fr")
    heure_gouter = window.heure_gouter.time()
    heure_texte  = heure_gouter.toString("HH:mm")
    temperature = window.cadrant_temperature.value()

    texte = f"<br>Notre héros <b>{heros}</b> part à l'aventure.</br><br></br>"
    texte += f"<br>Il a <b>{nombre_amis}</b> amis qui l\'accompagnent.</br><br></br>"
    texte += f"<br>Il part le <b>{date_texte.toString(date_depart)}</b></br><br></br>"
    texte += f"<br>mais, il doit rentrer avant <b>{heure_texte}</b></br><br></br>"
    texte += f"<br>sinon, il manquera le goûter.</br><br></br>"
    texte += f"<br>La température est de <b>{temperature}</b> degré Celcius.</br><br></br>"

    window.texte_histoire.setText(texte)

    texte_temperature = f"Température ({temperature})"
    window.texte_temperature.setText(texte_temperature)

#Initialiser le papillon, l'histoire et les couleurs au début du programe
mettre_a_jour_papillon()
mettre_a_jour_histoire()
mettre_a_jour_glisseur()


#Initialiser le lien entre les clics et les fonctions
window.bouton_papillon.clicked.connect(mettre_a_jour_papillon)

window.glisseur_bleu.valueChanged.connect(  mettre_a_jour_glisseur)
window.glisseur_rouge.valueChanged.connect( mettre_a_jour_glisseur)
window.glisseur_vert.valueChanged.connect(  mettre_a_jour_glisseur)

window.ligne_heros.textEdited.connect(           mettre_a_jour_histoire)
window.compteur_amis.valueChanged.connect(       mettre_a_jour_histoire)
window.cadrant_temperature.valueChanged.connect( mettre_a_jour_histoire)
window.heure_gouter.timeChanged.connect(         mettre_a_jour_histoire)
window.date_depart.dateChanged.connect(          mettre_a_jour_histoire)


window.show()
app.exec()
