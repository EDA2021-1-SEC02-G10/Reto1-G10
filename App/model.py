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
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as isort
from DISClib.Algorithms.Sorting import selectionsort as ssort
from DISClib.Algorithms.Sorting import quicksort as quick
from DISClib.Algorithms.Sorting import mergesort as merge
assert cf
from DISClib.DataStructures import listiterator as it 

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog(tipolista):
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y videos. Retorna el catalogo inicializado.
    """
    catalog = {'trending_date': None,
               "video":None,
               "category":None,
               'title': None,
               'cannel_tittle': None,
               'publish_time': None,
               'views': None,
               'likes': None,
               'dislikes': None,
               'country': None,
               'tags': None,
               'número_días': None,}

    catalog['trending_date'] = lt.newList()
    catalog['video'] = lt.newList(tipolista,
                                  cmpfunction=comparetittle)
    catalog['category'] = lt.newList(tipolista,
                                  cmpfunction=comparetittle)
    catalog['title'] = lt.newList(tipolista,
                                  cmpfunction=comparetittle)
    catalog['cannel_tittle'] = lt.newList(tipolista,
                                 cmpfunction=comparecannel_tittle)
    catalog['publish_time'] = lt.newList(tipolista,
                                 cmpfunction=comparepublish_time)
    catalog['views'] = lt.newList(tipolista,
                                 cmpfunction=compareviews)
    catalog['likes'] = lt.newList(tipolista,
                                 cmpfunction=comparelikes)
    catalog['dislikes'] = lt.newList(tipolista,
                                 cmpfunction=comparedislikes)
    catalog['country'] = lt.newList(tipolista,
                                 cmpfunction=comparecountry)
    catalog['tags'] = lt.newList(tipolista,
                                 cmpfunction=comparecountry)
    catalog['número_días'] = lt.newList(tipolista, 
                                cmpfunction=comparecountry)

    return catalog

# Funciones para agregar informacion al catalogo
def addvideo (catalogo, video1):
    lt.addLast(catalogo["video"],video1)
#def adddata (catalogo,vategory):
    #lt.addlast(catalogo[])

# Funciones para creacion de datos
def newtitle (title):
    title = {'title': "", "books": None,  "average_rating": 0}
    title['title'] = title
    title['books'] = lt.newList('ARRAY_LIST')
    return title


# Funciones de consulta
def cmpVideosByViews(video1, video2):

    rta = True
    if int(video1["views"]) > int(video1["views"]):
        rta = False
    return rta



#Devuelve verdadero (True) si los 'views' de video1 son menores que los del video2
#Args:
#video1: informacion del primer video que incluye su valor 'views'
#video2: informacion del segundo video que incluye su valor 'views'

# Funciones utilizadas para comparar elementos dentro de una lista

def comparetittle (titulo1, titulo2):
    if (titulo1['title'] == titulo2['title']):
        return 0
    return -1

def comparecannel_tittle (cannel, cannel2):
    if (cannel['channel']== cannel2['channel']):
        return 0
    return -1

def comparepublish_time (time1, time2):
    if (time1['publish_time'] > time2['publish_time']):
        return 1
    elif (time1['publish_time'] < time2['publish_time']):
        return -1
    return 0

def compareviews (vistas1, vistas2):
    if (vistas1['views'] > vistas2['views']):
        return 1
    elif (vistas1['views'] < vistas2['views']):
        return -1
    return 0
def comparelikes(like1, like2):
    if (like1['likes'] > like2['likes']):
        return 1
    elif (like1['likes'] < like2['likes']):
        return -1
    return 0
def comparedislikes( dislikes1, dislikes2):
    if (dislikes1['dislikes'] > dislikes2['dislikes']):
        return 1
    elif (dislikes1['dislikes'] < dislikes1['dislikes']):
        return -1
    return 0
def comparecountry(country1,country2):
    if (country1['country']== country2['country']):
        return 0
    return -14

def comparethings(video1, video2):
    return(float(video1["views"])>float(video2["views"]))

def comparelikes(video1, video2):
    return(int(video1["likes"]>int(video2["likes"])))

# Funciones de ordenamiento
def tipo_de_orden_model(numero, catalog, size):
    sub_list = lt.subList(catalog['video'], 0, size)
    sub_list = sub_list.copy()
    start_time = time.process_time()
    if numero == 2:
        sorted_list = sa.sort(sub_list, compareviews)
    elif numero == 1:
        sorted_list = isort.sort(sub_list, compareviews)
    elif numero == 3:
        sorted_list = ssort.sort(sub_list, compareviews)
    elif numero == 4:
        sorted_list = quick.sort(sub_list, compareviews)
    else:
        sorted_list = merge.sort(sub_list, compareviews)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return elapsed_time_mseg, sorted_list

#requerimiento 1
def llamar_views(catalog,numero,country,category):
    size=lt.size(catalog["video"])
    sub_list = lt.subList(catalog['video'], 0, size)
    sub_list = sub_list.copy()
    rta= sa.sort(sub_list,comparethings)
    best_video = lt.newList() 
    iterador = it.newIterator(rta)
    i=1
    while it.hasNext(iterador) and i <= numero:
        element=it.next(iterador)
        if country == element['country'] and category == int(element['category_id']):
            lt.addLast(best_video, element)
            i+=1
    return best_video
#requerimiento 2
###def llamar_video_mas_trending(catalog,pais):

#Requerimiento 4
def video_tag(catalog,pais,tag):
     size=lt.size(catalog["video"])
     sub_list = lt.subList(catalog['video'], 0, size)
     sub_list = sub_list.copy()
     rta= sa.sort(sub_list,comparelikes)
     tag_video = lt.newList()
     iterador = it.newIterator(rta)
     while it.hasNext(iterador):
         element=it.next(iterador)
         if pais == element["country"] and tag in element["tags"]:
             lt.addlast(tag_video,element)
     return tag_video 