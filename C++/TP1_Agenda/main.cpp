#include <iostream>
#include <string>
#include "Agenda.h"
using namespace std;

int main() {
    // Crear un objeto de la clase Agenda con una capacidad de 5
    Agenda a1(3);
    Agenda a2(2);
    Agenda a3;

    // Añadir entradas al agenda
    a1.ajouter("Ismael", "+34 689007389");
    a1.ajouter("Alice", "+34 612345678");
    a2.ajouter("Bob", "+34 612345679");
    a2.ajouter("Charlie", "+34 612345680");

    // Mostrar el contenido del agenda
    cout << "Contenu de l'agenda 1:\n";
    a1.affichage();
    cout << "\nContenu de l'agenda 2:\n";
    a2.affichage();
    cout << "\nConcatenation d'agenda 1 et 2" << endl;
    a1.concat(a2);
    a1.affichage();

    cout << "\nSuppression d'Alice" << endl;
    a1.supp_nom("Alice");
    cout << "Apres suppression d'Alice:\n";
    a1.affichage();

    cout << "\nQuestion 5)";
    cout <<"\nAgenda gere Tableau via un pointeur, ce qui necessite une gestion de la memoire (new et delete)";
    cout <<"\nLes methodes de Agenda accedent desormais a Tableau en utilisant '->' au lieu de '.'"<<endl;


    return 0;
}
