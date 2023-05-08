import random
from ClaseRegistro import registro
def menu(registros_mensuales):
    cont=0
    acutemp=0
    tempmax=0
    tempmin=99999999
    print('Ingrese alguna de las siguientes opciones:\n1# Mostrar datos\n2# Temperatura promedio\n3# Mostrar datos por/h')
    opcion = input()
    if opcion == 1:
        for d, registros_diarios in enumerate(registros_mensuales):
            for h, registro in enumerate(registros_diarios):
                if registro is not None:
                    tempaux = registro.get_temp() 
                    if tempaux > tempmax:
                        tempmax = tempaux 
                        diamax = d
                        horamax = h
                    if tempaux < tempmin:
                        tempmin = tempaux
                        diamin = d
                        horamin = h    
        print(f'El dia {diamin}, hora {horamin} hicieron {tempmin}º de temperatura minima')
        print(f'El dia {diamax}, hora {horamax} hicieron {tempmax}º de temperatura maxima')

    elif opcion == 2:
        hora = int(input("\n Ingresar hora del dia: "))
        for d, registros_diarios in enumerate(registros_mensuales):
            registro = registros_diarios[hora]
            if registro is not None:
                cont+=1
                temp = int(registro.gettemp())
                acutemp =acutemp+ temp
        if cont>0:
            prom = acutemp + cont
            print (f"la temperatura promedio mensual de la hora", hora , "es:",prom)
        else:
            print ("No hay registro en esa hora")
    elif opcion == 3:
        condicion = 0
        dia= int(input("Ingresar dia a mostrar: "))
        registros_diarios = registros_mensuales[dia]
        for h, registro in enumerate (registros_diarios):
            if registro is not None: 
                if condicion == 0:
                    print('hora temperatura     humedad   presion')
                    condicion = 1
                print (f'{h}        {registro.get_temp()}     {registro.get_hum()}      {registro.get_presion()}')     