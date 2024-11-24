#ifndef DOCUMENT_H
#define DOCUMENT_H

#include <string>
using namespace std;

class Document {
protected:
    string& titre;
    string* resume;
    string auteur;

public:
    Document(string& titre, string* resume,string auteur);
    virtual void afficher() const = 0;
    virtual Document* clone() const = 0;
    virtual double calculerCout() const=0;

    virtual const string& getTitre() const;
};

#endif // DOCUMENT_H
