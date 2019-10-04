# Jesus Hector Murillo Villanueva
# 02/10/2019

numero = int(input('Proporciona un numero que sea\nmultiplo de 3, 5 o 7: '))
#Se pide un numero que sea multiplo de los numeros indicados

#Se declara en variables el resultado esperado para cada uno de los casos haciendo de estos data type de valor booleano
multiplo3 = numero%3 == 0
multiplo5 = numero%5 == 0
multiplo7 = numero%7 == 0

#Se validan las condiciones operadas con el numero ingresadop por el usuario con la sentencia if 
if (multiplo3 or multiplo5 ) or multiplo7:
    print('Correcto')
else:
    print('Incorrecto')