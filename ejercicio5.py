# Ejercicio 5 #
'''
Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y 
posterior ordene los elementos de menor a mayor
'''
# Ejercicio 5 #
'''
Hacer un programa que inicialice una lista de números con valores aleatorios (10 valores), y 
posterior ordene los elementos de menor a mayor
'''
import random

def lista():
    cont=0
    lst=[]
    
    while(cont<10):
        numale=random.randint(0,100)
        cont+=1
        lst.append(numale)
        lst2=lst.copy() 
        lst2.sort()
    return lst, lst2
print(lista())
