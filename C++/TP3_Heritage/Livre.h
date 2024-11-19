#ifndef LIVRE_H
#define LIVRE_H

#include "Document.h"
#include <string>
using namespace std;

class Livre : public Document {
    string editeur;
    int anneeParution;
public:
    Livre(string& titre, string* resume = nullptr,string auteur = "",
          string editeur = "", int anneeParution = 0);
    Livre(const Livre& copie);
    Livre* clone() const;
    void afficher();
    Livre& operator=(const Livre& autre);


};



#endif //LIVRE_H
