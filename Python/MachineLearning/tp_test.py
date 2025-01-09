import os
from ModuleTPClassif import *  # Import des fonctions fournies
import numpy as np
from termcolor import colored
import librosa
import matplotlib.pyplot as plt

# --- Initialisation ---
date = 20231130
chemin_fichiers = "./Signaux"  # Modifier selon ton chemin

# --- Fonction pour calculer les MFCC utilisables pour l'AFD ---
def calculer_mfcc_pour_afd_librosa(chemin_fichiers):
    fichiers_audio = [f for f in os.listdir(chemin_fichiers) if f.endswith(".wav")]

    if not fichiers_audio:
        print(colored("Aucun fichier audio trouvé dans le répertoire.", "red"))
        return None, None, None

    print(f"Traitement de {len(fichiers_audio)} fichiers audio...")

    mfcc_matrice = []  # Pour stocker les coefficients MFCC
    labels = []  # Pour stocker les classes associées

    prefixes = ['aa', 'ee', 'eh', 'eu', 'ii', 'oe', 'oh', 'oo', 'uu', 'yy']  # Labels prédéfinis

    for fichier in fichiers_audio:
        # Lecture du fichier audio avec librosa
        chemin_complet = os.path.join(chemin_fichiers, fichier)
        echantillons, fe = librosa.load(chemin_complet, sr=None)

        # Calcul des coefficients MFCC
        mfcc_coeffs = librosa.feature.mfcc(y=echantillons, sr=fe, n_mfcc=13, n_fft=512)

        # Moyenne des coefficients sur toutes les trames
        mfcc_moyen = np.mean(mfcc_coeffs, axis=1)
        mfcc_matrice.append(mfcc_moyen)

        # Récupération du label depuis le préfixe du fichier
        prefix = fichier[:2]
        if prefix in prefixes:
            labels.append(prefixes.index(prefix) + 1)  # Classe associée
        else:
            print(colored(f"Préfixe inconnu pour le fichier {fichier}. Ignoré.", "yellow"))

    return np.array(mfcc_matrice), np.array(labels), prefixes

# --- Appliquer l'AFD avec corrections pour les centres de gravité ---
def appliquer_afd_custom_librosa(mfcc_matrice, labels, prefixes):
    if mfcc_matrice is None or labels is None:
        print("Les données ou les labels sont manquants.")
        return

    print("Application de l'Analyse Factorielle Discriminante (AFD) avec les fonctions personnalisées...")

    # Calcul des centres de gravité (données brutes, non centrées)
    CentresGravite = CalculerCentresGravite(mfcc_matrice, labels)
    print("Centres de gravité calculés :", CentresGravite)

    # Calcul des individus centrés réduits
    mfcc_centres_red = CalculerIndividusCentresReduits(mfcc_matrice, CentresGravite)

    # Correction : Assurer que les centres sont recalculés en accord avec les individus centrés réduits
    CentresGraviteReduits = CalculerCentresGravite(mfcc_centres_red, labels)

    # Calcul des variances (pour validation)
    VT, VA, VE = CalculerVariances(mfcc_matrice, labels, CentresGravite)
    print(f"Variances: Totale={VT:.2f}, Intraclasses={VA:.2f}, Interclasses={VE:.2f}")

    # Visualisation en 2D
    PresenterClasses2D(
        mfcc_centres_red,
        labels,
        "Projection AFD (individus centrés réduits)",
        CentresGravite=CentresGraviteReduits,
        prefixes=prefixes
    )

# --- Fonction de visualisation en 2D ---
def PresenterClasses2D(Individus, NoClasses, Titre, CentresGravite=[], ParamX=2, ParamY=3, prefixes=[]):
    TesterClasses(NoClasses)

    NbrIndividus, NbrParametres = np.shape(Individus)
    NbrClasses = np.max(NoClasses)

    # Couleurs pour les nuages de points
    couleurs = ['blue', 'green', 'purple', 'orange', 'cyan', 'pink', 'yellow', 'gray', 'brown', 'red']

    plt.figure(figsize=(10, 6))

    # Affichage des points des nuages avec des couleurs fixes
    for q in range(1, NbrClasses + 1):
        IndClasse = np.argwhere(NoClasses == q)[:, 0]
        plt.scatter(
            Individus[IndClasse, ParamX],
            Individus[IndClasse, ParamY],
            color=couleurs[(q - 1) % len(couleurs)],
            label=f"Classe {q} : {prefixes[q-1]}"
        )

    # Affichage des centres de gravité (croix noires)
    if len(CentresGravite) > 0:
        plt.scatter(
            CentresGravite[1:, ParamX],
            CentresGravite[1:, ParamY],
            color='black',
            marker='x',
            s=100,
            label="Centres de gravité"
        )

    plt.title(Titre)
    plt.xlabel(f"Paramètre {ParamX}")
    plt.ylabel(f"Paramètre {ParamY}")
    plt.legend()
    plt.grid()
    plt.show()

# --- Exécution ---
mfcc_matrice, labels, prefixes = calculer_mfcc_pour_afd_librosa(chemin_fichiers)

if mfcc_matrice is not None and labels is not None:
    appliquer_afd_custom_librosa(mfcc_matrice, labels, prefixes)
