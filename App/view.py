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

crimefile = 'crime-utf8.csv'

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("-"*75)
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de accidentes")
    print("3- Conocer los accidentes en una fecha")
    print("4- Conocer los accidentes anteriores a una fecha")
    print("5- Conocer los accidentes en un rango de fechas")
    print("6- Conocer el estado con mas accidentes")
    print("7- Conocer los accidentes por rango de horas")
    print("8- Conocer la zona geográfica mas accidentada")
    print("9- Usar el conjunto completo de datos")
    print("0- Salir")
    print("-"*75)

# Menu principal

def cargarAccidentes(cont):
    t1_start = process_time() #tiempo inicial
    print("\nCargando información de crimenes .....")
    controller.loadData(cont, crimefile)
    print('Crimenes cargados: ' + str(controller.crimesSize(cont)))
    print('Altura del arbol: ' + str(controller.indexHeight(cont)))
    print('Elementos en el arbol: ' + str(controller.indexSize(cont)))
    print('Menor Llave: ' + str(controller.minKey(cont)))
    print('Mayor Llave: ' + str(controller.maxKey(cont)))
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos ")

def accidentesPorFecha(cont):
    t1_start = process_time() #tiempo inicial
    year = input('Digite el año YYYY: ')
    month = input('Digite el mes MM: ')
    day = input('Digite el día DD: ')
    date = year.strip() + '-' + month.strip() + '-' + day.strip()
    lst = ctrl.accidentesPorFecha(cont, date)
    print('Los tipos de crimenes cometidos en la fecha', date, 'fueron: ')
    iterator = it.newIterator(lst[1])
    i = 1
    while it.hasNext(iterator):
        print(i,'- ',it.next(iterator))
        i += 1
    print('Para un total de ',lst[0],' crimenes')
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos ")


while True:
    printMenu()
    inputs = int(input('Seleccione una opción para continuar\n-> '))

    if inputs == 1:
        print("\nInicializando.....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.init()

    elif inputs == 2:
        cargarAccidentes(cont)

    elif inputs == 3:   #Req. 1
        print("\nBuscando crimenes en un rango de fechas: ")
        accidentesPorFecha(cont)

    elif inputs == 4:   #Req. 2
        print("\nRequerimiento No 1 del reto 3: ")

    elif inputs == 5:   #Req. 3
        print("\nRequerimiento No 1 del reto 3: ")

    elif inputs == 6:   #Req. 4
        print("\nRequerimiento No 1 del reto 3: ")

    elif inputs == 7:   #Req. 5
        print("\nRequerimiento No 1 del reto 3: ")

    elif inputs == 8:   #Req. 6*
        print("\nRequerimiento No 1 del reto 3: ")

    elif inputs == 9:   #Req. 7*    
        print("\nRequerimiento No 1 del reto 3: ")

    elif inputs == 0:
        sys.exit(0)

    else:
        print("Opcion incorrecta .....")
main()
