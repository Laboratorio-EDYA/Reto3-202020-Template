"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
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

import config as cf
from App import model
import datetime
import csv

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________

def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(analyzer, accidentsfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    accidentsfile = cf.data_dir + accidentsfile
    input_file = csv.DictReader(open(accidentsfile, encoding="utf-8"),
                                delimiter=",")
    for accident in input_file:
        model.addAccident(analyzer, accident)
    return analyzer

# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________

def accidentsSize(analyzer):
    """
    Numero de crimenes leidos
    """
    return model.accidentsSize(analyzer)

def indexHeight(analyzer):
    """
    Altura del indice (arbol)
    """
    return model.indexHeight(analyzer)

def indexSize(analyzer):
    """
    Numero de nodos en el arbol
    """
    return model.indexSize(analyzer)

def minKey(analyzer):
    """
    La menor llave del arbol
    """
    return model.minKey(analyzer)

def maxKey(analyzer):
    """
    La mayor llave del arbol
    """
    return model.maxKey(analyzer)

def getAccidentsByRange(analyzer, initialDate, finalDate):
    """
    Retorna el total de crimenes en un rango de fechas
    """
    initialDate = datetime.datetime.strptime(initialDate, '%Y-%m-%d')
    finalDate = datetime.datetime.strptime(finalDate, '%Y-%m-%d')
    return model.getAccidentsByRange(analyzer, initialDate.date(),
                                  finalDate.date())

def getAccidentsByRangeCode(analyzer, initialDate, offensecode):
    """
    Retorna el total de crimenes de un tipo especifico en una
    fecha determinada
    """
    initialDate = datetime.datetime.strptime(initialDate, '%Y-%m-%d')
    return model.getAccidentsByRangeCode(analyzer, initialDate.date(),
                                      offensecode)

def accidentesPorFecha(cont, date, anio):
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    return model.accidentesPorFecha(cont, date.date(), anio)

def accidentesEnUnRangoDeFecha(cont, initialDate, finalDate, anio):
    initialDate = datetime.datetime.strptime(initialDate, '%Y-%m-%d')
    finalDate = datetime.datetime.strptime(finalDate, '%Y-%m-%d')
    return model.accidentesEnUnRangoDeFecha(cont,initialDate.date(),finalDate.date(), anio)

def conocerEstado (cont, initialDate, finalDate, anio):
    initialDate = datetime.datetime.strptime(initialDate, '%Y-%m-%d')
    finalDate = datetime.datetime.strptime(finalDate, '%Y-%m-%d')
    return model.conocerEstado(cont,initialDate.date(),finalDate.date(), anio)

def accidentesAnteriores (cont, date, anio):
    date = datetime.datetime.strptime(date, '%Y-%m-%d')
    return model.accidentesAnteriores(cont, date.date(), anio)

def conocerHoras(cont, initialHour, finalHour, anio):
    initialHour1 = datetime.datetime.strptime(initialHour, '%H:%M')
    finalHour1 = datetime.datetime.strptime(finalHour, '%H:%M')
    initialHour = (initialHour1.hour,initialHour1.minute)
    finalHour = (finalHour1.hour,finalHour1.minute)
    return model.conocerHoras(cont,initialHour,finalHour,anio)

def conocerZonaGeografica(cont,latitud,longitud,radio,anio):
    return model.conocerZonaGeografica(cont,latitud,longitud,radio,anio)

def gradosAkilometros2(x):
    a=x.split('.')
    try:
        return str(a[0])+'.'+str(a[1])+str(a[2])
    except:
        return str(a[0])+'.'+str(a[1])    
    
