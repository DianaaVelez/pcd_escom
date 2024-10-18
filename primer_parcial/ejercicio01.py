import string

caracteres_ascii = string.ascii_letters
print(caracteres_ascii)

verificar = lambda cadena: all(caracter in caracteres_ascii for caracter in cadena)

cadena1 = "Esto es una cadena$"
print(verificar(cadena1))  

