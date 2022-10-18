# Ejercicio 1 #
'''
Realizar un programa que inicialice una lista con 10 valores aleatorios (del 1 al 10) y
posteriormente muestre en pantalla cada elemento de la lista junto con su cuadrado y su cubo.
'''

import random

#Función que ejecuta la lista aleatoria
def lista_2_3():
    lst=[]
    for i in range(0,10):
        lst.append(random.randint(1,10))
    return lst
lista=lista_2_3()
print("Lista numeros: ", lista)

#Función que hace la lista de cuadrados
def lista_cuadrado(lst):
    lst_cuadrado=[]
    for i in lst:
        cuadrado= i*i
        lst_cuadrado.append(cuadrado)
        cuadrado=0
    return lst_cuadrado
print("Lista cuadrados: ", lista_cuadrado(lista))

#Función que hace la lista de cubos
def lista_cubo(lst):
    lst_cubo=[]
    for i in lst:
        cubo= i*i*i
        lst_cubo.append(cubo)
        cubo=0
    return lst_cubo
print("Lista cubos: ", lista_cubo(lista))
