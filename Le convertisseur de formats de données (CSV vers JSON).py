import csv
import json

def csv_vers_json(chemin_csv, chemin_json):
    donnees = []
    
    try:
        # Lecture du fichier CSV
        with open(chemin_csv, mode="r", encoding="utf-8") as fichier_csv:
            lecteur_csv = csv.DictReader(fichier_csv)
            for ligne in lecteur_csv:
                donnees.append(ligne)
                
        # Écriture dans le fichier JSON
        with open(chemin_json, mode="w", encoding="utf-8") as fichier_json:
            json.dump(donnees, fichier_json, indent=4, ensure_ascii=False)
            
        print(f"Conversion réussie : {chemin_csv} converti en {chemin_json}")

    except FileNotFoundError:
        print(f"Erreur : Le fichier CSV spécifié est introuvable.")

# Exemple d'utilisation :
if __name__ == "__main__":
    csv_vers_json("donnees.csv", "donnees.json")