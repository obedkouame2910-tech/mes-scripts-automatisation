import os
import shutil

# Définissez le dossier à organiser (remplacez par le chemin de votre choix)
DOSSIER_CIBLE = r"C:\Users\NomUtilisateur\Downloads"

# Dictionnaire des extensions et de leurs dossiers de destination correspondants
EXTENSIONS_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx", ".csv"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Archives": [".zip", ".rar", ".7z"],
    "Programmes": [".exe", ".msi"]
}

def organiser_dossier():
    if not os.path.exists(DOSSIER_CIBLE):
        print(f"Le dossier {DOSSIER_CIBLE} n'existe pas.")
        return

    for fichier in os.listdir(DOSSIER_CIBLE):
        chemin_fichier = os.path.join(DOSSIER_CIBLE, fichier)

        # Ignore les dossiers, on ne traite que les fichiers
        if os.path.isdir(chemin_fichier):
            continue

        # Récupère l'extension du fichier
        _, extension = os.path.splitext(fichier)
        extension = extension.lower()

        deplace = False
        for categorie, extensions in EXTENSIONS_CATEGORIES.items():
            if extension in extensions:
                dossier_destination = os.path.join(DOSSIER_CIBLE, categorie)
                
                # Crée le dossier s'il n'existe pas
                if not os.path.exists(dossier_destination):
                    os.makedirs(dossier_destination)
                
                # Déplace le fichier
                shutil.move(chemin_fichier, os.path.join(dossier_destination, fichier))
                print(f"Déplacé : {fichier} -> {categorie}")
                deplace = True
                break
        
        if not deplace:
            print(f"Ignoré (format non géré) : {fichier}")

if __name__ == "__main__":
    organiser_dossier()