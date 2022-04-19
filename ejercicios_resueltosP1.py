#Ejercicio 1
def longitud(string):
    return print(len(string))

longitud("lara")

#Ejercicio 2
def imprimir(string):
    if(len(string) < 7):
        return print("Debe introducir un string con más de 7 caracteres")
    else:
        return print(string[5].upper(), string[6].upper())

imprimir("laraker")

#ejercicio 3
from re import S


def saludar(nombre, apellido):
    return print("¡Hola " + nombre + " " + apellido + ", espero que estes bien!")

saludar("lara", "ker")

#ejercicio 4
def persona(nombre, apellido1, apellido2):
    return print(nombre[0].upper(), apellido1[0].upper(), apellido2[0].upper())

persona("lara", "ker", "kerszenblat")

#Ejercicio 5
def promedio(num1, num2, num3):
    prom = (num1 + num2 + num3)/3
    return print(prom)

promedio(5, 3, 6)

#Ejercicio 6
def horas_y_minutos(minutos):
    if(minutos < 60):
        return print(str(minutos) + " minutos")
    else:
        min = int(minutos % 60)
        horas = int((minutos - min) / 60)
        string_minutos = str(min)
        string_horas = str(horas)
        return print(string_horas + " horas y " + string_minutos + " minutos")

horas_y_minutos(130)
horas_y_minutos(40)


