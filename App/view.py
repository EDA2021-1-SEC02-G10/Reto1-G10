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
from DISClib.ADT import list as lt
assert cf


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
    #print("5- Consultar los x videos con mas likes en un país específico con un tag específico") numero 4
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
        tipo_lista = int(input("escriba 1 si quiere usar SINGLE_LINKED, de lo contrario escriba 0:"))
        print("Cargando información de los archivos ....")
        catalog = controller.initCatalog(tipo_lista)
        loadData(catalog)
    elif int(inputs[0]) == 2:
        F_ordenamiento= int(input("ingrese 1 para selection, 2 para insertion y 3 shell:"))
        size = int(input("ingrese el size de la lista:"))
        Tipo_orden = controller.tipo_de_orden(F_ordenamiento, catalog, size)
        print(Tipo_orden[0])
        numero=input("Buscando los top ?:")
        video1=input("Cuál es el primer video que quiere comparar?:")  
        video2=input("Cuál es el segundo video que quiere comparar?:")  
        VideosByViews = VideosByViews(video1,video2)
    elif int(inputs[0]) == 3:
        pais=input("Cúal país quiere buscar?:")
    elif int(inputs[0]) == 4:
        categoria=input("Cúal categoria quiere buscar?:")
          
        
    else:
        sys.exit(0)
sys.exit(0)
