# Ejercicio 4 #
'''
Programa que declare una lista y la vaya llenando de núemros hasta que introducimos un número negativo.
Entonces se debe imprmir el vector (sólo los elementos introducidos)
'''

#Función
def lista():
    lst=[]
    try:
        while(True):
            n=int(input("Dime un numero: "))
            if(n > 0):
                lst.append(n)
            else:
                return lst
    except:
        print("Tiene que ser un numero")
print(lista())
