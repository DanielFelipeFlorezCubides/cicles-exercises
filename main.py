# Escriba un programa que genere todas las potencias de 2, 
# desde la 0-ésima hasta la ingresada por el usuario:
import math
exponential = int(input('Give me a n exponential number to combine it with 2: '))

for i in range(exponential+1):
    result = math.pow(2, i)
    print(f'The {i} exponential of 2 is: {result}')