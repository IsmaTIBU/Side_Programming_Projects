#include "Agenda.h"
#include "Entree.h"
#include "Tableau.h"
#include <iostream>
#include <string>
using namespace std;

Agenda::Agenda(int taille): tab(Tableau(taille)){
}

Agenda::Agenda(Agenda& copie):tab(copie.tab) {
}

void Agenda::concat(Agenda& a2) {
    int nbElemA2 = a2.tab.getNbElem();  // Número de elementos en la agenda a concatenar (a2)

    for (int i = 0; i < nbElemA2; i++) {
        this->tab.ajouter(a2.tab.tableau_entree[i].getNom(), a2.tab.tableau_entree[i].getNumTel());
    }
}

void Agenda::ajouter(string nom, string num_tel) {
    tab.ajouter(nom, num_tel);
}

void Agenda::supp_all(string nom, string num_tel) {
    tab.supp_all(nom, num_tel);
}

void Agenda::supp_nom(string nom) {
    tab.supp_nom(nom);
}

void Agenda::affichage() {
    tab.affichage();
}
