﻿"""
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
 """

import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog

# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadVideos(catalog)
    loadCategories(catalog)

def loadVideos(catalog):
    """
    Carga los videos del archivo. 
    """
    videosfile = cf.data_dir + 'videos-large.csv'
    input_file = csv.DictReader(open(videosfile, encoding='utf-8'))
    for video in input_file:
        model.addVideo(catalog, video)

def loadCategories(catalog):
    """
    Carga todas las categorías del archivo y los agrega a la lista de categorías
    """
    categoryfile = cf.data_dir + 'category-id.csv'
    input_file = csv.DictReader(open(categoryfile, encoding='utf-8'))
    for cat in input_file:
        cat['id\tname'] = cat['id\tname'].split("\t")
        model.addCategory(catalog, cat['id\tname'][0], cat['id\tname'][1])

# Funciones de ordenamiento


# Funciones de consulta sobre el catálogo
def videosSize(catalog):
    """
    Numero de videos cargados al catalogo
    """
    return model.videosSize(catalog)


def categoriesSize(catalog)::
    """
    Numero de categorias cargados al catalogo
    """
    return model.categoriesSize(catalog)

def getLikedVideos(catalog, category_name,country, numerovideos):
    return model.getLikedVideos(catalog, category_name,country, numerovideos)