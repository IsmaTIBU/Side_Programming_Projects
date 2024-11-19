#include <iostream>
#include "Entree.h"
using namespace std;

Entree::Entree(string nom,string num_tel) {
    this->nom=nom;
    this->num_tel=num_tel;
}

void Entree::affichage() const {
    cout<<"Utilisateur: "<<nom<<"\t|Numero de telephone: "<<num_tel<<endl;
}

const string& Entree::getNom()const {
    return nom;
}
const string& Entree::getNumTel()const {
    return num_tel;
}