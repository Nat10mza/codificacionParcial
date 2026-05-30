
import numpy as np

palabra=input("Ingresa tu palabra, pa: ").upper();
consonantes = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "Ñ", "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"];
vocales= ["A","E","I","O","U"];

# 3-B deplazamiento en 3 consonantes, vocales desplazadas en 2
desplazamiento_consonantes = 43
desplazamiento_vocales = 10


def codificacion(value, consonantes, vocales, desplazamiento_consonantes, desplazamiento_vocales):
    palabra= value;
    consonantes = consonantes;
    vocales= vocales;
    desplazamiento_consonantes = desplazamiento_consonantes
    desplazamiento_vocales = desplazamiento_vocales

    distancia= len(palabra);
    palabra_codifica= np.empty(distancia, dtype='U10')
    
# recorrido de la palabra
    for i in range(distancia):

        tamano_consonantes = len(consonantes)
        for j in range(tamano_consonantes):

            # Calcular la nueva posición con el desplazamiento y el módulo para evitar salir del rango
            nuevaPosicion = (j + desplazamiento_consonantes) % tamano_consonantes
            while nuevaPosicion >= tamano_consonantes:
                nuevaPosicion = nuevaPosicion - tamano_consonantes

            if consonantes[j] == palabra[i]:  
                palabra_codifica[i] = consonantes[nuevaPosicion]
        
        tamano_vocales = len(vocales)
        for k in range(tamano_vocales):
            
            nuevaPosicion = (k + desplazamiento_vocales) % tamano_vocales
            while nuevaPosicion >= tamano_vocales:
                nuevaPosicion = nuevaPosicion - tamano_vocales

            if vocales[k] == palabra[i]:  
                palabra_codifica[i] = vocales[nuevaPosicion]        

    respuesta = "".join(palabra_codifica);
    return respuesta;



# def decodificacion(value, consonantes, vocales, desplazamiento_consonantes, desplazamiento_vocales):
# # 3-B deplazamiento en 3 consonantes, vocales desplazadas en 2
#     palabra= value
#     consonantes = consonantes;
#     vocales= vocales;
#     desplazamiento_consonantes = desplazamiento_consonantes
#     desplazamiento_vocales = desplazamiento_vocales
#     distancia= len(palabra);
#     palabra_codifica= np.empty(distancia, dtype='U10')

# # recorrido de la palabra
#     for i in range(distancia):
#         # Flag para agregar solo una vez las consonantes y vocales
#         unshift_consonantes = False
#         unshift_vocales = False

#         # Chequear si letra es consonante
        
#         for j in range(len(consonantes)-1,-1,-1):
#             if j - desplazamiento_consonantes < 0 and not unshift_consonantes:
#                 consonantes = consonantes + consonantes
#                 unshift_consonantes = True
#             if consonantes[j] == palabra[i]: 
#                 palabra_codifica[i] = consonantes[j - desplazamiento_consonantes]
        
#         for k in range(len(vocales)-1,-1,-1):
#             if k - desplazamiento_vocales < 0 and not unshift_vocales:
#                 vocales = vocales + vocales
#                 unshift_vocales = True
#             if vocales[k] == palabra[i]:  
#                 palabra_codifica[i] = vocales[k - desplazamiento_vocales]
        

#     respuesta = "".join(palabra_codifica);
#     return respuesta;



palabra_codificada = codificacion(palabra, consonantes, vocales, desplazamiento_consonantes, desplazamiento_vocales)
print('Palabra codificada: ',palabra_codificada);

# palabra_decodificada = decodificacion(palabra_codificada, consonantes, vocales, desplazamiento_consonantes, desplazamiento_vocales)
# print('Palabra decodificada: ',palabra_decodificada);