# Ejercicio 3 #
'''
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10).
A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor
'''
#Función para la lista de notas
def lista_caracteres():
    lst=[]
    for i in range(0,5):
        cadena=float(input("Dime una nota: "))
        if(cadena<11 and cadena>-1):
            lst.append(cadena)
    return lst

#Funcion para la nota media
def nota_media(lst):
    acumulador=0
    for i in lst:
        acumulador += i
    resultado= acumulador/len(lst)
    return resultado

#Función para la nota alta
def nota_alta(lst):
    acumulador=0
    for i in lst:
        if(i>acumulador):
            acumulador=i
    return acumulador

#Función para la nota baja
def nota_baja(lst):
    acumulador=11
    for i in lst:
        if(i<acumulador):
            acumulador=i
    return acumulador


lst=lista_caracteres()
#Mostramos la lista
print(lst)
#Mostramos la nota media
print("La nota media es :", nota_media(lst))
#Mostramos la nota alta
print("La nota alta es :", nota_alta(lst))
#Mostramos la nota baja
print("La nota baja es :", nota_baja(lst))
