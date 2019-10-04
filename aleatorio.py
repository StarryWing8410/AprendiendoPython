#Jesus Hector Murillo Villanueva
#25/09/2019

import random #Dentro de la basta libreria de python importamos el module,
#utilizando la instruccion import

numero1 = float(10.5) #Declaramos la variable de data type punto flotante o float

#La funcion te permite hacer una serie de instrucciones especificas, indicadas por nosotros o alguien mas,
#la cual se es llamada de una manera en especifico. Sirve como una manera de ahorro de trabajo, simplemente invocas la funcion,
#das los datos que en ella ya se piden y esta hara la tarea deseada.
def funcion ():
    numero2 = float(random.randrange(1,10)) #Se convierte en float el numero generado por random,
    #permitiendole sumarse con la variable que declaramos anteriormente

    mensaje = 'La suma de {} y {} es {}'

    print(mensaje.format(numero1,numero2,numero1+numero2)) #Se muestra el mensaje y junto a este
    #se hace la operacion para dar con el resultado deseado

funcion() #Se invica la funcion para elabora y se ejecuta