#ifndef ARTICLE_H
#define ARTICLE_H

#include "Document.h"
using namespace std;

class Article : public Document {
    string revue;
    string editeur;
    int num_edit;

public:
    Article(string& titre,string auteur,string* resume,string revue,string editeur, int num_edit, double prix_de_base);
    Article(const Article& copie);
    Article* clone() const override;
    void afficher() const override;
    const string& getTitre() const override;
    double calculerCout() const override;
};

#endif // ARTICLE_H
