#Jesus Hector Murillo Villanueva
#25/09/2019

for i in range(1,11):
    encabezado = 'TABLA DEL {}'
    print(encabezado.format(i))
    # Este for itera este bloque para que cada que de la vuelta se imprima el encabezado
    #de la tabla que se va a imprimir 
    print() #El print solo es un salto de linea, en este caso para que se vea mejor lo que se 
    #va a imprimir

    for j in range(1,11):
        salida = '{} X {} = {}'
        print(salida.format(i,j,i*j)) #La j es el elemento de la tabla en este bloque
        #se imprime la tabla, el i esta declarado como la tabla que se imprimira,
        #ademas se hace la operacion dentro del print para dar el resultado de la tabla

    else:
        print() #Salto de linea para iniciar la otra tabla