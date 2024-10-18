import string
import random

minusculas_ascii = string.ascii_lowercase
print(minusculas_ascii)

mayusculas_ascii = string.ascii_uppercase
print(mayusculas_ascii)

numeros = string.digits
print(numeros)

def generarPassword(n):
    caracteres = minusculas_ascii + mayusculas_ascii + numeros

    password = ''.join(random.choices(caracteres, k=n))
    
    return password

for i in range(10, 20):
    print(generarPassword(i))
