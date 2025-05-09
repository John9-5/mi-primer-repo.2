#!/usr/bin/env python

lista_ejemplo = ["fox", "box", "dog", "cat", "car", "bus"]
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
n = 3

class Palabra:
    def __init__(self, string_palabra):
        abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        for letra in abc:
            frecuencia = string_palabra.count(letra)
            setattr(self, letra, frecuencia)
        

def lista_palabras_obj(lista_palabras):
    lista_obj = []
    for palabra in lista_palabras:
        lista_obj.append(Palabra(palabra))
    return lista_obj

def ordenar_palabras_por_letra(lista_obj, letra):
    lista_ordenada = sorted(lista_obj, key=lambda palabra: getattr(palabra, letra), reverse=True)
    return lista_ordenada

def listas_de_palabras_ordenadas_por_letra(lista_obj, lista_letras=abc):
    listas_ordenadas = []
    for letra in lista_letras:
        listas_ordenadas.append(ordenar_palabras_por_letra(lista_obj, letra))
    return listas_ordenadas

def suma_frecuencias(lista_ordenada, N, letra):
    suma = 0
    for i in range(N):
        suma += getattr(lista_ordenada[i], letra)
    return suma

def numero_bloques(listas_ordenadas, N=n):
    lista_frecuencias = []
    for i in range(len(abc)):
        lista_frecuencias.append(suma_frecuencias(listas_ordenadas[i], N, abc[i]))
    return lista_frecuencias

lista_Palabras = lista_palabras_obj(lista_ejemplo)
listas_ordenadas = listas_de_palabras_ordenadas_por_letra(lista_Palabras)
print(numero_bloques(listas_ordenadas))
