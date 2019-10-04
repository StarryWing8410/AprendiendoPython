#Jesus Hector Murillo Villanueva
#25/09/2019

numero = input('dame un numero del 1 al 9: ')
numero = int(numero) #Se pide un numero y se transforma a int

for i in range(1,11): # for repite un bloque de codigo cierta cantidad de veces que se declare o se indique
    
    salida = '{} x {} = {}' # i itera la cantidad de veces indicada y se itera el bloque de la variable salida y print
    #en el cual se opera para dar el resultado de la tabla
    print(salida.format(numero,i,i*numero))