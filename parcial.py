
import numpy as np

palabra=input("Ingresa tu palabra, pa: ").upper();

def codificacion(value):
    palabra= value;
# 3-B deplazamiento en 3 consonantes, vocales desplazadas en 2
    consonantes = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "Ñ", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"];
    vocales= ["A","E","I","O","U"];
    desplazamiento_consonantes = 3
    desplazamiento_vocal = 2


    distancia= len(palabra);
    palabra_codifica= np.empty(distancia, dtype='U10')

# recorrido de la palabra
    for i in range(distancia):
        # Chequear si letra es consonante
        
        for j in range(len(consonantes)):
            if consonantes[j] == palabra[i]:  
                palabra_codifica[i] = consonantes[j + desplazamiento_consonantes]
                print(palabra_codifica[i]);
        
        for k in range(len(vocales)):
            if vocales[k] == palabra[i]:  
                palabra_codifica[i] = vocales[k + desplazamiento_vocal]        

    respuesta = "".join(palabra_codifica);
    return respuesta;


def decodificacion(value):
# 3-B deplazamiento en 3 consonantes, vocales desplazadas en 2
    palabra= value

    consonantes = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "Ñ", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"];
    vocales= ["A","E","I","O","U"];
    desplazamiento_consonantes = 3
    desplazamiento_vocal = 2
    distancia= len(palabra);
    palabra_codifica= np.empty(distancia, dtype='U10')

# recorrido de la palabra
    for i in range(distancia):
        # Chequear si letra es consonante
        
        for j in range(len(consonantes)-1,-1,-1):
            if consonantes[j] == palabra[i]:  
                palabra_codifica[i] = consonantes[j - desplazamiento_consonantes]
                print(palabra_codifica[i]);
        
        for k in range(len(vocales)-1,-1,-1):
            if vocales[k] == palabra[i]:  
                palabra_codifica[i] = vocales[k - desplazamiento_vocal]
                print(palabra_codifica[i]);
        

    respuesta = "".join(palabra_codifica);
    return respuesta;






palabra_codificada = codificacion(palabra)
print('Palabra despues de primera ejecucion',palabra_codificada);

palabra_codificada_2 = decodificacion(palabra_codificada)
print('Palabra despues de primera ejecucion',palabra_codificada_2);