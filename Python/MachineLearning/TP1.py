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

        # Durée totale du signal en secondes
        winlen = len(echantillons) / fe
        winstep = winlen  # Pas de décalage, une seule fenêtre

        # Calcul des coefficients MFCC
        VecteurCoefficients = librosa.feature.mfcc(
            y=echantillons, sr=fe, n_mfcc=13, hop_length=len(echantillons), n_fft=512
        )

        # Extraire le vecteur (un seul jeu de coefficients)
        mfcc_moyen = VecteurCoefficients[:, 0]  # Une seule fenêtre
        mfcc_matrice.append(mfcc_moyen)

        # Récupération du label depuis le préfixe du fichier
        prefix = fichier[:2]
        if prefix in prefixes:
            labels.append(prefixes.index(prefix) + 1)  # Classe associée
        else:
            print(colored(f"Préfixe inconnu pour le fichier {fichier}. Ignoré.", "yellow"))

    # Conversion en matrice numpy
    return np.array(mfcc_matrice), np.array(labels), prefixes


# --- Calcul des coefficients cepstraux ---
def calculer_cepstre(echantillons):
    print("Calcul des coefficients cepstraux...")
    # Transformée de Fourier
    tf_signal = np.fft.fft(echantillons)

    # Calcul du logarithme du module
    log_magnitude = np.log(np.abs(tf_signal) + 1e-10)  # Ajout d'un epsilon pour éviter log(0)

    # Transformée de Fourier inverse
    cepstre = np.fft.ifft(log_magnitude).real

    # Affichage du cepstre
    plt.figure()
    plt.plot(cepstre)
    plt.title("Coefficients Cepstraux")
    plt.xlabel("Quefrence")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()

    return cepstre


# --- Analyse du signal : représentation temporelle et DSP ---
def analyser_signal_temporel_frequentiel(chemin_fichier):
    # Charger le fichier audio
    echantillons, fe = librosa.load(chemin_fichier, sr=None)

    # Représentation temporelle
    plt.figure(1)
    plt.plot(echantillons)
    plt.title("Représentation temporelle du signal")
    plt.xlabel("Temps (échantillons)")
    plt.ylabel("Amplitude")
    plt.grid()

    # Transformée de Fourier et calcul de la DSP
    tf_signal = np.fft.fft(echantillons)
    dsp = np.multiply(tf_signal, np.conj(tf_signal)).real  # Partie réelle de la DSP

    # Axe des fréquences
    freqs = np.fft.fftfreq(len(dsp), 1 / fe)

    # Représentation fréquentielle (DSP)
    plt.figure(2)
    plt.plot(freqs[:len(freqs) // 2], dsp[:len(dsp) // 2])  # Partie positive des fréquences
    plt.title("Densité Spectrale de Puissance")
    plt.xlabel("Fréquence (Hz)")
    plt.ylabel("Puissance")
    plt.grid()

    plt.show()

    # Calcul des coefficients cepstraux
    calculer_cepstre(echantillons)


# --- Appliquer l'AFD avec corrections pour les centres de gravité ---
def appliquer_afd_custom_librosa(mfcc_matrice, labels, prefixes):
    if mfcc_matrice is None or labels is None:
        print("Les données ou les labels sont manquants.")
        return

    print("\nApplication de l'Analyse Factorielle Discriminante (AFD) avec les fonctions personnalisées...")

    # Calcul des centres de gravité (données brutes, non centrées)
    CentresGravite = CalculerCentresGravite(mfcc_matrice, labels)

    # Calcul des individus centrés réduits
    mfcc_centres_red = CalculerIndividusCentresReduits(mfcc_matrice, CentresGravite)

    # Correction : Assurer que les centres sont recalculés en accord avec les individus centrés réduits
    CentresGraviteReduits = CalculerCentresGravite(mfcc_centres_red, labels)

    # Calcul des variances (pour validation)
    VT, VA, VE = CalculerVariances(mfcc_centres_red, labels, CentresGraviteReduits)

    print(f"Variances: Totale={VT:.2f}, Intraclasses={VA:.2f}, Interclasses={VE:.2f}")

    # Visualisation en 2D
    # Visualisation en 2D
    PresenterClasses2D(
        mfcc_centres_red,
        labels,
        "Projection AFD (individus centrés réduits)",
        CentresGravite=CentresGraviteReduits,
        prefixes=prefixes,
        ParamX=2,
        ParamY=3
    )

    return mfcc_centres_red


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
            label=f"Classe {q} : {prefixes[q - 1]}"
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
fichiers_audio = [f for f in os.listdir(chemin_fichiers) if f.endswith(".wav")]

if fichiers_audio:
    print("Analyse temporelle et fréquentielle du premier fichier...")
    analyser_signal_temporel_frequentiel(os.path.join(chemin_fichiers, fichiers_audio[0]))

    print("Calcul des MFCC et application de l'AFD...")
    mfcc_matrice, labels, prefixes = calculer_mfcc_pour_afd_librosa(chemin_fichiers)

    appliquer_afd_custom_librosa(mfcc_matrice, labels, prefixes)
    # Renvoyer les données pour utilisation dans d'autres scripts
    mfcc_centres_red = CalculerIndividusCentresReduits(mfcc_matrice, CalculerCentresGravite(mfcc_matrice, labels))

else:
    print(colored("Aucun fichier audio trouvé pour l'analyse.", "red"))
