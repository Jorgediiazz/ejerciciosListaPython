# Ejercicio 10 #
'''
Crear un programa que cree un matriz de 5 x 5 con números aleatorios
'''
import random

#Funcion que genera una lista aleatoria
def generarListaRandom():
    lst=[]
    for i in range(0,5):
        lst.append(random.randint(0,10))
    return lst

#Funcion que genera una lista de lista aleatoria
def generaMatrizAleatoria():
    lst=[]
    for i in range(0,5):
        lst.append(generarListaRandom())
    return lst

def sumaMatrices(matriz_a,matriz_b):
    lst_suma=[]
    suma=0
    print("Matriz 1:",matriz_a)
    print("Matriz 2:",matriz_b)
    for i in range(0, len(matriz_a)):
        lst_aux=[]
        #print("Iteración " , i)
        #print(matriz_a[i])
        #print(matriz_b[i])
        for j in range(0,len(matriz_a[i])):
            #print("Matriz_a: ", matriz_a[i][j])
            #print("Matriz_a: ", matriz_b[i][j])
            suma_aux=matriz_a[i][j]+matriz_b[i][j]
            lst_aux.append(suma_aux)
        lst_suma.append(lst_aux)
    return lst_suma
    
def restaMatrices(matriz_a,matriz_b):
    lst_suma=[]
    suma=0
    for i in range(0, len(matriz_a)):
        lst_aux=[]
        #print("Iteración " , i)
        #print(matriz_a[i])
        #print(matriz_b[i])
        for j in range(0,len(matriz_a[i])):
            #print("Matriz_a: ", matriz_a[i][j])
            #print("Matriz_a: ", matriz_b[i][j])
            suma_aux=matriz_a[i][j]-matriz_b[i][j]
            lst_aux.append(suma_aux)
        lst_suma.append(lst_aux)
    return lst_suma
    
matriz_a=generaMatrizAleatoria()
matriz_b=generaMatrizAleatoria()
print("Suma:  ",sumaMatrices(matriz_a,matriz_b))
print("Resta: ",restaMatrices(matriz_a,matriz_b))

