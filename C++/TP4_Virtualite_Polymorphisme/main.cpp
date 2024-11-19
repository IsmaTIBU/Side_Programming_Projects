#include "Biblio.h"
#include "Livre.h"
#include "Article.h"
#include <iostream>

using namespace std;

int main() {
    Biblio biblio;

    string resume1 = "Langage C++ avance";
    string titre1 = "Programmation en C++";
    Livre* livre1 = new Livre(titre1, &resume1, "Ismael", "Patoty", 2017,7);

    string resume2 = "Introduction a l'algorithme";
    string titre2 = "Algorithmique";
    Article* article1 = new Article(titre2, "Solal", &resume2, "Science News", "Olivero", 3,5);

    biblio.ajouterDocument(livre1);
    biblio.ajouterDocument(article1);

    cout<<"\nLA BIBLIOTHEQUE EST REMPLIE AVEC LES SUIVANTS DOCUMENTS"<<endl;
    cout<<"------------------"<<endl;
    biblio.afficherBibliotheque();

    return 0;
}
