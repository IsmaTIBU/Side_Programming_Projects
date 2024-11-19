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
    //Constructeur
    Document(string& titre, string* resume=nullptr, string auteur="");

    // Constructeur de copie
    Document(const Document& copie);

    // Méthode de clonage
    Document* clone() const;

    // Méthode pour afficher le document
    void afficher();

    Document& operator=(const Document& autre);

};



#endif //DOCUMENT_H
