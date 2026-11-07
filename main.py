# imports
from pathlib import Path # pathlib : chemin de fichiers

p_tri = Path.home() / "OneDrive"/ "Documentos" / "Projet1_Trieur_de_fichier" / "dossier-tri" # chemin dossier tri
p_test = Path.home() / "OneDrive"/ "Documentos" / "Projet1_Trieur_de_fichier" / "dossier-test" # chemin dossier test
fichiers = [f for f in p_test.iterdir() if f.is_file()] # récupération des fichiers du dossier test grâce à la méthode iterdir()
categories = {"Images" : [".jpg", ".png", ".gif" ], "Documents" : [".pdf", ".docx", ".txt"], "Audio": [".mp3", ".wav"], "Vidéos" : [".mp4"], "Archives" : [".zip"], "Code" : [".py"], "Autres" : []}

def main():
    with open("rapport.txt", "w", encoding="utf-8") as rapport:
        for f in fichiers:
            for cat in categories:
                print(f.suffix.lower())
                if f.suffix.lower() in categories[cat]:
                    rapport.write(f"{f.name} => {cat} \n")
                    break
            else:
                rapport.write(f"{f.name} => Autres \n")

main()