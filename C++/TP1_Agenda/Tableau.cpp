#include "Tableau.h"
#include "Entree.h"
#include <iostream>
#include <string>
using namespace std;

Tableau::Tableau(int taille_tab) {
    this->taille_tot_tab = taille_tab;
    this->tableau_entree = new Entree[taille_tot_tab];
    this->nb_elem = 0;
}

Tableau::~Tableau() {
    delete []tableau_entree; //Liberation de memoire
}

Tableau::Tableau(Tableau& copie) {
    this->taille_tot_tab = copie.taille_tot_tab;
    this->tableau_entree=new Entree[taille_tot_tab];
    this->nb_elem=copie.nb_elem;
    for (int i = 0; i < nb_elem; i++) {
        this->tableau_entree[i]=copie.tableau_entree[i];
    }
}

void Tableau::affichage() {
    for (int i = 0; i < nb_elem; i++) {  // Iterar hasta nb_elem
        tableau_entree[i].affichage();
    }
}

void Tableau::ajouter(string nom, string num_tel) {
    if (nb_elem >= taille_tot_tab) {
        // Si el tableau está lleno, ampliarlo
        taille_tot_tab *= 2;  // Duplicar el tamaño del tableau
        Entree* new_tableau = new Entree[taille_tot_tab];

        // Copiar los elementos existentes al nuevo tableau
        for (int i = 0; i < nb_elem; i++) {
            new_tableau[i] = tableau_entree[i];
        }

        // Liberar el antiguo tableau y asignar el nuevo
        delete[] tableau_entree;
        tableau_entree = new_tableau;
    }

    tableau_entree[nb_elem] = Entree(nom, num_tel); // Nuevo objeto Entree
    nb_elem++;
}


void Tableau::supp_all(string nom, string num_tel) {
    for (int i = 0; i < nb_elem; i++) {
        // Verifier si le nom et num_tel coincident
        if (tableau_entree[i].nom == nom && tableau_entree[i].num_tel == num_tel) {
            // Eliminer l'element en mouvant tous d'apres d'un pas vers lui
            for (int j = i; j < nb_elem - 1; j++) {
                tableau_entree[j] = tableau_entree[j + 1];
            }
            nb_elem--; // Diminution du nombre d'elements
            return;
        }
    }
}

void Tableau::supp_nom(string nom) {
    for(int i=0;i<nb_elem;i++) {
        if (tableau_entree[i].nom == nom) {
            for (int j = i; j < nb_elem - 1; j++) {
                tableau_entree[j] = tableau_entree[j + 1];
            }
            nb_elem--;
            return;
        }
    }
}

int Tableau::getNbElem(){
    return nb_elem; // Retourne le nombre d'éléments
}

int Tableau::getTailleTot(){
    return taille_tot_tab; // Retourne la taille totale
}