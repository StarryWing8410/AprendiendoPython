#Jesus Hector Murillo Villanueva
#25/05/2019

numero = '5678' #Se declara la variable de tipo string con una serie de digitos

print(type(numero)) #Type verifica el tipo de dato que es la variable que se 
#se pone entre parentesis, junto a print que es el que muestra un mensaje 
#en la consola, muestra el data type de la variable

numero = int(numero) #Cambiamos el data type de la variable usando integer

print(type(numero)) #Mostramos el nuevo data type de la variable

print('El numero utilizado es {}'.format(numero)) # Mandamos un mensaje junto al cual concatenamos 
#la variable que utilizamos