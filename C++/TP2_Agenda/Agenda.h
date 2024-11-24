#ifndef AGENDA_H
#define AGENDA_H

#include <string>
#include <iostream>
#include "Tableau.h"
using namespace std;

class Agenda {
    Tableau tab;

public:
    Agenda(int taille = 10);
    Agenda(const Agenda& copie);

    void concat(const Agenda& a2);
    void ajouter(const string& nom, const string& num_tel);
    void supp_nom(const string& nom);
    void supp_all(const string& nom, const string& num_tel);
    void affichage() const;

    friend ostream& operator<<(ostream& os, const Agenda& agenda);
    Agenda& operator+=(const Entree& entree);
    Agenda& operator|=(const Agenda& autre);
    Agenda& operator=(const Agenda& autre);
    Agenda operator+(const Agenda& copie) const;
    string operator[](const string& nom) const;
    Agenda& operator-=(const string& nom);
    bool operator==(const Agenda& autre) const;
    bool operator/(const string& nom) const;
    void operator()(char lettre) const;
};

#endif // AGENDA_H
