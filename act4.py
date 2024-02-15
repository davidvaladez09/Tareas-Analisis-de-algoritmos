#Equipo 11
#Back Davdi Valadez Gutierrez
#Front Enrique Eduardo Lozano Aceves
import pandas as pd

def recorridoCadena(cadena, longitud_subcadena, inicio_subcadena):
    subcadenas = []
    for i in range(inicio_subcadena, len(cadena), longitud_subcadena):
        subcadenas.append(cadena[i:i+longitud_subcadena])
    return subcadenas

def modificarCaracter(cadena, posicion, nuevo_caracter):
    if posicion < len(cadena):
        cadena = cadena[:posicion] + nuevo_caracter + cadena[posicion+1:]
        return cadena
    else:
        return cadena

cadena = 'TGTAGTGCAGTGGCGTGATCTTGGCTCACTGCAGCCTCCACCTTAGAGCAATCCTCTTGCCTCATCCTCCCGGGTAGTTGGGACTACATGTGCATGCCACATGCCTGGCTAATTTTTGTATTTTTAGTA' #input("Ingrese la cadena: ")
longitud_recorrido = 2
longitud_subcadena = 5
inicio_subcadena = 0

subcadenas = recorridoCadena(cadena, longitud_subcadena, inicio_subcadena)

cadenas_modificadas = [cadena]

modificaciones = []

for n in range(2):
    posicion_modificar = int(input("Ingrese la posición a modificar: "))
    nuevo_caracter = input("Ingrese el nuevo caracter: ")

    cadena_modificada = modificarCaracter(cadenas_modificadas[-1], posicion_modificar, nuevo_caracter)
    cadenas_modificadas.append(cadena_modificada)

    print("Cadena modificada:", cadena_modificada)

    if cadena_modificada not in subcadenas:
        modificaciones.append(cadena_modificada)

print("Cadenas modificadas:", ', '.join(cadenas_modificadas))
print("Subcadenas:")

for subcadena in subcadenas:
    print(subcadena)

print(subcadenas)
print(cadenas_modificadas)

df = pd.DataFrame(subcadenas, columns=["Subcadenas"])

# Guardar el DataFrame en un archivo CSV
df.to_csv("archivo.csv", index=False)
