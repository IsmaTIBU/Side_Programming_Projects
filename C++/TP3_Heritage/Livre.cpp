#include "Livre.h"
#include <iostream>
using namespace std;

Livre::Livre(string &titre, string *resume, string auteur,
             string editeur, int anneeParution): Document(titre, resume, auteur), editeur(editeur),anneeParution(anneeParution) {
}

Livre::Livre(const Livre &copie): Document(copie), editeur(copie.editeur), anneeParution(copie.anneeParution) {
}

Livre *Livre::clone() const {
    return new Livre(*this); // Retourne une copie de l'objet actuel
}

void Livre::afficher() {
    Document::afficher();
    cout << "Editeur: " << editeur << endl;
    cout << "Annee de parution: " << anneeParution << endl;
}

Livre &Livre::operator=(const Livre &autre) {
    Document::operator=(autre);
    this->editeur = autre.editeur;
    this->anneeParution = autre.anneeParution;
    return *this;
}
