#include <iostream>
#include "Livre.h"
#include "Biblio.h"

int main() {
    Biblio T;
    Biblio B(10);
    Biblio A(B);

    return 0;
}
