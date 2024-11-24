#include "Agenda.h"
#include "Entree.h"
#include "Tableau.h"
#include <iostream>
#include <string>
using namespace std;

Agenda::Agenda(int taille) : tab(taille) {}

Agenda::Agenda(const Agenda& copie) : tab(copie.tab.getTailleTot()) {
    for (int i = 0; i < copie.tab.getNbElem(); i++) {
        Entree entree = copie.tab.getEntree(i);
        tab.ajouter(entree.getNom(), entree.getNumTel());
    }
}

void Agenda::concat(const Agenda& a2) {
    int nbElemA2 = a2.tab.getNbElem();
    for (int i = 0; i < nbElemA2; i++) {
        string nom = a2.tab.tableau_entree[i].getNom();
        string numTel = a2.tab.tableau_entree[i].getNumTel();
        tab.ajouter(nom, numTel);
    }
}

void Agenda::ajouter(const string& nom, const string& num_tel) {
    tab.ajouter(nom, num_tel);
}

void Agenda::supp_all(const string& nom, const string& num_tel) {
    tab.supp_all(nom, num_tel);
}

void Agenda::supp_nom(const string& nom) {
    tab.supp_nom(nom);
}

void Agenda::affichage() const {
    tab.affichage();
}

ostream& operator<<(ostream& os, const Agenda& agenda) {
    for (int i = 0; i < agenda.tab.getNbElem(); i++) {
        Entree entree = agenda.tab.getEntree(i);
        os << "Utilisateur: " << entree.getNom()
           << "\t| Numero de telephone: " << entree.getNumTel() << endl;
    }
    return os;
}


Agenda& Agenda::operator+=(const Entree& entree) {
    this->ajouter(entree.getNom(), entree.getNumTel());
    return *this;
}


Agenda& Agenda::operator|=(const Agenda& autre){
    this->concat(autre);
    return *this;
}


Agenda& Agenda::operator=(const Agenda& autre) {
    if (this != &autre) {
        this->tab = autre.tab;
    }
    return *this;
}

string Agenda::operator[](const string& nom) const {
    for (int i = 0; i < tab.getNbElem(); i++) {
        if (tab.tableau_entree[i].getNom() == nom) {
            return tab.tableau_entree[i].getNumTel();
        }
    }
    return "Non trouvé";
}

Agenda& Agenda::operator-=(const string& nom) {
    this->supp_nom(nom);
    return *this;
}

bool Agenda::operator==(const Agenda& autre) const {
    if (this->tab.getNbElem() != autre.tab.getNbElem()) return false;
    for (int i = 0; i < tab.getNbElem(); i++) {
        if (tab.tableau_entree[i].getNom() != autre.tab.tableau_entree[i].getNom() ||
            tab.tableau_entree[i].getNumTel() != autre.tab.tableau_entree[i].getNumTel()) {
            return false;
        }
    }
    return true;
}

bool Agenda::operator/(const string& nom) const {
    for (int i = 0; i < tab.getNbElem(); i++) {
        if (tab.tableau_entree[i].getNom() == nom) {
            return true;
        }
    }
    return false;
}

void Agenda::operator()(char lettre) const {
    for (int i = 0; i < tab.getNbElem(); i++) {
        if (tab.tableau_entree[i].getNom()[0] == lettre) {
            cout << tab.tableau_entree[i].getNom() << " : " << tab.tableau_entree[i].getNumTel() << endl;
        }
    }
}

Agenda Agenda::operator+(const Agenda& copie) const {
    Agenda resultat(this->tab.getNbElem() + copie.tab.getNbElem());

    for (int i = 0; i < this->tab.getNbElem(); i++) {
        string nom = this->tab.getEntree(i).getNom();
        string numTel = this->tab.getEntree(i).getNumTel();
        resultat.ajouter(nom, numTel);
    }

    for (int i = 0; i < copie.tab.getNbElem(); i++) {
        string nom = copie.tab.getEntree(i).getNom();
        string numTel = copie.tab.getEntree(i).getNumTel();
        resultat.ajouter(nom, numTel);
    }

    return resultat;
}