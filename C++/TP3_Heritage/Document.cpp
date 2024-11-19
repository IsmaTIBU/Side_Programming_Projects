#include "Document.h"
#include <iostream>
using namespace std;

Document::Document(string& titre, string* resume, string auteur): titre(titre){
    this-> auteur = auteur;
    this->resume = new string(*resume);
}

Document::Document(const Document &copie): titre(copie.titre){
    this-> auteur = copie.auteur;
    this->resume = new string(*copie.resume);
}

Document* Document::clone() const {
    return new Document(*this);
}

void Document::afficher() {
    cout<<"Titre: "<<titre<<endl;
    cout<<"Auteur: "<<this->auteur<<endl;
    cout<<"Resume: "<<*resume<<endl;
}

Document& Document::operator=(const Document& autre){
        Document* temp = autre.clone();
        swap(this->resume, temp->resume);
        this->auteur = temp->auteur;
        delete temp;
    return *this;
}

