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

def cargarAccidentes(cont):
    t1_start = process_time() #tiempo inicial
    anio = int(input("\nEscriba el año de los accidentes que desea cargar (entre 2016 y 2019)\n-> "))
    if anio == 2016:
        accidentfile = accidentes2016
    elif anio == 2017:
        accidentfile = accidentes2017
    elif anio == 2018:
        accidentfile = accidentes2018
    elif anio == 2019:
        accidentfile = accidentes2019
    elif anio == 0:
        accidentfile = accidentesAll
    try:
        print("\nCargando información de accidentes .....")
        controller.loadData(cont, accidentfile)
        print('Crimenes cargados: ' + str(controller.accidentsSize(cont)))
        print('Altura del arbol: ' + str(controller.indexHeight(cont)))
        print('Elementos en el arbol: ' + str(controller.indexSize(cont)))
        print('Menor Llave: ' + str(controller.minKey(cont)))
        print('Mayor Llave: ' + str(controller.maxKey(cont)))
    except:
        print('¡¡KELLY ASEGURESE DE DIGITAR EL AÑO BIEN!!')
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos ")


def accidentesPorFecha(cont):   #Req. 1
    t1_start = process_time() #tiempo inicial
    year = input('Digita el año YYYY: ')
    month = input('Digita el mes MM: ')
    day = input('Digita el día DD: ')
    date = year.strip() + '-' + month.strip() + '-' + day.strip()
    data = ctrl.accidentesPorFecha(cont, date)
    print('El total de accidentes reportados en la fecha '+date+' fue de ',data['total'],' accidentes')
    print('Total según severidad: ')
    print('Severidad 1: ',data['1'])
    print('Severidad 2: ',data['2'])
    print('Severidad 3: ',data['3'])
    print('Severidad 4: ',data['4'])
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos ")


def accidentesAnteriores (cont):   #REQ. 2
    t1_start = process_time() #tiempo inicial
    year = input('Digita el año YYYY: ')
    month = input('Digita el mes MM: ')
    day = input('Digita el día DD: ')
    date = year.strip() + '-' + month.strip() + '-' + day.strip()
    data = ctrl.accidentesAnteriores(cont, date)
    print(data[0], " accidentes fueron reportados antes de la fecha " +date)
    print("En " ,str(data[1][0]).replace('datetime.date(','').replace(')',''), " fue el día con mayor accidentalidad")
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos ")


def accidentesEnUnRangoDeFecha(cont):   #REQ. 3
    t1_start = process_time() #tiempo inicial
    initialDate = input("Digita la fecha inicial en formato YYYY-MM-DD: ")
    finalDate = input("Digita la fecha final en formato YYYY-MM-DD: ")
    data = ctrl.accidentesEnUnRangoDeFecha(cont,initialDate,finalDate)
    print("La cantidad total de accidentes ocurridos desde " +initialDate+ " hasta " +finalDate+ " fueron" ,data[0], "accidentes" )
    print("La severidad" ,data[1][0], "fue la más común en estos accidentes, con un total de ",data[1][1])
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos ")


def conocerEstado (cont):    #REQ. 4
    t1_start = process_time() #tiempo inicial
    initialDate = input("Digita la fecha inicial en formato YYYY-MM-DD: ")
    finalDate = input("Digita la fecha final en formato YYYY-MM-DD: ")
    data = ctrl.conocerEstado(cont,initialDate,finalDate)
    print("El estado con más accidentes reportados es" ,data[1][0])
    print("La fecha donde hubo más accidentes fue" ,str(data[0][0]).replace('datetime.date(','').replace(')',''), 'con ',data[0][1], 'accidentes')
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos ")

def conocerZonaGeografica (cont):
    t1_start = process_time() #tiempo inicial
    latitud = float(input("Digita la latitud: ").replace('.',''))
    longitud = float(input("Digita la longitud: ").replace('.',''))
    radio = float(input("Digita la distancia del radio en km (recuerde que un grado es 111,12km): "))
    x = ctrl.conocerZonaGeografica(cont,latitud,longitud,radio)
    print("Hay ",x, " accidentes en el radio: ",radio)
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos ")
    #111.12km
def main():
    cont = None
    while True:
        printMenu()
        inputs = int(input('Seleccione una opción para continuar\n-> '))

        if inputs == 1:   #Inicio y carga
            print("\nInicializando.....") 
            # cont es el controlador que se usará de acá en adelante
            cont = controller.init()
            cargarAccidentes(cont)

        elif inputs == 2:   #Req. 1
            print("Buscando accidentes en un rango de fechas\n ")
            if cont == None:
                print('¡KELLY CARGUE EL ARCHIVO PRIMERO!')
            else:
                accidentesPorFecha(cont)
            

        elif inputs == 3:   #Req. 2
            print("Conocer los accidentes anteriores a una fecha\n")
            if cont == None:
                print('¡KELLY CARGUE EL ARCHIVO PRIMERO!')
            else:
                accidentesAnteriores (cont)
                

        elif inputs == 4:   #Req. 3
            print('Conocer los accidentes en un rango de fechas\n ')
            if cont == None:
                print('¡KELLY CARGUE EL ARCHIVO PRIMERO!')
            else:
                accidentesEnUnRangoDeFecha(cont)

        elif inputs == 5:   #Req. 4
            print("Conocer el estado con mas accidentes\n")
            if cont == None:
                print('¡KELLY CARGUE EL ARCHIVO PRIMERO!')
            else:
                conocerEstado(cont)

        elif inputs == 6:   #Req. 5
            print("\nRequerimiento No 5 del reto 3: ")
            if cont == None:
                print('¡KELLY CARGUE EL ARCHIVO PRIMERO!')

        elif inputs == 7:   #Req. 6*
            print("\nRequerimiento No 6 del reto 3: ")
            if cont == None:
                print('¡KELLY CARGUE EL ARCHIVO PRIMERO!')
            else:
                conocerZonaGeografica(cont)

        elif inputs == 8:   #Req. 7*    
            print("\nRequerimiento No 7 del reto 3: ")
            if cont == None:
                print('¡KELLY CARGUE EL ARCHIVO PRIMERO!')

        elif inputs == 0:
            sys.exit(0)

        else:
            print("Opción incorrecta .....")
main()
