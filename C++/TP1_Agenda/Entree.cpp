#include <iostream>
#include "Entree.h"
using namespace std;

Entree::Entree(string nom,string num_tel) {
    this->nom=nom;
    this->num_tel=num_tel;
}

void Entree::affichage() {
    cout<<"Utilisateur: "<<this->nom<<"\t|Numero de telephone: "<<this->num_tel<<endl;
}

string Entree::getNom() {
    return nom;
}
string Entree::getNumTel() {
    return num_tel;
}