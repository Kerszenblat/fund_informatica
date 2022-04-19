#Ejercicio 1 
def potencias(numero):
    return print({numero: numero**2})

potencias(4)
potencias(2)
potencias(30)

#Ejercicio 2 
sum = 0

def sumatoria(sum, dic):
    for numero in dic:
        sum += numero
    return print(sum)

sumatoria(sum, {5, 4, 3, 2, 1})
sumatoria(sum, {6, 8, 12, 9})

#Ejercicio 3
def listar(lista_strings):
    longitud_lista = len(lista_strings)
    longitud_strings = []
    for list in lista_strings:
        longitud_strings.append(len(list))
    return print(longitud_lista, longitud_strings, lista_strings)

listar(["lara", "lar", "candela"])

#Ejercicio 4
string = []
intriger = []
boolean = []

def lista_mixta(lista):
    for dato in lista:
        if(type(dato) is str):
            nuevo__dato = dato.replace("a", "u")
            string.append(nuevo__dato)
        elif(type(dato) == int):
            intriger.append(dato)
        else:
            boolean.append(dato)
    return print(string, intriger, boolean)

lista_mixta(["lara", 20, True, "chau", False, "gabi", 1, 40, "sol", True])