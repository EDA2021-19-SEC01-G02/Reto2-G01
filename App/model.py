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

# ==============================
# Construccion de modelos
# ==============================

def newCatalog():
    """ Inicializa el catálogo de videos

    Crea una lista vacia para guardar todos los libros

    Se crean indices (Maps) por los siguientes criterios:
    Categorias
    Retorna el catalogo inicializado.
    """
    catalog = {'videos': None,
               'categories': None,
               'countries': None,
               'categories_name': None}

    catalog['videos'] = lt.newList('ARRAY_LIST')
    catalog['categories'] = mp.newMap(32, maptype='PROBING', loadfactor=0.5)
    catalog['countries'] = mp.newMap(10, maptype='PROBING', loadfactor=0.5)
    catalog['categories_name'] = mp.newMap(32, maptype='PROBING', loadfactor=0.5) 

    return catalog


# ==============================
# Funciones para agregar informacion al catalogo
# ==============================

def addVideo(catalog, video):
    """
    Esta funcion adiciona un video a la lista de videos,
    adicionalmente lo guarda en un Map usando como llave su Id.
    Finalmente crea una entrada en el Map de años, para indicar que este
    libro fue publicaco en ese año.
    """

    if mp.contains(catalog['countries'], video['country'].lower().strip()):
        country = me.getValue(mp.get(catalog['countries'], video['country'].lower().strip()))
        #mp.get me da la pareja lalve valor pero como solo necesito el valor por eso hago el .getValue
        lt.addLast(country['videos'], video)
    else:
        addCountry(catalog, video['country'].lower().strip())
        country = me.getValue(mp.get(catalog['countries'], video['country'].lower().strip()))
        lt.addLast(country['videos'], video)
        #si no esta el pais entonces, se crea el nuevo pais con el nombre y la lista de videos y des pues se adiciona 
    cat = me.getValue(mp.get(catalog['categories'], video['category_id']))
    lt.addLast(catalog['videos'], video)
    lt.addLast(cat['videos'], video)


def addCategory(catalog, id, name):
    """
    Adiciona una categoría junto con su Id a la lista de categorías.
    """
    cat = newCategory(id, name)
    mp.put(catalog['categories'], cat['id'], cat)
    mp.put(catalog['categories_name'], cat['name'], cat['id'])


def addCountry(catalog, name):
    """
    Adiciona una categoría junto con su Id a la lista de categorías.
    """
    country = newCountry(name)
    mp.put(catalog['countries'], name, country)


# ==============================
# Funciones para creacion de datos
# ==============================

def newCategory(id, name):
    """
    Esta estructura almacena los tags utilizados para marcar libros.
    """
    category = {'name': None,
     'id': None,
     'videos': None}

    category['name'] = name.lower().strip()
    category['id'] = id
    category['videos'] = lt.newList('ARRAY_LIST')

    return category


def newCountry(name):
    """
    Esta estructura almacena los tags utilizados para marcar libros.
    """
    country = {'name': None,
     'videos': None}

    country['name'] = name.lower()
    country['videos'] = lt.newList('ARRAY_LIST')

    return country


# ==============================
# Funciones para creacion de datos
# ==============================

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


def countriesSize(catalog):
    """
    Numero de paises en el catalogo
    """
    return mp.size(catalog['countries'])


# ==============================
# Funciones de consulta
# ==============================

def getLikedVideos(catalog, category_name, country, numerovideos):
    id = -1000
    sublista = None

    try:
        id = mp.get(catalog["categories_name"], category_name.lower())
        id = me.getValue(id)
    except:
        print("La categoria no existe")

    if id != -1000:   
        lista_inicial = me.getValue(mp.get(catalog['countries'], country.lower()))["videos"]
        lista_sortear= lt.newList('ARRAY_LIST')

        for j in range(1,lt.size(lista_inicial)+1):
            video = lt.getElement(lista_inicial, j)
            if video["category_id"] == id:   
                lt.addLast(lista_sortear, video)

        lista_sortear = sortVideosLikes(lista_sortear)
        lista_sortear = getUnicos(lista_sortear)
        if numerovideos <= lt.size(lista_sortear):
            sublista = lt.subList(lista_sortear, 1, numerovideos)
    return sublista


