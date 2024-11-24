#include "Livre.h"
#include <iostream>

using namespace std;

Livre::Livre(string& titre, string* resume, string auteur, string editeur, int anneeParution)
    : Document(titre, resume, auteur), editeur(editeur), anneeParution(anneeParution) {}

Livre::Livre(const Livre& copie)
    : Document(copie), editeur(copie.editeur), anneeParution(copie.anneeParution) {}

Livre* Livre::clone() const {
    return new Livre(*this);
}

void Livre::afficher() const {
    cout << "Titre: " << titre << endl;
    cout << "Auteur: " << auteur << endl;
    cout << "Resume: " << *resume << endl;
    cout << "Editeur: " << editeur << endl;
    cout << "Annee de parution: " << anneeParution << endl;
    cout<< "Prix du livre: "<<calculerCout()<<" eur"<<endl;
}

const string& Livre::getTitre() const {
    return titre;
}

double Livre::calculerCout() const {
    double prix_final=7+(2024-anneeParution)*1.1;
    return prix_final;
}
