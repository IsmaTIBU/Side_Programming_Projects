#include "Document.h"
#include <iostream>

using namespace std;

Document::Document(string& titre, string* resume, string auteur)
    : titre(titre), resume(new string(*resume)), auteur(auteur) {}

const string& Document::getTitre() const {
    return titre;
}