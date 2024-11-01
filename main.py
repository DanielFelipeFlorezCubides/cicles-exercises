# Escriba un programa que muestre la tabla de multiplicar del 1 al 10 del número ingresado por el usuario:

number = int(input('''Give me a number to show you it's table: '''))

for i in range(1,11):
    result = number * i
    print(f'{number} x {i} = {result}')