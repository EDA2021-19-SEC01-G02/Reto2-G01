"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
assert cf

from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar los videos con mas likes")
    print("3- Consultar el video trending el mayor numero de dias")
    print("4- Consultar video trending con percepcion sumamente positiva")
    print("5- Consultar videos con mas comentarios por tag")
    print("0- Salir")

catalog = None

def initCatalog():
    return controller.initCatalog()


def loadData(catalog):
    """
    Carga los libros en el catalogo
    """
    controller.loadData(catalog)


def printLikedVideos(lista):
    if lista != None:
        for i in range(1,lt.size(lista)+1):
            video = lt.getElement(lista,i)
            print('trending_date : {} \t title: {} \t channel_title : {} \t publish_time : {} \t views: {} \t likes: {} \t dislikes: {}'
            .format(video['trending_date'],video['title'],video['channel_title'],video['publish_time'],video['views'],video['likes'],video['dislikes']))
    else:
        print('Verifique los datos ingresados.')


def printAltamentePositiva(video):
    if video != None:
        print('title: {} \t channel_title : {} \t country : {} \t ratio_likes_dislikes: {:.2f} \t days: {}'
            .format(video['title'],video['channel_title'],video['country'],video['ratio'],video['days'])) 
    else:
        print('Verifique los datos ingresados.')  


def printSumamentePositiva(video):
    if video != None:
        print('title: {} \t channel_title : {} \t category_id : {} \t ratio: {:.2f} \t days: {}'
            .format(video['title'],video['channel_title'],video['category_id'],video['ratio'],video['days']))
    else:
        print('Verifique los datos ingresados.')   


def printComentariosVideos(lista):
    if lista != None:
        for i in range(1,lt.size(lista)+1):
            video = lt.getElement(lista,i)
            print('title: {} \t channel_title : {} \t publish_time : {} \t views: {} \t likes: {} \t dislikes: {} \t comment_count: {} \t tags: {}'
            .format(video['title'],video['channel_title'],video['publish_time'],video['views'],video['likes'],video['dislikes'],video['comment_count'],video['tags']))
    else:
        print('Verifique los datos ingresados.')


"""
Menu principal
"""

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")

        catalog = controller.initCatalog()
        answer= controller.loadData(catalog)

        print('Videos cargados: ' + str(controller.videosSize(catalog)))
        print('Categorias cargadas: ' + str(controller.categoriesSize(catalog)))
        print('Paises cargados: ' + str(controller.countriesSize(catalog)))

        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")

    elif int(inputs[0]) == 2:
        
        category_name = input("Ingrese la categoria a buscar: ")
        country = input("Ingrese el pais a buscar: ")
        numerovideos = int(input("Ingrese el numero de videos que quiere listar: "))
        answer= controller.timeLikes(catalog, category_name, country, numerovideos)
        mas_likes = controller.getLikedVideos(catalog, category_name, country, numerovideos)
        printLikedVideos(mas_likes)

        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")

    elif int(inputs[0]) == 3:
        country = input("Ingrese el pais a buscar: ")
        answer= controller.timeAltamente(catalog, country)
        trending_positiva = controller.getAltamentePositiva(catalog, country)
        printAltamentePositiva(trending_positiva)

        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")

    elif int(inputs[0]) == 4:
        category_name = input("Ingrese la categoria a buscar: ")
        answer= controller.timeSumamente(catalog, category_name)
        trending_positiva = controller.getSumamentePositiva(catalog, category_name)
        printSumamentePositiva(trending_positiva)

        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")

    elif int(inputs[0]) == 5:
        country = input("Ingrese el pais a buscar: ")
        numero_videos = int(input("Ingrese el numero de videos que quiere listar: "))
        tag = input("Ingrese la etiqueta del video: ")
        answer= controller.timeComentarios(catalog, country, numero_videos, tag)
        mas_comentarios = controller.getComentariosVideos(catalog, country, numero_videos, tag)
        printComentariosVideos(mas_comentarios)

        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",
              "Memoria [kB]: ", f"{answer[1]:.3f}")

    else:
        sys.exit(0)
sys.exit(0)
