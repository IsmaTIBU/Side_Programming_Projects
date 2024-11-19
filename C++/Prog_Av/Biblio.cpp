#include <iostream>
#include "Biblio.h"

// Constructeur
Biblio::Biblio(int taille){
    this -> tab = new Livre[taille];
    this -> nbLivres=0;
    this-> tailleMax=taille;
}

Biblio::Biblio(Biblio& copie) {
    this->tailleMax=copie.tailleMax;
    this->nbLivres=copie.nbLivres;
    this ->tab=newLivre[tailleMax];
    for (int i = 0; i < nbLivres; i++) {
        this->tab[i]=copie.tab[i];
    }
}

Biblio::~Biblio() {
    delete []tab;
}

Biblio& Biblio::operator=(Biblio& copie) {
    if(this != &copie) {
        delete [] tab;
        this -> tab = new Livre [copie.tailleMax];
        this -> nbLivres=copie.nbLivres;
        this -> tailleMax=copie.tailleMax;
        for (int i = 0; i < nbLivres; i++) {
            this->tab[i]=copie.tab[i];
        }
    }
}

ostream& operator<<(ostream& out, const Biblio& b) {
    out<<"Bibliotheque"<<b.nbLivres<<"livres"<<endl;
    for(int i = 0; i < b.nbLivres; i++) {
        out<<b.tab[i];
    }
    return out;
}