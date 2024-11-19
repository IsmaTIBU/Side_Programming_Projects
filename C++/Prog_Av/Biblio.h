#ifndef BIBLIO_H
#define BIBLIO_H
using namespace std;
#include "Livre.h"

class Biblio {
    Livre* tab;
    int nbLivres;
    int tailleMax;

public:
    // Constructeur
    Biblio(int=10);

    // Constructeur de copie
    Biblio(Biblio&);

    // Destructeur
    ~Biblio();

    // Opérateur d'affectation
    Biblio& operator=(Biblio&);

    // Opérateur d'affichage
    friend ostream& operator<<(ostream&, Biblio&);
};

#endif // BIBLIO_H
