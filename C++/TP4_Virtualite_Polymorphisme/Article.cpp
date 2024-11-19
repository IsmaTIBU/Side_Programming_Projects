#include "Article.h"
#include <iostream>

using namespace std;

Article::Article(string& titre, string auteur, string* resume, string revue, string editeur, int num_edit, double prix_de_base)
    : Document(titre, resume, auteur, prix_de_base), revue(revue), editeur(editeur), num_edit(num_edit) {}

Article::Article(const Article& copie)
    : Document(copie), revue(copie.revue), editeur(copie.editeur), num_edit(copie.num_edit) {}

Article* Article::clone() const {
    return new Article(*this);
}

void Article::afficher() const {
    cout << "Titre: " << titre << endl;
    cout << "Auteur: " << auteur << endl;
    cout << "Resume: " << *resume << endl;
    cout << "Revue: " << revue << endl;
    cout << "Editeur: " << editeur << endl;
    cout << "Numero d'edition: " << num_edit << endl;
    cout<< "Prix de l'article: "<<calculerCout()<<" eur"<<endl;
}

const string& Article::getTitre() const {
    return titre;
}

double Article::calculerCout() const {
    double prix_final=prix_de_base+(num_edit)*1.1;
    return prix_final;
}