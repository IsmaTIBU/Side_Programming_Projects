#ifndef DOCUMENT_H
#define DOCUMENT_H

#include <string>
using namespace std;

class Document {
protected:
    string& titre;
    string* resume;
    string auteur;
    double prix_de_base;

public:
    Document(string& titre, string* resume,string auteur, double prix_de_base);
    virtual void afficher() const = 0;
    virtual Document* clone() const = 0;
    virtual double calculerCout() const = 0;

    virtual const string& getTitre() const {
        return titre;
    }

    virtual double getPrix() const {
        return prix_de_base;
    }
};

#endif // DOCUMENT_H
