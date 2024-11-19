#ifndef TABLEAU_H
#define TABLEAU_H
#include "Entree.h"
#include <string>
using namespace std;

class Agenda;

class Tableau {
    int taille_tot_tab=0;
    Entree* tableau_entree;
    int nb_elem=0;
public:
    //Constructeur
    Tableau(int taille=10);
    //Destructeur
    ~Tableau();
    //Constructeur par copie
    Tableau(const Tableau& copie);

    void affichage()const;
    void ajouter(const string& nom, const string& num_tel);
    void supp_all(const string& nom, const string& num_tel);
    void supp_nom(const string& nom);
    int getNbElem() const;
    int getTailleTot() const;
    Entree getEntree(int index) const;


    friend class Agenda;
};

#endif //TABLEAU_H