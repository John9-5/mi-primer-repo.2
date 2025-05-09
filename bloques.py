#!/usr/bin/env python
import string
lista_ejemplo = ["fox", "box", "dog", "cat", "car", "bus"]
n = 3

class Palabra:
    abc = string.ascii_lowercase
    def __init__(self, string_palabra):
        self.frecuencias = {}
        for letra in self.abc:
            count = string_palabra.count(letra)
            if count != 0:
                self.frecuencias[letra] = count
    def get_frecuencia(self, letra):
        return self.frecuencias.get(letra,0)

def palabras_a_objetos(lista_palabras):
    lista_Palabra = []
    for palabra in lista_palabras:
        lista_Palabra.append(Palabra(palabra))
    return lista_Palabra

def seleccion_en_pares(lista_Palabras,letra):
    lista_Palabras_filtradas = []
    i = 0
    while i+1 < len(lista_Palabras):
        if lista_Palabras[i].get_frecuencia(letra) > lista_Palabras[i+1].get_frecuencia(letra):
            lista_Palabras_filtradas.append(lista_Palabras[i])
        else:
            lista_Palabras_filtradas.append(lista_Palabras[i+1])
        i+=2
    return lista_Palabras_filtradas

def main(lista_palabras=lista_ejemplo, N=n, abc=string.ascii_lowercase):
    lista_bloques = []
    lista_Palabras = palabras_a_objetos(lista_palabras) #convierte lista de strings a lista de objetos
    for i in range(len(abc)): #Itera con i desde 0 hasta la longitud del abecedario
        lista_Palabras_filtradas = seleccion_en_pares(lista_Palabras, abc[i]) #Recibe una lista de objetos y una letra, selecciona cual objeto tiene mayor frecuencia de la letra de entre un par 
        frecuencia = 0
        for j in range(N): #El ciclo sumará el atributo "abc[i]" de las primeras N palabras
            frecuencia += lista_Palabras_filtradas[j].get_frecuencia(abc[i])
        lista_bloques.append(frecuencia)
    print(lista_bloques)

if __name__ == "__main__":
    main()
