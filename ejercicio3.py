# Ejercicio 3 #
'''
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre 0 y 10).
A continuación debe mostrar todas las notas, la nota media, la nota más alta que ha sacado y la menor
'''
def lista_caracteres():
    lst=[]
    for i in range(0,5):
        cadena=float(input("Dime una nota: "))
        if(cadena<11):
            lst.append(cadena)
    return lst
print(lista_caracteres())

def nota_media(lst):
    acumulador=0
    for i in lst:
        acumulador += i
    resultado= acumulador/len(lst)
    return resultado
media=nota_media(lista_caracteres())
print("La nota media es :", media)

def nota_alta(lst):
    acumulador=0
    for i in lst:
        if(i>acumulador):
            acumulador=i
    return acumulador
alta=nota_alta(lista_caracteres)
print("La nota alta es :", alta)

def nota_baja(lst):
    acumulador=11
    for i in lst:
        if(i<acumulador):
            acumulador=i
    return acumulador
baja=nota_baja(lista_caracteres)
print("La nota baja es :", baja)
