# Ejercicio 7 #
'''
Programa que declare tres listas 'lista1', 'lista2' de cinco enteros cada uno. 
Calcule lista3 = lista1 + lista2, por ejemplo 
           lista1 = [1, 2, 3, 4, 5]
        +  lista2 = [3, 2, 4, 5, 1]
           --------------------------
           lista3 = [4, 4, 7, 9, 6]
           
'''

import random
#Función que hace 2 listas aleatorias 
def ListaRandom(n):
    lst = []
    for i in range(0, n):
        lst.append(random.randint(0,10))
    return lst
# Función que suma las 2 listas
def sumaLista(lista1, lista2):
    lista3 = []
    
    if(len(lista1) == len(lista2)):
        for i in range(0, len(lista1)):
            lista3.append(lista1[i] + lista2[i])
    else:
        print("Tienen que tener el mismo tamaño")
    
    return lista3

lst1 = ListaRandom(5)
print(lst1)
lst2 = ListaRandom(5)
print(lst2)
print(sumaLista(lst1, lst2))
