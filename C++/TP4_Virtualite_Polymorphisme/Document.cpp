#include "Document.h"
#include <iostream>

using namespace std;

Document::Document(string& titre, string* resume, string auteur, double prix_de_base)
    : titre(titre), resume(new string(*resume)), auteur(auteur), prix_de_base(prix_de_base) {}
