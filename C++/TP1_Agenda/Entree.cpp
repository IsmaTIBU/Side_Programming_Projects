#include <iostream>
#include "Entree.h"
using namespace std;

Entree::Entree(string nom,string num_tel): nom(nom), num_tel(num_tel) {
}

void Entree::affichage() {
    cout<<"Utilisateur: "<<this->nom<<"\t|Numero de telephone: "<<this->num_tel<<endl;
}

string Entree::getNom() const{
    return nom;
}
string Entree::getNumTel() const{
    return num_tel;
}