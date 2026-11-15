# imports
from pathlib import Path # pathlib : chemin de fichiers
import shutil # déplacement de fichiers
import csv
from datetime import datetime

p_tri = Path(input("Dossier de destination : ")) # chemin dossier tri
p_test = Path(input("Dossier à trier : ")) # chemin dossier test
fichiers = [f for f in p_test.iterdir() if f.is_file()] # récupération des fichiers du dossier test grâce à la méthode iterdir()
categories = {"Images" : [".jpg", ".png", ".gif" ], "Documents" : [".pdf", ".docx", ".txt"], "Audio": [".mp3", ".wav"], "Vidéos" : [".mp4"], "Archives" : [".zip"], "Code" : [".py"], "Autres" : []}

def tri():
    nettoyage()
    creation_sous_dossier()
    with open("rapport.csv", "w", newline="", encoding="utf-8-sig") as fichier_rapport: # création du fichier de rapport
        rapport = csv.writer(fichier_rapport, delimiter=";")
        rapport.writerow(["nom", "type", "taille (octets)", "date", "nouveau chemin"])
        for f in fichiers:
            if not p_test.is_dir():
                        rapport.write("Le dossier test n'existe pas")
                        break
            for cat in categories:
                if f.suffix.lower() in categories[cat]:
                    source = p_test / f.name # Là ou est le fichier initialement (donc dans dossier_test)
                    destination = p_tri / cat / f.name # là ou sera le fichier à la fin (donc dans dossier-tri) 
                    destination = doublons(f, cat, False, destination)
                    shutil.move(source, destination) # déplacement de fichier
                    infos = destination.stat()
                    rapport.writerow([ # rédaction du fichier
                         destination.name,
                         cat,
                         infos.st_size,
                         datetime.fromtimestamp(infos.st_mtime).strftime("%Y-%m-%d %H:%M"),
                         destination,
                    ])
                    break
            else:
                source = p_test / f.name
                destination = p_tri / "Autres" / f.name
                destination = doublons(f, cat, True, destination)
                shutil.move(source, destination)
                infos = destination.stat()
                rapport.writerow([ # rédaction du fichier
                                         destination.name,
                                         cat,
                                         infos.st_size,
                                         datetime.fromtimestamp(infos.st_mtime).strftime("%Y-%m-%d %H:%M"),
                                         destination,
                                    ])

# créer les sous dossiers Images, Archives ...
def creation_sous_dossier():
    for doc in categories.keys():
        sous_dossier = p_tri / doc
        sous_dossier.mkdir(exist_ok=True)

# Nettoyer le contenu des sous-dossiers avant le tri
def nettoyage():
    for f in p_tri.rglob("*"): # rglob : prend en compte ce qui a à l'intérieur des sous dossiers
        if f.is_file():
            f.unlink() # supprimer les fichiers
def doublons(f, cat, isAutre, destination):
    i = 1
    while destination.exists():  # Gérer les doublons :  SI fichier (1).txt existe alors on rename fichier en fichier (2).txt
        if isAutre:
            destination = p_tri / "Autres" / (f.stem + f" ({i})" + f.suffix)
        else:
            destination = p_tri / cat / (f.stem + f" ({i})" + f.suffix)
        i += 1
    return destination

tri()