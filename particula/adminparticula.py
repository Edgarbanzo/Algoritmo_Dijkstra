from particula.algoritmos import distancia_euclidiana
from .particula import Particula
import json
from pprint import pprint, pformat
from .grafo import Grafo
from .nodo import Nodo
from .arista import Arista,AristaNoDirigida,AristaNoDirigidaPonderada

class AdminParticula:
    def __init__(self):
        self.__particulas = []
        self.__grafo = Grafo()


    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

    def __str__(self):
        return "".join(
            str(p) + '\n' for p in self.__particulas #programación funcional
        )
    def guardar(self, ubicacion):
        try:

            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                print(lista)
                json.dump(lista,archivo, indent=4)
            return 1
        except:
            return 0
            # archivo.write(str(self))
    
    def abrir(self,ubicacion):
        try:
            with open(ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
                return 1
        except:
            return 0

    def __len__(self):
        return len(self.__particulas)
    
    def __iter__(self): # para que sea iterable
        self.cont = 0

        return self # regresa el objeto
    
    def __next__(self): # es lo que llama la iteración (como una lista ligada)
        if self.cont < len(self.__particulas):
            p = self.__particulas[self.cont]
            self.cont += 1
            return p
        raise StopIteration #excepción

    def ordenar_por_id(self):
        self.__particulas.sort(key = lambda p: p.id)
    
    def ordenar_por_distancia(self):
        self.__particulas.sort(key= lambda p: p.distancia, reverse=True)
    
    def ordenar_por_velocidad(self):
        self.__particulas.sort(key=lambda p: p.velocidad)
    


    def ver_grafo(self):

        for p in self.__particulas:
            origen_x = p.origen_x
            origen_y = p.origen_y
            origen = (origen_x, origen_y)
            destino_x = p.destino_x
            destino_y = p.destino_y
            destino = (destino_x, destino_y)

            n1 = Nodo(origen)
            n2 = Nodo(destino)
        

            arista = AristaNoDirigidaPonderada(n1, n2)
            grafo = self.__grafo.agregar_arista(arista)
        
        return grafo
    
    def recorrido_profundidad(self, origen: Nodo):
        nodo = Nodo(origen)
        recorrido = self.__grafo.recorrido_profundidad(nodo)
        return recorrido

    def recorrido_amplitud(self, origen: Nodo):
        nodo = Nodo(origen)
        recorrido = self.__grafo.recorrido_amplitud(nodo)
        return recorrido

    def recorrido_toString(self, recorrido):
        cadena = ""
        for nodo in recorrido:
            cadena += str(nodo) + "\n"
        return cadena


#Funcion para obtener la lista para simplificar
    def lista(self):
        return self.__grafo.get_lista_ady()

#Creamos la funcion para crear un grafo pero ahora con el peso y el peso es nuestra velocidad
    def crear_grafo_velocidad(self) -> dict:
        for particula in self.__particulas:
            nodo1 = Nodo((particula.origen_x, particula.origen_y))
            nodo2 = Nodo((particula.destino_x, particula.destino_y))
            peso = particula.velocidad
            arista = AristaNoDirigidaPonderada(nodo1, nodo2, peso)
            grafo = self.__grafo.agregar_arista(arista)
        return grafo

#Creamos la funcion para mandar a llamar la funcion y pasar los parametros a nuesto algoritmo en grafos
    def kruskal(self, grafo: dict):
        grafo = self.__grafo.get_lista_ady()
        kruskal = self.__grafo.kruskal(grafo)
        return kruskal

#Conexion con el algoritmo de dijkstra
    def dijkstra(self, inicio: Nodo):
        nodo = Nodo(inicio)
        dijkstra = self.__grafo.dijkstra(nodo)
        return dijkstra
    #Funcion para mostrar el camino y distancias
    def mostrar_dijkstra(self,grafo:dict):
        for nodo,valor in grafo.items():
            print(nodo,':',valor)   

    #Funcion para crear un grafo con peso
    def crear_grafo_peso(self) -> dict:
        for particula in self.__particulas:
            nodo1 = Nodo((particula.origen_x, particula.origen_y))
            nodo2 = Nodo((particula.destino_x, particula.destino_y))
            peso = particula.distancia
            arista = AristaNoDirigidaPonderada(nodo1, nodo2, peso)
            grafo = self.__grafo.agregar_arista(arista)
        return grafo