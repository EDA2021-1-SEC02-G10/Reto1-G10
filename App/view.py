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
import controller
from DISClib.ADT import list as lt
assert cf
import sys
from DISClib.DataStructures import listiterator as it 


default_limit = 1000
sys.setrecursionlimit(default_limit*10)

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar los Top x videos con más views")
    print("3- Consultar el video que más dias ha sido trending en un país")
    print("4- Consultar el video que más dias ha sido trending en una categoria")
    print("5- Consultar los x videos con mas likes en un país específico con un tag específico")
    print("0- Salir")

catalog = None

def initCatalog():
    #inicia el catalogo de videos
    return controller.initCatalog()

def loadData(catalog):
    #carga los videos en la estructura de datos
     controller.loadData(catalog)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        #tipo_lista = int(input("escriba 1 si quiere usar SINGLE_LINKED, de lo contrario escriba 0:"))
        tipo_lista="ARRAY_LIST"
        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog(tipo_lista)
        loadData(catalog)
    elif int(inputs[0]) == 2:
        #F_ordenamiento= int(input("ingrese 1 para selection, 2 para insertion, 3 shell, 4 quick, 5 merge:"))
        #size = int(input("ingrese el size de la lista:"))
        ###size=lt.size(catalog["video"])
        ###F_ordenamiento=5
        ###Tipo_orden = controller.tipo_de_orden(F_ordenamiento, catalog, size)
        #print(Tipo_orden[0])
        numero=int(input("Buscando los top ?:"))
        country=input("Cuál país quiere buscar?:")  
        category=int(input("Cuál categoria quiere buscar?:"))  
        #VideosByViews = VideosByViews(video1,video2)
        rta=controller.llamar_video_mas_views(catalog,numero,country,category)
        ###print(rta)
        iterador= it.newIterator(rta)
        while it.hasNext(iterador):
            element=it.next(iterador)
            print(("Trending date: {}, title: {}, channel title: {}, publish time: {}, views: {}, likes: {}, dislikes: {}").format(element["trending_date"],element['title'],element['channel_title'],element['publish_time'],element['views'],element['likes'],element['dislikes']))
    ###elif int(inputs[0]) == 3:
        ###pais=input("Cúal país quiere buscar?:")
        ###rta=controller.llamar_video_mas_trending(catalog,pais)
    ###elif int(inputs[0]) == 4:
        ###categoria=input("Cúal categoria quiere buscar?:")
    elif int(inputs[0]) == 5:
        pais=input("Cúal país quiere buscar?:")
        tag=input("Cual tag quiere buscar?:")
        rta=controller.video_tag(catalog, pais, tag)
        iterador= it.newIterator(rta)
        while it.hasNext(iterador):
            element=it.nexts(iterador)
            print((" title:{}, channel title:{}, publish_time:{}, views:{}, likes:{}, dislikes:{}, tags:{}").format(element["title"], element["cannel_tittle"], element["publish_time"], element["views"], element["likes"],element["dislikes"],element["tags"]))
    else:
        sys.exit(0)
sys.exit(0)
