#include <iostream>
#include "Livre.h"
#include "Article.h"
using namespace std;

int main() {
    //Creation d'un DOCUMENT
    string resume0 = "C est un langage de programation...";
    string titre0 = "Cours de C";
    Document D1(titre0, &resume0, "Ismael");
    D1.afficher();

    //UTILISATION DE L'OPPERATEUR
    Document D2=D1;
    cout << "\nDOCUMENT ASSIGNE:" << endl;
    D2.afficher();
    cout<<"\n";

    //Creation d'un LIVRE
    string resume1 = "C# est un langage de programation...";
    string titre1 = "Cours de C#";
    Livre L1(titre1, &resume1, "Ismael", "Solal", 2024);
    L1.afficher();

    //UTILISATION DE L'OPPERATEUR POUR UN LIVRE
    Livre L2=L1;
    cout << "\nLIVRE ASSIGNE:" << endl;
    L2.afficher();
    cout<<"\n";

    // Creation d'un ARTICLE
    string resume2 = "C++ est un langage de programation...";
    string titre2 = "Cours de C++";
    Article a1(titre2, "Solal", &resume2, "CoddingNews", "Olivero", 3);
    a1.afficher();

    // UTILISATION DE L'OPPERATEUR POUR L'ARTICLE
    Article a2 = a1;
    cout << "\nARTICLE ASSIGNE:" << endl;
    a2.afficher();

    return 0;
}
