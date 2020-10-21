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
import config
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as m
import datetime
assert config
from DISClib.DataStructures import listiterator as it

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria


"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------


def newAnalyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    analyzer = {'accidents': None,
                'dateIndex': None
                }

    analyzer['accidents'] = lt.newList('SINGLE_LINKED', compareIds)
    analyzer['dateIndex'] = om.newMap(omaptype='RBT',
                                      comparefunction=compareDates)
    return analyzer


# Funciones para agregar informacion al catalogo


def addAccident(analyzer, accident):
    """
    """
    lt.addLast(analyzer['accidents'], accident)
    updateDateIndex(analyzer['dateIndex'], accident)
    return analyzer


def updateDateIndex(map, accident):
    """
    Se toma la fecha del crimen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    occurreddate = accident['Start_Time']
    accidentdate = datetime.datetime.strptime(occurreddate, '%Y-%m-%d %H:%M:%S')
    entry = om.get(map, accidentdate.date())
    if entry is None:
        datentry = newDataEntry(accident)
        om.put(map, accidentdate.date(), datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, accident)
    return map


def addDateIndex(datentry, accident):
    """
    Actualiza un indice de tipo de crimenes.  Este indice tiene una lista
    de crimenes y una tabla de hash cuya llave es el tipo de crimen y
    el valor es una lista con los crimenes de dicho tipo en la fecha que
    se está consultando (dada por el nodo del arbol)
    """
    lst = datentry['lstaccident']
    lt.addLast(lst, accident)
    offenseIndex = datentry['offenseIndex']
    offentry = m.get(offenseIndex, accident['Description'])
    if (offentry is None):
        entry = newOffenseEntry(accident['Description'], accident)
        lt.addLast(entry['lstoffenses'], accident)
        m.put(offenseIndex, accident['Description'], entry)
    else:
        entry = me.getValue(offentry)
        lt.addLast(entry['lstoffenses'], accident)
    return datentry


def newDataEntry(accident):
    """
    Crea una entrada en el indice por fechas, es decir en el arbol
    binario.
    """
    entry = {'offenseIndex': None, 'lstaccident': None}
    entry['offenseIndex'] = m.newMap(loadfactor = 3,
                                     numelements = 30,
                                     maptype = 'CHAINING',
                                     comparefunction = compareOffenses)
    entry['lstaccident'] = lt.newList('SINGLE_LINKED', compareDates)
    return entry


def newOffenseEntry(offensegrp, accident):
    """
    Crea una entrada en el indice por tipo de crimen, es decir en
    la tabla de hash, que se encuentra en cada nodo del arbol.
    """
    ofentry = {'offense': None, 'lstoffenses': None}
    ofentry['offense'] = offensegrp
    ofentry['lstoffenses'] = lt.newList('SINGLELINKED', compareOffenses)
    return ofentry


# ==============================
# Funciones de consulta
# ==============================


def accidentsSize(analyzer):
    """
    Número de libros en el catago
    """
    return lt.size(analyzer['accidents'])


def indexHeight(analyzer):
    """Numero de autores leido
    """
    return om.height(analyzer['dateIndex'])


def indexSize(analyzer):
    """Numero de autores leido
    """
    return om.size(analyzer['dateIndex'])


def minKey(analyzer):
    """Numero de autores leido
    """
    return om.minKey(analyzer['dateIndex'])


def maxKey(analyzer):
    """Numero de autores leido
    """
    return om.maxKey(analyzer['dateIndex'])


def getAccidentsByRange(analyzer, initialDate, finalDate):
    """
    Retorna el numero de crimenes en un rago de fechas.
    """
    lst = om.values(analyzer['dateIndex'], initialDate, finalDate)
    return lst


def getAccidentsByRangeCode(analyzer, initialDate, offensecode):
    """
    Para una fecha determinada, retorna el numero de crimenes
    de un tipo especifico.
    """
    accidentdate = om.get(analyzer['dateIndex'], initialDate)
    if accidentdate['key'] is not None:
        offensemap = me.getValue(accidentdate)['offenseIndex']
        numoffenses = m.get(offensemap, offensecode)
        if numoffenses is not None:
            return m.size(me.getValue(numoffenses)['lstoffenses'])
        return 0

def accidentesPorFecha(cont, date):   #REQ. 1
    data = om.get(cont['dateIndex'],date)
    values = me.getValue(data)['offenseIndex']
    accidents = m.keySet(values)
    cantidad = {'total': 0,'1':0,'2':0,'3':0,'4':0}
    iterator = it.newIterator(accidents)
    while it.hasNext(iterator):
        actual = m.get(values,it.next(iterator))
        data = me.getValue(actual)['lstoffenses']
        cantidad['total'] += lt.size(data)
        siguiente = it.newIterator(data)
        while it.hasNext(siguiente):
            current = it.next(siguiente)
            severidad = current['Severity']
            cantidad[severidad] += 1
    return cantidad

def accidentesAnteriores (cont, date):   # REQ. 1
    initialDate = om.minKey(cont['dateIndex'])
    finalDate = om.floor(cont['dateIndex'],date)
    shaves = om.keys(cont['dateIndex'],initialDate,finalDate)
    cantidad = {'total': 0, 'fecha': {} }
    iterator = it.newIterator(shaves)
    while it.hasNext(iterator):
        date = it.next(iterator)
        data = om.get(cont['dateIndex'],date)
        values = me.getValue(data)['offenseIndex']
        accidents = m.keySet(values)
        numero = 0
        iterator2 = it.newIterator(accidents)
        while it.hasNext(iterator2):
            actual = m.get(values,it.next(iterator2))
            data = me.getValue(actual)['lstoffenses']
            cantidad['total'] += lt.size(data)
            numero += lt.size(data)
        cantidad['fecha'][date] = numero
    mayor = ['',0]
    for i in cantidad['fecha']:
        if cantidad['fecha'][i] >= mayor[1]:
            mayor[0] = i
            mayor[1] = cantidad['fecha'][i]
    return (cantidad['total'],mayor)

def accidentesEnUnRangoDeFecha(cont,initialDate,finalDate): #O(N)   REQ. 3
    shaves = om.keys(cont['dateIndex'],initialDate,finalDate)
    cantidad = {'total': 0,'1':0,'2':0,'3':0,'4':0}
    iterator = it.newIterator(shaves)
    while it.hasNext(iterator):
        date = it.next(iterator)
        cantidades = accidentesPorFecha(cont,date)
        cantidad['total'] += cantidades['total']
        cantidad['1'] += cantidades['1']
        cantidad['2'] += cantidades['2']
        cantidad['3'] += cantidades['3']
        cantidad['4'] += cantidades['4']
    mayor = ['',0]
    total = cantidad['total']
    del cantidad['total']
    for i in cantidad:
        if cantidad[i] >= mayor[1]:
            mayor[0] = i
            mayor[1] = cantidad[i]
    return (total,mayor)

def conocerEstado (cont,initialDate,finalDate):   #REQ. 4
    shaves = om.keys(cont['dateIndex'],initialDate,finalDate)
    cantidad = {'fecha': {}, 'state': {} }
    iterator = it.newIterator(shaves)
    while it.hasNext(iterator):
        date = it.next(iterator)
        data = om.get(cont['dateIndex'],date)
        values = me.getValue(data)['offenseIndex']
        accidents = m.keySet(values)
        numero = 0
        iterator2 = it.newIterator(accidents)
        while it.hasNext(iterator2):
            actual = m.get(values,it.next(iterator2))
            data = me.getValue(actual)['lstoffenses']
            numero += lt.size(data)
            siguiente = it.newIterator(data)
            while it.hasNext(siguiente):
                current = it.next(siguiente)
                state = current['State']
                if state not in cantidad['state']:
                    cantidad['state'][state] = 1
                else: 
                    cantidad['state'][state] += 1
        cantidad['fecha'][date] = numero
    mayorFecha = ['',0]
    for i in cantidad['fecha']:
        if cantidad['fecha'][i] >= mayorFecha[1]:
            mayorFecha[0] = i
            mayorFecha[1] = cantidad['fecha'][i]
    mayorState = ['',0]
    for i in cantidad['state']:
        if cantidad['state'][i] >= mayorState[1]:
            mayorState[0] = i
            mayorState[1] = cantidad['state'][i]
    return (mayorFecha, mayorState)

def dentroDelRadio(cont, radio, longitud, latitud, current):
    loc_lng = float(current['Start_Lng'].replace('.',''))
    loc_lat = float(current['Start_Lat'].replace('.',''))
    extremo_y  = latitud+radio
    extremo_x    = longitud+radio
    if extremo_y >= loc_lat and extremo_x >= loc_lng:
        return True

def conocerZonaGeografica(cont, radio, longitud, latitud):
    """
    cont: analyzer
    Radio: En que se encuentran los accidentes
    longitud: coordenada
    latitud: coordenada
    centro=(latitud,longitud)

    """
    initialDate = om.minKey(cont['dateIndex'])
    finalDate = om.floor(cont['dateIndex'],om.maxKey(cont['dateIndex'])) 
    shaves = om.keys(cont['dateIndex'],initialDate,finalDate)
    cantidad = 0
    iterator = it.newIterator(shaves)
    while it.hasNext(iterator):
        date = it.next(iterator)
        data = om.get(cont['dateIndex'],date)
        values = me.getValue(data)['offenseIndex']
        accidents = m.keySet(values)
        iterator2 = it.newIterator(accidents)
        while it.hasNext(iterator2):
            actual = m.get(values,it.next(iterator2))
            data = me.getValue(actual)['lstoffenses']
            siguiente = it.newIterator(data)
            while it.hasNext(siguiente):
                current = it.next(siguiente)
                if dentroDelRadio(cont, radio, longitud, latitud, current) == True:
                    cantidad += 1
                
    return cantidad


# ==============================
# Funciones de Comparacion
# ==============================


def compareIds(id1, id2):
    """
    Compara dos crimenes
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareDates(date1, date2):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1


def compareOffenses(offense1, offense2):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    offense = me.getKey(offense2)
    if (offense1 == offense):
        return 0
    elif (offense1 > offense):
        return 1
    else:
        return -1
