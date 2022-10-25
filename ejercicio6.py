# Ejercicio 6 #
'''
Crea un programa que pida un número al usuario, un número de mes ( por ejemplo, el 4). 
El programa dirá cuántos días tiene (por ejemplo 30) y el nombre del mes. Debes usar listas. Nota: En una lista podemos guardar listas.
Para simplificarlo vamos a suponer que febrero tiene 28 días
'''

'''Pide al usuario un numero que este entre 1 y 12'''
def pedirMes():
    lst=[["Enero",31],["Febrero",28],["Marzo",31],["Abril",30],["Mayo",31],["Junio",30],["Julio",31],["Agosto",31],["Septiembre",30],["Octubre",31],["Noviembre",30],["Diciembre",31]]
    try:
        mes=int(input("Dime un numero: "))
        if(mes>12 or mes<1):
            print("No es valido")
        else:
            print(lst[mes-1][0], "tiene", lst[mes-1][1], "dias.")
    except:
        print("Tiene que ser un numero")
pedirMes()
