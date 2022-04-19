#ejercicio 1
def firstLetter(string):
    try:
        letter = string[0]
        if(letter == letter.upper()):
            return print("La primera letra de mi string es una mayuscula")
        elif(letter == letter.lower()):
            return print("La primera letra de mi string es una minuscula")  
    except:
        return print("Debes introducir un dato de tipo string")

firstLetter("lara")
firstLetter("Lara")
firstLetter(1)

#Ejercicio 2
def my_number_is(number):
    try:
        if(number >= 1):
            if(number % 2 == 0):
                return print("Mi numero es positivo y es par")
            else:
                return print("Mi numero es positivo y es impar")
        elif(number == 0):
            return print("Mi numero es 0 y es par")
        else:
            return print("Mi numero es negativo")
    except:
       return print("Ocurrio un error. Asegurate de introducir un numero")

my_number_is(0)
my_number_is(5)
my_number_is(-3)
my_number_is("1")

#ejercicio 3
def dados(number):
    try:
        if(number > 6 or number < 1):
            return print("Debes introducir un numero menor o igual a 6 y mayor o igual a 1")
        else:
            if(number == 1): 
                return print("2")
            elif(number == 2): 
                return print("3")
            elif(number == 3): 
                return print("4")
            elif(number == 4): 
                return print("5")
            elif(number == 5): 
                return print("6")
            elif(number == 6): 
                return print("1")
    except:
        return print("Debes introducir un numero")

dados(1)
dados(2)
dados(3)
dados(4)
dados(5)
dados(6)
dados("1")

#Ejercicio 4
def transporte_internacional(ubicacion, costo_por_gramo, kilo):
    if(kilo < 5 and kilo > 0):
        if(ubicacion == "América del Sur"):
            return print("El costo de servicio sale " + costo_por_gramo)
        elif(ubicacion == "América Central"):
            return print("El costo de servicio sale " + costo_por_gramo)
        elif(ubicacion == "América del Norte"):
            return print("El costo de servicio sale " + costo_por_gramo)
        elif(ubicacion == "Europa"):
            return print("El costo de servicio sale " + costo_por_gramo)
        elif(ubicacion == "Asia"):
            return print("El costo de servicio sale " + costo_por_gramo)
        else:
            return print("No trabajamos en ese continente. Intenta introducir un continente valido que son los siguientes: América del Sur, América Central, América del Norte, Europa o Asia")
    else:
        return print("No realizamos pedidos mayores o iguales a 5kg.")

transporte_internacional("América del Sur", "10.00 dolares", 1)
transporte_internacional("América Central", "15.00 dolares", 2)
transporte_internacional("América del Norte", "18.00 dolares", 3)
transporte_internacional("Europa", "24.00 dolares", 4)
transporte_internacional("Asia", "30.00 dolares", 2)
transporte_internacional("América del Sur", "10.00 dolares", 6)
transporte_internacional("América del Sur", "10.00 dolares", 0)


#Ejercicio 5
def dia_de_semana(number):
    if(number >=1 and number <= 7):
        return print(number)
    else:
        return print("El numero esta fuera de rango. Vuelve a intentarlo.")

dia_de_semana(1)
dia_de_semana(3)
dia_de_semana(5)
dia_de_semana(0)
dia_de_semana(10)

#ejercicio 6
lista_1 = ["lara", "kerszenblat", "20 años", "1.67 de altura", "50 kg de peso"]
lista_2 = []

for item in reversed(lista_1):
    lista_2.append(item)

print(lista_2)


#ejercicio 7
lista = []
i = 14

while i > 0:
    lista.append(i)
    i -= 1
    if i == 0:
        print(lista)
        break

#ejercicio 8
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list3 = []

def lists(list_one, list_two, list_three):
    for list in range(0, 4):
        list_three.append(list_one[list] + list_two[list])
    return print(list_three)

lists(list1, list2 ,list3)

#ejercicio 9
#ejercicio 10 
#ejercicio 11
#ejercicio 12 

#ejercicio 13
def esMultiplo(entero1, entero2):
    if(entero1 % entero2 == 0):
        return print("El primer entero es multiplo del otro")
    if(entero2 % entero1 == 0):
        return print("El segundo entero es multiplo del otro")
    return print("Ninguno es multiplo del otro")

def enteros(entero1, entero2):
    esMultiplo(entero1, entero2)

enteros(8, 4)
enteros(2, 6)
enteros(12, 10)

#ejercicio 14

#ejercicio 15

socios = [
    {"number": 1, "name": "Florencia Ocampo", "entry": "14/09/2001", "payment": "No tiene las coutas al día"},
    {"number": 2, "name": "David Estévez", "entry": "14/09/2001", "payment": "No tiene las coutas al día"},
    {"number": 3, "name": "Sofía Cáceres", "entry": "14/09/2001", "payment": "No tiene las coutas al día"}    
]

def count_members(members):
    return print(len(members))

count_members(socios)

def payment(id_user, members):
    for member in members:
        if(member["number"] == id_user):
            member["payment"] = "Si tiene las cuotas al día"
            return print(member["payment"])

payment(1, socios)

def changingEntries(newDate, members):
    for member in members:
        if(member["entry"] == "14/09/2001"):
            member["entry"] = newDate
    return print(members)

changingEntries("22/10/2017", socios)

def deleteMember(name, members, id):
    for member in members:
        if(member["name"] == name):
            members.pop(id - 1)
    return print(members)

deleteMember("Florencia Ocampo", socios, 1)

def printAll(members):
    return print(members)

printAll(socios)