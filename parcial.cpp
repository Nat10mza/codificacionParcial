#include <iostream>
#include <string>
#include <cctype>
#include <cstring>

using namespace std;

// Protitipos
void codificacion(char *value, char *consonantes, char *vocales, int desplazamiento_consonantes, int desplazamiento_vocales);
void toUpper(char *str);

int main()
{
    char palabra[20];
    cout << "Ingrese una palabra: ";
    cin >> palabra;
    toUpper(palabra);

    char consonantes[] = "BCDFGHJKLMNÑPQRSTVWXYZ";
    char vocales[] = "AEIOU";
    int desplazamiento_consonantes = 3;
    int desplazamiento_vocales = 2;

    // codificacion(palabra, consonantes, vocales, desplazamiento_consonantes, desplazamiento_vocales);
    // cout << "Palabra codificada: " << palabra << endl;

    return 0;
}

void toUpper(char *str)
{
    for (int i = 0; str[i]; i++)
    {
        str[i] = toupper(str[i]);
    }
}