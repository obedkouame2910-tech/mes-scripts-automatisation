def nettoyer_texte(chemin_entree, chemin_sortie):
    try:
        with open(chemin_entree, "r", encoding="utf-8") as f:
            lignes = f.readlines()

        lignes_nettoyees = []
        lignes_vues = set()

        for ligne in lignes:
            # Supprime les espaces inutiles au début et à la fin
            ligne_propre = ligne.strip()

            # Ignore les lignes vides et les doublons exacts
            if ligne_propre and ligne_propre not in lignes_vues:
                lignes_vues.add(ligne_propre)
                lignes_nettoyees.append(ligne_propre + "\n")

        with open(chemin_sortie, "w", encoding="utf-8") as f:
            f.writelines(lignes_nettoyees)

        print(f"Nettoyage réussi ! Fichier enregistré sous : {chemin_sortie}")
        print(f"Nombre de lignes uniques conservées : {len(lignes_nettoyees)}")

    except FileNotFoundError:
        print(f"Erreur : Le fichier {chemin_entree} est introuvable.")

# Exemple d'utilisation :
# Créez un fichier "texte_brut.txt" dans le même dossier pour tester
if __name__ == "__main__":
    nettoyer_texte("texte_brut.txt", "texte_propre.txt")