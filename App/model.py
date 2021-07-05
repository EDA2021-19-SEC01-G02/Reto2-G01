"""
 * Copyright 2020, Departamento de sistemas y Computación,
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
    """ Inicializa el catálogo de videos

    Crea una lista vacia para guardar todos los libros

    Se crean indices (Maps) por los siguientes criterios:
    Categorias
    Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'categories': None}
    """
    Esta lista contiene todo los libros encontrados
    en los archivos de carga.  Estos libros no estan
    ordenados por ningun criterio.  Son referenciados
    por los indices creados a continuacion.
    """
    catalog['videos'] = lt.newList('SINGLE_LINKED', compareVideos)

    """
    Este indice crea un map cuya llave es el la categoria
    """
    catalog['categories'] = mp.newMap(32,
                                  maptype='CHAINING',
                                  loadfactor=4.0,
                                  comparefunction=compareCategories))
    return catalog

# Funciones para agregar informacion al catalogo
def addBook(catalog, video):
    """
    Esta funcion adiciona un video a la lista de videos,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Adicionalmente se guarda en el indice de autores, una referencia
    al libro.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    lt.addLast(catalog['videos'], video)
    mp.put(catalog['categories'], book['category_id'], video)

# Funciones para creacion de datos
def videosSize(catalog):
    """
    Número de videos en el catago
    """
    return lt.size(catalog['videos'])


def categoriesSize(catalog):
    """
    Numero de categorias en el catalogo
    """
    return mp.size(catalog['categories'])
    
# Funciones de consulta
def getLikedVideos(catalog, category_name,country, numerovideos):
    id = -1000
    sublista = None

    for i in range(1, lt.size(catalog['categories'])+1):
        categoria = lt.getElement(catalog['categories'], i)
        if categoria['name'].lower() == category_name.lower():
            id = categoria['category_id']

    if id != -1000:   
        lista_inicial = catalog['videos']
        lista_sortear= lt.newList('ARRAY_LIST')

        for j in range(1,lt.size(lista_inicial)+1):
            video = lt.getElement(lista_inicial, j)
            if video["category_id"] == id and video["country"].lower().strip() == country.lower():   
                lt.addLast(lista_sortear, video)

        lista_sortear = sortVideosLikes(lista_sortear)
        lista_sortear = getUnicos(lista_sortear)
        if numerovideos <= lt.size(lista_sortear):
            sublista = lt.subList(lista_sortear, 1, numerovideos)
    return sublista

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

# ==============================
# Funciones de Comparacion
# ==============================

