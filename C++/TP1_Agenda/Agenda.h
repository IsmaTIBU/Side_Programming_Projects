#ifndef AGENDA_H
#define AGENDA_H

#include <string>
#include "Tableau.h"
using namespace std;

class Agenda {
    Tableau tab;

public:
    Agenda(int taille=10);
    Agenda(Agenda&);

    void concat(Agenda& a2);
    void ajouter(string nom, string num_tel);
    void supp_all(string nom, string num_tel);
    void supp_nom(string nom);
    void affichage();

};



#endif //AGENDA_H
