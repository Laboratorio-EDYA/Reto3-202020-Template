"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller
from DISClib.ADT import orderedmap as om
assert config
from time import process_time
from App import controller as ctrl



"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion hace la solicitud 
al controlador para ejecutar la operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

accidentesAll = 'US_Accidents_Dec19.csv'
accidentes2016 = 'us_accidents_dis_2016.csv'
accidentes2017 = 'us_accidents_dis_2017.csv'
accidentes2018 = 'us_accidents_dis_2018.csv'
accidentes2019 = 'us_accidents_dis_2019.csv'

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("-"*75)
    print("Bienvenido")
    print("1- Inicializar Analizador y cargar información de accidentes")
    print("2- Conocer los accidentes en una fecha")
    print("3- Conocer los accidentes anteriores a una fecha")
    print("4- Conocer los accidentes en un rango de fechas")
    print("5- Conocer el estado con mas accidentes")
    print("6- Conocer los accidentes por rango de horas")
    print("7- Conocer la zona geográfica mas accidentada")
    print("8- Usar el conjunto completo de datos")
    print("0- Salir")
    print("-"*75)

# Menu principal
def cargarporanio(cont, anio):
    if cont[anio][0] != None:
        accidentfile = cont[anio][1]
        print("\nCargando información de accidentes .....")
        controller.loadData(cont[anio][0], accidentfile)
        print('Crimenes cargados: ' + str(controller.accidentsSize(cont[anio][0])))
        print('Altura del arbol: ' + str(controller.indexHeight(cont[anio][0])))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont[anio][0])))
        print('Menor Llave: ' + str(controller.minKey(cont[anio][0])))
        print('Mayor Llave: ' + str(controller.maxKey(cont[anio][0])))

def cargarAccidentes(cont, anio):
    t1_start = process_time() #tiempo inicial
    anios = input("\nEscriba el año de los accidentes que desea cargar (entre 2016 y 2019)\n* Digita 0 para cargar todos los archivos *\n-> ")
    if anios == '2016':
        cont['2016'] = [ctrl.init(),accidentes2016]
        anio['anio'] = '2016'
        anio['type'] = 0
    elif anios == '2017':
        cont['2017'] = [ctrl.init(),accidentes2017]
        anio['anio'] = '2017'
        anio['type'] = 0
    elif anios == '2018':
        cont['2018'] = [ctrl.init(),accidentes2018]
        anio['anio'] = '2018'
        anio['type'] = 0
    elif anios == '2019':
        cont['2019'] = [ctrl.init(),accidentes2019]
        anio['anio'] = '2019'
        anio['type'] = 0
    elif anios == '0': 
        anio['anio'] = '0'
        anio['type'] = 1
        cont['2016'] = [ctrl.init(),accidentes2016]
        cont['2017'] = [ctrl.init(),accidentes2017] 
        cont['2018'] = [ctrl.init(),accidentes2018]
        cont['2019'] = [ctrl.init(),accidentes2019]
    #try:
    cargarporanio(cont,'2016')
    cargarporanio(cont,'2017')
    cargarporanio(cont,'2018')
    cargarporanio(cont,'2019')
    #except:
    #    print('¡¡KELLY ASEGURESE DE DIGITAR EL AÑO BIEN!!')
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos ")
    return cont


def accidentesPorFecha(cont, anio):   #Req. 1
    t1_start = process_time() #tiempo inicial
    year = input('Digita el año YYYY: ')
    month = input('Digita el mes MM: ')
    day = input('Digita el día DD: ')
    date = year.strip() + '-' + month.strip() + '-' + day.strip()
    data = ctrl.accidentesPorFecha(cont, date, anio)
    print('El total de accidentes reportados en la fecha '+date+' fue de ',data['total'],' accidentes')
    print('Total según severidad: ')
    print('Severidad 1: ',data['1'])
    print('Severidad 2: ',data['2'])
    print('Severidad 3: ',data['3'])
    print('Severidad 4: ',data['4'])
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos ")


def accidentesAnteriores (cont, anio):   #REQ. 2
    t1_start = process_time() #tiempo inicial
    year = input('Digita el año YYYY: ')
    month = input('Digita el mes MM: ')
    day = input('Digita el día DD: ')
    date = year.strip() + '-' + month.strip() + '-' + day.strip()
    data = ctrl.accidentesAnteriores(cont, date, anio)
    print(data[0], " accidentes fueron reportados antes de la fecha " +date)
    print("En " ,str(data[1][0]).replace('datetime.date(','').replace(')',''), " fue el día con mayor accidentalidad")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos ")


def accidentesEnUnRangoDeFecha(cont, anio):   #REQ. 3
    t1_start = process_time() #tiempo inicial
    initialDate = input("Digita la fecha inicial en formato YYYY-MM-DD: ")
    finalDate = input("Digita la fecha final en formato YYYY-MM-DD: ")
    data = ctrl.accidentesEnUnRangoDeFecha(cont,initialDate,finalDate, anio)
    print("La cantidad total de accidentes ocurridos desde " +initialDate+ " hasta " +finalDate+ " fueron" ,data[0], "accidentes" )
    print("La severidad" ,data[1][0], "fue la más común en estos accidentes, con un total de ",data[1][1])
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos ")