def getAltamentePositiva(catalog, country):
    lista_sortear= lt.newList('ARRAY_LIST')
    lista_inicial = None

    try:
        lista_inicial = mp.get(catalog["countries"], country.lower())
        lista_inicial = me.getValue(lista_inicial)['videos']
    except:
        print("El pais no esta en la base de datos")
    
    if lista_inicial != None:
        for i in range(1,lt.size(lista_inicial)+1):
            video = lt.getElement(lista_inicial, i)
            if int(video["dislikes"])>0:
                ratio = int(video["likes"])/int(video["dislikes"])
                if  ratio > 10:
                    video['ratio'] = ratio  
                    lt.addLast(lista_sortear, video)

    if lt.size(lista_sortear) != 0:
        return lt.getElement(conteo_trending(lista_sortear),1)
    else:
        return None


def getSumamentePositiva(catalog, category_name):
    id = -1000
    lista_sortear= lt.newList('ARRAY_LIST')

    try:
        id = mp.get(catalog["categories_name"], category_name.lower())
        id = me.getValue(id)
    except:
        print("La categoria no existe")

    if id != -1000:
        lista_inicial = me.getValue(mp.get(catalog["categories"], id))['videos']
        for j in range(1,lt.size(lista_inicial)+1):
            video = lt.getElement(lista_inicial,j)
            if int(video["dislikes"])>0:
                ratio = int(video["likes"])/int(video["dislikes"])
                if video["category_id"] == id and ratio > 20:
                    video['ratio'] = ratio
                    lt.addLast(lista_sortear, video)

    if lt.size(lista_sortear) != 0:
        return lt.getElement(conteo_trending(lista_sortear),1)
    else:
        return None
    

def getComentariosVideos(catalog, country, numerovideos, tag):
    sublista = None
    lista_inicial = None

    try:
        lista_inicial = mp.get(catalog["countries"], country.lower())
        lista_inicial = me.getValue(lista_inicial)['videos']
    except:
        print("El pais no esta en la base de datos")
    
    if lista_inicial != None:
        lista_comentarios = lt.newList('ARRAY_LIST')
        for j in range(1, lt.size(lista_inicial)+1):
            video_comentarios = lt.getElement(lista_inicial, j)
            tags = str(video_comentarios["tags"])

            if tag.lower() in tags.lower():
                lt.addLast(lista_comentarios, video_comentarios)

        lista_comentarios = sortVideosComents(lista_comentarios)
        lista_sortear = getUnicos(lista_comentarios)
        if numerovideos <= lt.size(lista_sortear):
            sublista = lt.subList(lista_sortear, 1, numerovideos)
            
    return sublista


# ==============================
# Funciones utilizadas para comparar elementos dentro de una lista
# ==============================

def cmpVideosByLikes(video1, video2):
    """ Devuelve verdadero (True) si los likes de video1 
    son menores que los del video2 Args: video1: informacion del 
    primer video que incluye su valor 'likes'"""
    return (int(video1['likes'])) > int((video2['likes']))


def cmpVideosByDays(video1, video2):
    """ Devuelve verdadero (True) si los likes de video1 
    son menores que los del video2 Args: video1: informacion del 
    primer video que incluye su valor 'likes'"""
    return (int(video1['days'])) > int((video2['days']))


def cmpVideosByComments(video1, video2):
    """ Devuelve verdadero (True) si los likes de video1 
    son menores que los del video2 Args: video1: informacion del 
    primer video que incluye su valor 'likes'"""
    return (int(video1['comment_count'])) > int((video2['comment_count']))


# ==============================
# Funciones de ordenamiento
# ==============================

def sortVideosLikes(lista):
    return sa.sort(lista,cmpVideosByLikes) 


def sortVideosDays(lista):
    return sa.sort(lista,cmpVideosByDays)
    

def sortVideosComents(lista):
    return sa.sort(lista,cmpVideosByComments)  


# ==============================
# Funciones auxiliares
# ==============================

def conteo_trending(lista_videos):
    lista_u = sortVideosDays(getUnicos(lista_videos))
    return lista_u


def getUnicos(lista_videos):
    lista_u = lt.newList('ARRAY_LIST')
    conteo = {}

    for i in range (1,lt.size(lista_videos)+1):
        video = lt.getElement(lista_videos,i)
        id = video['video_id']
        if id in conteo:
            conteo[id] += 1
        else:
            conteo[id] = 1
            lt.addLast(lista_u, video)

    for j in range(1, lt.size(lista_u)+1):
        video_u = lt.getElement(lista_u,j)
        id_u = video_u['video_id']
        video_u['days'] = conteo[id_u]
    
    return lista_u



