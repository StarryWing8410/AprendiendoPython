#Jesus Hector Murillo Villanueva
#25/09/2019

numero1 = input('numero1: ')
numero2 = input('numero2: ')
salida = 'Los numeros son: {} y {}. {}'

if numero1 == numero2: #Solo entra si se verifica que los numeros adquiridos son iguales
    print(salida.format(numero1, numero2, 'Los numeros son iguales'))
elif numero1 > numero2: #Solo entra si se verifica que el numero 1 es mayor que el 2
    print(salida.format(numero1, numero2, 'El mayor es el primer numero'))
else: #De otro modo al no cumplirse ninguna de las condiciones anteriores solo queda por cumplirse la ultima
    print(salida.format(numero1,numero2,'El mayor es el segundo'))