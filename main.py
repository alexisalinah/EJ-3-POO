import csv
from ClaseRegistro import registro
from menu import menu



if __name__ == "__main__":
    archivo = open('registro.csv')
    reader = csv.reader(archivo,delimiter=';')
    next(reader)
    registros_mensuales = []
    dias_en_mes = 30
    horas_en_dia = 24

    for dia in range(dias_en_mes):
        registros_diarios = []
        for hora in range(horas_en_dia):  
            registros_diarios.append(None)
        registros_mensuales.append(registros_diarios)

    for fila in reader:
        print(fila)
        row = fila[2].split(',')
        temp = int(row[0])
        hum = int(row[1])
        presion = int(row[2])
        Registro = registro(temp,hum,presion)
        registros_mensuales[int(fila[0])][int(fila[1])] = Registro
        
    menu(registros_mensuales)
    