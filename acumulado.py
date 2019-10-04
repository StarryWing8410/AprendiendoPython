# Jesus Hector Murillo Villanueva
# 02/10/2019

acumulado = 0 
numero = ''
#Se declaran las variables a trabajar en el while, python es flexible con los data type
#asi que se puede usar como esta declarado o de manera acumulado=int(0) y numero=str('')

while True:
    numero = input('Da un numero entero: ')
    if numero == '': #Si no se registra ningun dato sale de la sentencia con la funcion break.
        #Esto se registra por el data type, al ser str se registra si existe algun dato en cualquier posicion de la cadena
        print('No se proporciono un numero.\nSalida del programa')
        break
    else:
        #Al detectar un dato lo transforma a integer haciendo que sume los numeros dados y declarandolos en una variable 
        #en la cual se acumularan los datos dados e imprimiendo el monto acumulado
        acumulado += int(numero)
        print('Monto acumulado: {}'.format(acumulado))