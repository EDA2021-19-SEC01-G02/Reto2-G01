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
def newCatalog(hash):
    """ Inicializa el catálogo de videos

    Crea una lista vacia para guardar todos los libros

    Se crean indices (Maps) por los siguientes criterios:
    Categorias
    Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'categories': None}
    catalog['videos'] = lt.newList('SINGLE_LINKED')

    if hash ==1:
        catalog['categories'] = mp.newMap(32,
                                  maptype='CHAINING',
                                  loadfactor=2.0)
    if hash ==2:
        catalog['categories'] = mp.newMap(32,
                                  maptype='PROBING',
                                  loadfactor=0.8) 
    return catalog

# Funciones para agregar informacion al catalogo

def addVideo(catalog, video):
    """
    Esta funcion adiciona un video a la lista de videos,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """
    cat = me.getValue(mp.get(catalog['categories'], video['category_id']))
    
    lt.addLast(catalog['videos'], video)
    lt.addLast(cat['videos'], video)

def addCategory(catalog, id, name):
    """
    Adiciona una categoría junto con su Id a la lista de categorías.
    """
    cat = newCategory(id, name)
    mp.put(catalog['categories'], cat['id'], cat) 

# Funciones para creacion de datos

def newCategory(id, name):
    """
    Esta estructura almacena los tags utilizados para marcar libros.
    """
    category = {'name': None,
     'id': None,
     'videos': None}

    category['name'] = name.lower().strip()
    category['id'] = id
    category['videos'] = lt.newList('ARRAY')

    return category

# Funciones para creacion de datos
def videosSize(catalog):
    """
    Número de videos en el catalogo
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

def compareVideos(video1,video2):
    pass

def compareCategories(cat1,cat2):
    pass
