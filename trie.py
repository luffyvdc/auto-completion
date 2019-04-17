
# Regroupons sur ce fichier les fonctions servant à la création de la trie à partir d'un ensemble de textes

# Le choix des textes doit être modernes pour que l'ensemble des mots et des fréquences de base soit cohérents
# avec une utilisation actuelle.

# Article "Implémenter une trie dans Python en moins de 100 lignes", plutôt inspirant si on ne sait pas par où démarrer :
# https://towardsdatascience.com/implementing-a-trie-data-structure-in-python-in-less-than-100-lines-of-code-a877ea23c1a1

def creation_dico(livre):
    """fonction qui : - prend en argument un livre sous forme de chaîne de caractère
                      - retourne un arbre contenant tous les mots du livre une seule fois avec leur fréquence associée"""
    # on crée le dictionnaire que l'on va retourner ainsi que le string contenant tous les caractères spéciaux usuels
    dico = {}
    carac_speciaux = ',?;.:/!§%*µ$£=+<>})°]@\'_-(\[}#"~&1234567890{])'
    # je parcours tous les caractères spéciaux
    for i in carac_speciaux:
        # on repère tous les apostrophes dans le texte et l'on ajoute un espace juste après chacun d'eux pour délimiter le mot
        if i == "'":
            livre = livre.replace(i,i+" ")
        # on repère tous les autres caractères spéciaux que l'on remplace par un espace dans le texte
        else :
            livre = livre.replace(i,"")    
    # on récupère tous les mots sous forme de liste et on crée la liste qui contiendra une seule fois tous les mots
    liste_mots = livre.split(" ")
    liste_mots_uniques = []
    # on parcourt tous les mots du texte
    for mot in liste_mots :
        # si le mot n'est pas vide et s'il n'est pas déjà dans la liste des mots uniques
        if mot != "" and mot.lower() not in liste_mots_uniques :
            # on ajoute le mot à la liste des mots uniques et on crée le compteur qui va compter le nombre d'apparition de chaque mot
            liste_mots_uniques.append(mot.lower())
            compt = 0
            # on parcourt la longueur de la liste de mots
            for indice in range(len(liste_mots)) :
                # si le mot est le même que celui à la position indice dans la liste de mots, on incrémente le compteur
                if mot.lower() == liste_mots[indice].lower() :
                    compt += 1
            # on ajoute le mot au dictionnaire avec sa fréquence correspondante
            dico[mot] = compt*100/len(liste_mots)
    return(dico)
