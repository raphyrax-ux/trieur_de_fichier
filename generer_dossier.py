# imports
from pathlib import Path # pathlib : chemin de fichiers
import random # random : créer aléatoirement des fichiers
import shutil # shultil : mémoire

# création des fichiers de test
noms = ["photo", "vacances", "rapport", "facture", "cv", "musique", "chanson", "film", "notes",
"budget", "projet","cours", "image", "scan", "archive", "backup", "data", "script", "devoir", "recette"]
extensions = [".jpg", ".JPG", ".png", ".PNG", ".gif", ".pdf", ".PDF", ".docx", ".txt", ".mp3", ".Mp3", ".wav", ".mp4", ".zip", ".py"]
pieges = ["PHOTO.JPG", "Song.Mp3", "Rapport.PdF", "FACTURE.pdf", "README", "Makefile", ".gitignore", ".env", 
"fichier.xyz", "fichier.", "notes.motuncroyablementlong", "video.mp4a", "backup.7z", "archive.tar.gz", "rapport.final.pdf", 
"projet.v2.docx", "fichier..txt", "mes vacances.jpg", "événement.png", "budget (copie).pdf", "cv-final_2.docx", "2024.pdf", "rapport.pdf", "rapport.docx", "photo.jpg", "PHOTO.JPG"]
p = Path.home() / "OneDrive"/ "Documentos" / "Projet1_Trieur_de_fichier" / "dossier-test" # chemin des dossiers

for element in p.iterdir():
    if element.is_dir():
        shutil.rmtree(element)
    else:
        element.unlink()

for i in range(len(noms)):
    hasard = random.choice(extensions) 
    Path(p / (noms[i] + hasard)).touch() # On créé chaque fichier de test
for i in range(len(pieges)):
    Path(p / pieges[i]).touch() # On rajoute les fichiers "pièges"