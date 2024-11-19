#ifndef BIBLIO_H
#define BIBLIO_H

#include <list>
#include "Document.h"
using namespace std;

class Biblio {
    list<Document*> documents;

public:
    void ajouterDocument(Document* doc);
    Document* rechercherDocument(const string& titre);
    void afficherBibliotheque() const;
};

#endif // BIBLIO_H
