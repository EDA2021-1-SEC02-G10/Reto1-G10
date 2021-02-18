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
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """
    Inicializa el catálogo de videos. Crea una lista vacia para guardar
    todos los videos, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y videos. Retorna el catalogo inicializado.
    """
    catalog = {'trending_date': None,
               'title': None,
               'cannel_tittle': None,
               'publish_time': None,
               'views': None,
               'likes': None,
               'dislikes': None,
               'country': None,
               'número_días': None,}

    catalog['trending_date'] = lt.newList()
    catalog['title'] = lt.newList('SINGLE_LINKED',
                                  cmpfunction=comparetitle)
    catalog['cannel_tittle'] = lt.newList('SINGLE_LINKED',
                                 cmpfunction=comparecannel_tittle)
    catalog['publish_time'] = lt.newList('SINGLE_LINKED',
                                 cmpfunction=comparepublish_time)
    catalog['views'] = lt.newList('SINGLE_LINKED',
                                 cmpfunction=compareviews)
    catalog['likes'] = lt.newList('SINGLE_LINKED',
                                 cmpfunction=comparelikes)
    catalog['dislikes'] = lt.newList('SINGLE_LINKED',
                                 cmpfunction=comparedislikes)
    catalog['country'] = lt.newList('SINGLE_LINKED',
                                 cmpfunction=comparecountry)
    catalog['número_días'] = lt.newList('SINGLE_LINKED')

    return catalog


# Funciones para agregar informacion al catalogo

# Funciones para creacion de datos

# Funciones de consulta

# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento