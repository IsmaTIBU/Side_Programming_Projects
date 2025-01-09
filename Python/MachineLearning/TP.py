import os
import numpy as np
from termcolor import colored
import matplotlib.pyplot as plt
from scipy.io import wavfile
from python_speech_features import mfcc
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# --- Initialisation ---
date = 20231130
chemin_fichiers = "./Signaux"  # Modifier selon ton chemin
prefixes = ['aa', 'ee', 'eh', 'eu', 'ii', 'oe', 'oh', 'oo', 'uu', 'yy']


# Fonctions Utiles
def TesterClasses(NoClasses):
    numMini = min(NoClasses)
    numMaxi = max(NoClasses)
    if numMini < 1:
        print(colored(
            f'Attention, les numeros de classe doivent commencer à 1 (ici {numMini}). La valeur 0 est réservée.',
            'red'))
    for i in range(1, numMaxi + 1):
        if len(np.argwhere(NoClasses == i)) == 0:
            print(colored(f'Attention, la classe numero {i} est vide.', 'red'))


# --- Partie 1 : Lecture des fichiers et Extraction MFCC ---
X = []  # Matrice des coefficients MFCC
Y = []  # Labels (classes)

for fichier in os.listdir(chemin_fichiers):
    if fichier.endswith(".wav"):
        # Lecture du fichier
        fe, echantillons = wavfile.read(os.path.join(chemin_fichiers, fichier))

        # Représentation temporelle
        plt.figure()
        plt.plot(echantillons)
        plt.title(f"Représentation temporelle - {fichier}")
        plt.close()

        # Densité Spectrale de Puissance
        tf_signal = np.fft.fft(echantillons)
        dsp = np.abs(tf_signal) ** 2
        plt.figure()
        plt.plot(dsp[:len(dsp) // 2])
        plt.title(f"Densité Spectrale de Puissance - {fichier}")
        plt.close()

        # Extraction des coefficients MFCC
        mfcc_coeffs = mfcc(echantillons, fe, winlen=0.025, winstep=0.01, numcep=13, nfft=2048)
        X.append(mfcc_coeffs.flatten())

        # Récupération du numéro de classe
        num_classe = prefixes.index(fichier[:2])
        Y.append(num_classe)

X = np.array(X)
Y = np.array(Y)

# --- Partie 2 : Analyse Factorielle Discriminante (AFD) ---
print("\nAnalyse Factorielle Discriminante (AFD)")
lda = LinearDiscriminantAnalysis()
X_afd = lda.fit_transform(X, Y)

# --- Visualisation des résultats AFD ---
plt.figure()
for i in range(len(prefixes)):
    plt.scatter(X_afd[Y == i, 0], X_afd[Y == i, 1], label=prefixes[i])
plt.title("Projection AFD des coefficients MFCC")
plt.xlabel("Axe 1")
plt.ylabel("Axe 2")
plt.legend()
plt.grid()
plt.show()


# --- Fonctions Complémentaires Utilisées dans l'analyse ---
def CalculerCentresGravite(Individus, NoClasses):
    TesterClasses(NoClasses)
    NbrIndividus, NbrVariables = np.shape(Individus)
    NbrClasses = np.max(NoClasses) + 1
    CentresGravite = np.zeros((NbrClasses, NbrVariables))
    CentresGravite[0] = np.mean(Individus, axis=0)
    for q in range(1, NbrClasses):
        IndClasse = np.argwhere(NoClasses == q)[:, 0]
        CentresGravite[q] = np.mean(Individus[IndClasse], axis=0)
    return CentresGravite


def PresenterClasses(Individus, NoClasses, Titre, CentresGravite=[], NomParametres=[], MaxGraphes=10, ParamX=0,
                     ParamY=0):
    TesterClasses(NoClasses)
    NbrIndividus, NbrParametres = np.shape(Individus)
    NbrClasses = np.max(NoClasses)
    motif = ('1', 'v', '2', 's', '3', 'p', '4', '*', '^', '+', 'x', '.', 'o')
    plt.figure()
    for q in range(1, NbrClasses + 1):
        IndClasse = np.argwhere(NoClasses == q)[:, 0]
        plt.scatter(Individus[IndClasse, ParamX], Individus[IndClasse, ParamY], label=f"Classe {q}")
    plt.title(Titre)
    plt.xlabel(f"Paramètre {ParamX}")
    plt.ylabel(f"Paramètre {ParamY}")
    plt.legend()
    plt.grid()
    plt.show()
