# imports
from pathlib import Path # pathlib : chemin de fichiers
import shutil # déplacement de fichiers

p_tri = Path.home() / "OneDrive"/ "Documentos" / "Projet1_Trieur_de_fichier" / "dossier-tri" # chemin dossier tri
p_test = Path.home() / "OneDrive"/ "Documentos" / "Projet1_Trieur_de_fichier" / "dossier-test" # chemin dossier test
fichiers = [f for f in p_test.iterdir() if f.is_file()] # récupération des fichiers du dossier test grâce à la méthode iterdir()
categories = {"Images" : [".jpg", ".png", ".gif" ], "Documents" : [".pdf", ".docx", ".txt"], "Audio": [".mp3", ".wav"], "Vidéos" : [".mp4"], "Archives" : [".zip"], "Code" : [".py"], "Autres" : []}

def tri():
    nettoyage()
    creation_sous_dossier()
    with open("rapport.txt", "w", encoding="utf-8") as rapport: # création du fichier de rapport
        for f in fichiers:
            for cat in categories:
                if f.suffix.lower() in categories[cat]:
                    source = p_test / f.name # Là ou est le fichier initialement (donc dans dossier_test)
                    destination = p_tri / cat / f.name # là ou sera le fichier à la fin (donc dans dossier-tri) 
                    destination = doublons(f, cat, False, destination)
                    shutil.move(source, destination) # déplacement de fichier
                    rapport.write(f"{f.name} => {cat} \n")
                    break
            else:
                source = p_test / f.name
                destination = p_tri / "Autres" / f.name
                destination = doublons(f, cat, True, destination)
                shutil.move(source, destination)
                rapport.write(f"{f.name} => Autres \n")

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