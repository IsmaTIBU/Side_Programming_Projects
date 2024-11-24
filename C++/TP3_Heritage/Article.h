#ifndef ARTICLE_H
#define ARTICLE_H

#include "Document.h"
#include <string>
using namespace std;

class Article : public Document {
    string revue;
    string editeur;
    int num_edit;

public:
    Article(string& titre, string auteur = "", string* resume = nullptr, string revue = "", string editeur = "", int num_edit = 0);
    Article(const Article& copie);
    Article* clone() const;
    void afficher();
    Article& operator=(const Article& autre);
};

#endif // ARTICLE_H
