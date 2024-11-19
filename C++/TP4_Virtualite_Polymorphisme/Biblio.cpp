#include "Biblio.h"
#include <iostream>

using namespace std;

void Biblio::ajouterDocument(Document* doc) {
    documents.push_back(doc);
}

Document* Biblio::rechercherDocument(const string& titre) {
    for (Document* doc : documents) {
        if (doc->getTitre() == titre) {
            return doc;
        }
    }
    return nullptr;
}

void Biblio::afficherBibliotheque() const {
    for (const auto& doc : documents) {
        doc->afficher();
        cout << "-----------------" << endl;
    }
}

