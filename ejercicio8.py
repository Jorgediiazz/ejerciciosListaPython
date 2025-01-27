# Ejercicio 8 #
'''
Denifinir una estructura de datos con listas que permita guardar la temperatura mínima y máxima de 5 días. 
Realiza un programa que de la siguiente información:
     - La temperatura media de cada día
     - Los días con menos temperatura
     - Que permita leer una temperatura por teclado y muestre los días cuya temperatura máxima coincida con ella, en caso contrario mostrar un mensaje diciendo que no existe ningún día
     
'''
import random

#Funcion que genera una lista de temperaturas aleatorias de 5 dias
def listaTemperatura(n):
    lst=[]
    for i in range(0,n):
        min_=random.randint(-30,10)
        max_=random.randint(10,40)
        lst.append([min_,max_])
    return lst

#Funcion que calcula la temperatura media
def temperaturaMedia(lista):
    lst_media=[]
    for i in lista:
        media=(i[0]+i[1])/2
        lst_media.append(media)
    return lst_media

#Funcion que te da los dias con menos temperatura
def diasMenosTemperatura(lista):
    lista_minimos=[]
    tempmin=lista[0][0]
    for i in lista:
        if(i[0]<=tempmin):
            tempmin=i[0]
    print("Esta es la temperatura minima: ", tempmin)
    
    for i in range(0,len(lista)):
        if(tempmin==lista[i][0]):
            lista_minimos.append(i+1)
    return lista_minimos

#Funcion que te pide un temperatura y muestre los dias cuya temperatura maxima coincida
def buscarTemperaturaMaxima(lista1):
    temp = float(input("Dime la temperatura:"))
    
    lista_dias_max = []
    lista_max = []
    
    for i in lista1:
        #Se agregan todas las temperaturas máximas a una lista vacia
        lista_max.append(i[1])
    
    for i in range(0, len(lista_max)):
        if(lista_max[i] == temp):
            lista_dias_max.append(i+1)
            return lista_dias_max
    else:
        print("No existe ningun día con esa temperatura")

lista=listaTemperatura(5)
lista2=listaTemperatura(10)
lista3=listaTemperatura(0)

print("Esta es la lista de las temperaturas: ", lista)
print("Esta es la lista de la temperatura media: ", temperaturaMedia(lista))
print("Este es el dia/s con menos temperatura: ",diasMenosTemperatura(lista))
print(buscarTemperaturaMaxima(lista))
