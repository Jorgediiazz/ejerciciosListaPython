# Ejercicio 2
'''
Crea una lista e inicializala con 5 cadenas de caracteres leídas por teclado. 
Copia los elementos de la lista en otra lista pero en orden inverso, y muestra sus elementos por la pantalla.
'''

def lista_caracteres():
    lst=[]
    for i in range(0,5):
        cadena=str(input("Dime una palabra: "))
        lst.append(cadena)
    return lst
lista=lista_caracteres()
lista2=lista.copy()
lista2.reverse()
print(lista)
print(lista2)


'''
def lista_inversa(lst):
    lista=lst.reverse()
print(lista)'''
