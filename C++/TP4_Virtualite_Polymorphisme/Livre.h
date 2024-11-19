#ifndef LIVRE_H
#define LIVRE_H

#include "Document.h"
using namespace std;

class Livre : public Document {
    string editeur;
    int anneeParution;

public:
    Livre(string& titre, string* resume, string auteur,string editeur, int anneeParution, double prix_de_base);
    Livre(const Livre& copie);
    Livre* clone() const override;
    void afficher() const override;
    const string& getTitre() const override;
    double calculerCout() const override;
};

#endif // LIVRE_H
