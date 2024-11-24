#include "Tableau.h"
#include "Entree.h"
#include <iostream>
#include <string>
using namespace std;

Tableau::Tableau(int taille_tab):taille_tot_tab(taille_tab), tableau_entree(new Entree[taille_tot_tab]) {
    this->nb_elem = 0;
}

Tableau::~Tableau() {
    delete[] tableau_entree;
}

Tableau::Tableau(const Tableau& copie):taille_tot_tab(copie.taille_tot_tab),nb_elem(copie.nb_elem), tableau_entree(new Entree[taille_tot_tab]) {
    for (int i = 0; i < nb_elem; i++) {
        tableau_entree[i] = copie.tableau_entree[i];
    }
}

void Tableau::affichage() const {
    for (int i = 0; i < nb_elem; i++) {
        tableau_entree[i].affichage();
    }
}

void Tableau::ajouter(const string& nom, const string& num_tel) {
    if (nb_elem >= taille_tot_tab) {
        taille_tot_tab *= 2;
        Entree* nouveau_tableau = new Entree[taille_tot_tab];
        for (int i = 0; i < nb_elem; i++) {
            nouveau_tableau[i] = tableau_entree[i];
        }
        delete[] tableau_entree;
        tableau_entree = nouveau_tableau;
    }
    tableau_entree[nb_elem] = Entree(nom, num_tel);
    nb_elem++;
}


void Tableau::supp_all(const string& nom, const string& num_tel) {
    for (int i = 0; i < nb_elem; i++) {
        if (tableau_entree[i].nom == nom && tableau_entree[i].num_tel == num_tel) {
            for (int j = i; j < nb_elem - 1; j++) {
                tableau_entree[j] = tableau_entree[j + 1];
            }
            nb_elem--;
            return;
        }
    }
}

void Tableau::supp_nom(const string& nom) {
    int i = 0;
    while (i < nb_elem) {
        if (tableau_entree[i].nom == nom) {
            for (int j = i; j < nb_elem - 1; j++) {
                tableau_entree[j] = tableau_entree[j + 1];
            }
            nb_elem--;
        } else {
            i++;
        }
    }
}

int Tableau::getNbElem() const {
    return this->nb_elem;
}

int Tableau::getTailleTot() const {
    return taille_tot_tab;
}

Entree Tableau::getEntree(int index) const {
    if (index >= 0 && index < nb_elem) {
        return tableau_entree[index];
    }
    throw out_of_range("Index hors de portée");
}

