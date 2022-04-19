#Ejercicio 1 
def cada_linea(archivo, modo, letra):
    import os
    path = os.getcwd() + archivo
    sum = 0
    with open(path, modo) as arch:
        lista = arch.readlines()
        for palabras in lista:
            if(palabras[0] != letra):
                sum += 1
        return print(sum)

cada_linea("\ejercicio_1.txt", "r", "a")

#Ejercico 2 
def imprimir_lineas(archivo, modo, num_lineas):
    import os
    path = os.getcwd() + archivo
    with open(path, modo) as arch:
        lista = arch.readlines(num_lineas)
        return print(lista)


imprimir_lineas("\ejercicio_1.txt", "r", 10)

#Ejercicio 3 
