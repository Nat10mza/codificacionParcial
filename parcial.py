
import numpy as np

palabra=input("Ingresa tu palabra, pa: ").upper();

def codificacion(value):
    palabra= value;
# 3-B deplazamiento en 3 consonantes, vocales desplazadas en 2
    consonantes = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "Ñ", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"];
    vocales= ["A","E","I","O","U"];
    desplazamiento_consonantes = 3
    desplazamiento_vocales = 2


    distancia= len(palabra);
    palabra_codifica= np.empty(distancia, dtype='U10')

# recorrido de la palabra
    for i in range(distancia):
        # Flag para agregar solo una vez las consonantes y vocales
        push_consonantes = False
        push_vocales = False

        # Chequear si letra es consonante
        
        for j in range(len(consonantes)):
            # Pushear consonantes para evitar error de indice
            if j + desplazamiento_consonantes >= len(consonantes) and not push_consonantes:
                consonantes = consonantes + consonantes
                push_consonantes = True

            if consonantes[j] == palabra[i]:  
                palabra_codifica[i] = consonantes[j + desplazamiento_consonantes]
        
        for k in range(len(vocales)):
            if k + desplazamiento_vocales >= len(vocales) and not push_vocales:
                vocales = vocales + vocales
                push_vocales = True

            if vocales[k] == palabra[i]:  
                palabra_codifica[i] = vocales[k + desplazamiento_vocales]        

    respuesta = "".join(palabra_codifica);
    return respuesta;



def decodificacion(value):
# 3-B deplazamiento en 3 consonantes, vocales desplazadas en 2
    palabra= value

    consonantes = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "Ñ", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"];
    vocales= ["A","E","I","O","U"];
    desplazamiento_consonantes = 3
    desplazamiento_vocales = 2
    distancia= len(palabra);
    palabra_codifica= np.empty(distancia, dtype='U10')

# recorrido de la palabra
    for i in range(distancia):
        # Flag para agregar solo una vez las consonantes y vocales
        unshift_consonantes = False
        unshift_vocales = False

        # Chequear si letra es consonante
        
        for j in range(len(consonantes)-1,-1,-1):
            if j - desplazamiento_consonantes < 0 and not unshift_consonantes:
                consonantes = consonantes + consonantes
                unshift_consonantes = True
            if consonantes[j] == palabra[i]: 
                palabra_codifica[i] = consonantes[j - desplazamiento_consonantes]
        
        for k in range(len(vocales)-1,-1,-1):
            if k - desplazamiento_vocales < 0 and not unshift_vocales:
                vocales = vocales + vocales
                unshift_vocales = True
            if vocales[k] == palabra[i]:  
                palabra_codifica[i] = vocales[k - desplazamiento_vocales]
        

    respuesta = "".join(palabra_codifica);
    return respuesta;



palabra_codificada = codificacion(palabra)
print('Palabra codificada: ',palabra_codificada);

palabra_decodificada = decodificacion(palabra_codificada)
print('Palabra decodificada: ',palabra_decodificada);