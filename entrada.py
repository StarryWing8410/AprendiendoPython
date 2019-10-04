#Jesus Hector Murillo Villanueva
#25/09/2019

entrada = input('ingresa un numero')
print(type(entrada))
# Se declara la variable pidiendo un dato de tipo int, ademas de imprimir el data type

entero = (entrada.isdigit() and entrada.find('.'))
# Se declara la variable la cual se validara en la sentencia if con el dato preguntado

if (entero):
    print('es entero, muy bien') #Se ejecuta solo si se cumple la condicion
else:
    print('no es entero, intenta de nuevo') #Se ejecuta si no se cumple la condicion 