def conocerEstado (cont, anio):    #REQ. 4
    t1_start = process_time() #tiempo inicial
    initialDate = input("Digita la fecha inicial en formato YYYY-MM-DD: ")
    finalDate = input("Digita la fecha final en formato YYYY-MM-DD: ")
    data = ctrl.conocerEstado(cont,initialDate,finalDate, anio)
    print("El estado con más accidentes reportados es" ,data[1][0])
    print("La fecha donde hubo más accidentes fue" ,str(data[0][0]).replace('datetime.date(','').replace(')',''), 'con ',data[0][1], 'accidentes')
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos ")

def conocerHoras (cont, anio):   #REQ. 5
    t1_start = process_time() #tiempo inicial
    initialHour = ''
    finalHour = ''
    initialHourH = int(input('Digita las horas de la hora inicial en formato HH: '))
    initialHourM = int(input('Digita los minutos de la hora inicial en formato MM: '))
    finalHourH = int(input('Digita las horas de la hora final en formato HH: '))
    finalHourM = int(input('Digita los minutos de la hora final en formato MM: '))
    if initialHourM > 60 or initialHourH > 24 or finalHourM > 60 or finalHourH > 24:
        print('¡¡ KELLY, UNA HORA TIENE 60 MINUTOS Y UN DÍA 24 HORAS !!')
    else:
        if initialHourM < 15:
            initialHourM = '00'
            initialHour = str(initialHourH) + ':' + initialHourM
        elif (initialHourM >= 15 and initialHourM <= 45) or initialHourM == 30:    
            initialHourM = '30'
            initialHour = str(initialHourH) + ':' + initialHourM
        elif initialHourM <= 60:
            initialHourM = '00'
            initialHourH += 1
            initialHour = str(initialHourH) + ':' + initialHourM
        if finalHourM < 15:
            finalHourM = '00'
            finalHour = str(finalHourH) + ':' + finalHourM
        elif (finalHourM >= 15 and finalHourM <= 45) or finalHourM == 30:
            finalHourM = '30'
            finalHour = str(finalHourH) + ':' + finalHourM
        elif finalHourM <= 60:
            finalHourM = '00'
            finalHourH += 1
            finalHour = str(finalHourH) + ':' + finalHourM
        data = ctrl.conocerHoras(cont, initialHour, finalHour, anio)
    print('Desde las '+initialHour+' hasta las '+finalHour+', se registraron ',data[0]['total'],' accidentes')
    print('Clasificados por severidad: ')
    print('Severidad 1:   ',data[0]['1'],' accidentes')
    print('Severidad 2:   ',data[0]['2'],' accidentes')
    print('Severidad 3:   ',data[0]['3'],' accidentes')
    print('Severidad 4:   ',data[0]['4'],' accidentes')
    print('Estos accidentes representan el ',data[1],'% de la totalidad de accidentes registrados')
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos ")

def conocerZonaGeografica (cont,anio):
    t1_start = process_time() #tiempo inicial
    latitud = float(input("Digita la latitud: ").replace('.',''))
    longitud = float(input("Digita la longitud: ").replace('.',''))
    radio = float(input("Digita la distancia del radio en km (recuerde que un grado es 111,12km): "))
    x = ctrl.conocerZonaGeografica(cont,latitud,longitud,radio,anio)
    print("Hay ",x, " accidentes en el radio: ",radio)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos ")
    #111.12km

def main():
    cont = {}
    anio = {}
    while True:
        printMenu()
        inputs = int(input('Seleccione una opción para continuar\n-> '))

        if inputs == 1:   #Inicio y carga
            print("\nInicializando.....") 
            # cont es el controlador que se usará de acá en adelante
            cont = {'2016': [None], '2017': [None], '2018': [None],'2019': [None]}
            cargarAccidentes(cont, anio)

        elif inputs == 2:   #Req. 1
            print("Buscando accidentes en un rango de fechas\n ")
            if cont == None:
                print('¡KELLY CARGUE EL ARCHIVO PRIMERO!')
            else:
                accidentesPorFecha(cont, anio)
        elif inputs == 3:   #Req. 2
            print("Conocer los accidentes anteriores a una fecha\n")
            if cont == None:
                print('¡KELLY CARGUE EL ARCHIVO PRIMERO!')
            else:
                accidentesAnteriores (cont, anio)
                

        elif inputs == 4:   #Req. 3
            print('Conocer los accidentes en un rango de fechas\n ')
            if cont == None:
                print('¡KELLY CARGUE EL ARCHIVO PRIMERO!')
            else:
                print("-"*50)
                accidentesEnUnRangoDeFecha(cont, anio)

        elif inputs == 5:   #Req. 4
            print("Conocer el estado con mas accidentes\n")
            if cont == None:
                print('¡KELLY CARGUE EL ARCHIVO PRIMERO!')
            else:
                conocerEstado(cont, anio)

        elif inputs == 6:   #Req. 5
            print("\nRequerimiento No 5 del reto 3: ")
            if cont == None:
                print('¡KELLY CARGUE EL ARCHIVO PRIMERO!')
            else:
                conocerHoras(cont, anio)

        elif inputs == 7:   #Req. 6*
            print("\nRequerimiento No 6 del reto 3: ")
            if cont == None:
                print('¡KELLY CARGUE EL ARCHIVO PRIMERO!')
            else:
                conocerZonaGeografica(cont,anio)

        elif inputs == 8:   #Req. 7*    
            print("\nRequerimiento No 7 del reto 3: ")
            if cont == None:
                print('¡KELLY CARGUE EL ARCHIVO PRIMERO!')

        elif inputs == 0:
            sys.exit(0)

        else:
            print("Opción incorrecta .....")
main()
