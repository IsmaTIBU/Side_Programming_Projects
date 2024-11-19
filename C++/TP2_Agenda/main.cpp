#include <iostream>
#include <string>
#include "Agenda.h"
using namespace std;

int main() {
    // Créer un objet de la classe Agenda avec une capacité de 3 pour l'agenda 1, 2 pour l'agenda 2
    Agenda a1(3);
    Agenda a2(2);
    Agenda a3;

    // Ajouter des entrées à l'agenda en utilisant l'opérateur +=
    a1 += make_pair("Ismael", "+34 689007389");
    a1 += make_pair("Alice", "+34 612345678");
    a2 += make_pair("Bob", "+34 612345679");
    a2 += make_pair("Charlie", "+34 612345680");

    // Afficher le contenu de l'agenda en utilisant l'opérateur <<
    cout << "Contenu de l'agenda 1:\n" << a1;
    cout << "\nContenu de l'agenda 2:\n" << a2;

    // Supprimer "Charlie" en utilisant l'opérateur -=
    a1 -= string("Alice");
    cout << "\nApres suppression d'Alice de l'agenda 1:\n" << a1;

    // Concatenation de a2 a a1
    a1 |= a2;
    cout<<"\nContenu de l'agenda 1 apres concatenation avec agenda 2\n"<<a1<<endl;

    // Rechercher un numéro de téléphone en utilisant l'opérateur []
    string numero = a1["Ismael"];
    cout << "Numero de Ismael: " << numero << endl;

    // Vérifier si un nom est dans l'agenda en utilisant l'opérateur /
    if (a1 / "Charlie") {
        cout << "\nCharlie est dans l'agenda 1\n";
    } else {
        cout << "\nCharlie n'est pas dans l'agenda 1\n";
    }
    if (a2 / "Charlie") {
        cout << "Charlie est dans l'agenda 2\n";
    } else {
        cout << "Charlie n'est pas dans l'agenda 2\n";
    }

    // Afficher tous les noms commençant par la lettre 'C' en utilisant l'opérateur ()
    cout << "\nNoms commencant par C dans l'agenda 2:\n";
    a2('C');
    cout << "\nNoms commencant par I dans l'agenda 1:\n";
    a1('I');

    // Comparer deux agendas en utilisant l'opérateur ==
    if (a1 == a2) {
        cout << "Les agendas 1 et 2 sont identiques\n";
    } else {
        cout << "Les agendas 1 et 2 sont differents\n";
    }

    return 0;
}
