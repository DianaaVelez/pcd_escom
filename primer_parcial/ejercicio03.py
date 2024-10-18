# Crear un programa que genere 100 numeros aleatorios entre 1 y 1000
# inserte en un alista los pares y en otr alos impares
# Imprimir ambas listas y el tamaño de las mismas

import random

pares = []
impares = []

for _ in range(100):
    numero = random.randint(1, 1000)  
    if numero % 2 == 0:
        pares.append(numero) #agregar a la lista de pares
    else:
        impares.append(numero)  #lista imapres

print("Números pares:", pares)
print("Tamaño de la lista de pares:", len(pares))
print("Números impares:", impares)
print("Tamaño de la lista de impares:", len(impares))
