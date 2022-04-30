from .arista import Arista, AristaNoDirigida
from collections import deque 
from .nodo import Nodo
from queue import PriorityQueue
from pprint import pprint, pformat


class Grafo:
    def __init__(self) -> None:
        self.__aristas = []
        self.__ady = {}#o dict()
        self.__g_resultante = {} #definimos el grafo resultante

    def agregar_arista(self,arista: Arista):
        if arista not in self.__aristas:
            self.__aristas.append(arista)

    def __str__(self) -> str:
        return str([str(arista) for arista in self.__aristas])
    
    def eliminar_arista(self, arista: Arista):
        self.__aristas.remove(arista)

    def get_lista_ady(self) -> dict:
        self.__ady.clear()

        for arista in self.__aristas:
            if arista.dirigido():
                n1 = arista.get_nodo1() #Metemos el nodo en su posicion [0]
                n2 = arista.get_nodo2() #Metemos el nodo en su posicion [1]
                peso = arista.peso
                self.agregar_dict(n1,n2,peso)
                self.agregar_dict(n2,n1,peso)
            else:
                n1 = arista.get_nodo1()
                n2 = arista.get_nodo2()
                self.agregar_dict(n1,n2, arista.peso)
                self.agregar_dict(n2,n1, arista.peso)

        return self.__ady

    def print_ady(self):
        self.get_lista_ady()
        for key in self.__ady.keys():
            print(key, "----->", end="")

            for value in self.__ady[key]:
                nodo = value[0]
                peso = value[1]
                print(f"[{nodo}, {peso}]", ",", end="")
            print("\n")


    def agregar_dict(self,n1,n2,peso):
        if n1 in self.__ady:
            self.__ady[n1].append([n2, peso])
        else:
            self.__ady[n1] = [[n2,peso]]
    
    def recorrido_profundidad(self, inicio: Nodo):
        visitados = []
        pila = deque()
        recorrido = []

        grafo= self.get_lista_ady()

        if inicio not in grafo:
            return recorrido

        pila.append(inicio)
        visitados.append(inicio)

        while len(pila)>0:
            nodo = pila.pop()
            recorrido.append(nodo)

            for ady in grafo[nodo]:
                if ady[0] not in visitados:
                    pila.append(ady[0])
                    visitados.append(ady[0])
        return recorrido

    def recorrido_amplitud(self, inicio: Nodo):
        visitados = []
        cola = deque()
        resultado = []

        grafo=self.get_lista_ady()

        if inicio not in grafo:
            return resultado
            
        visitados.append(inicio)
        cola.append(inicio)

        while len(cola) > 0:
            vertice = cola[0]
            resultado.append(vertice)
            cola.popleft()
            for ady in grafo[vertice]:
                if ady[0] not in visitados:
                    cola.append(ady[0])
                    visitados.append(ady[0])
        return resultado

    def prim(self, inicio: Nodo):
            visitados = [] 
            pq = PriorityQueue()
            visitados.append(inicio)
            
            for ady in self.__ady[inicio]:
                pq.put((ady[1],inicio,ady[0]))
                
            while not pq.empty():
                arista = pq.get()
                peso = arista[0]
                origen = arista[1]
                destino = arista[2]

                if destino not in visitados:
                    visitados.append(destino)
                    for ady in self.__ady[destino]:
                        if ady[0] not in visitados:
                            pq.put((ady[1],destino,ady[0]))    
                    self.agregar_resultante(origen, destino, peso)
                    self.agregar_resultante(destino, origen, peso)


            for key in self.__g_resultante.keys():
                print(key,":", end="")
                for v in self.__g_resultante[key]:
                    nodo = v[0]
                    peso = v[1]
                    print("[("+str(nodo)+', '+str(peso)+"))", end="")
                print("]")



            return self.__g_resultante
        
    def agregar_resultante(self, n1, n2, peso):
        if n1 in self.__g_resultante:
            self.__g_resultante[n1].append([n2, peso])
        else:
            self.__g_resultante[n1] = [[n2, peso]]


    def kruskal(self, grafo:dict):
        #Definimos al grafo resultante
        arbol = [] #Arbol es una lista de aristas
        lista = []#lista ordenada

        for nodo, adyacentes in grafo.items(): #aqui se guarda nodo y adyacente en una lista de listas
            #por cada adyacente en mi lista de adyacente sacamos:
            for ady in adyacentes:

                peso = ady[1] #sacamos el peso de la poscion 0 
                destino = ady[0]#sacamos el destino en la posicion[1]
                arista = peso,nodo, destino #arista es una tupla que va de nodo destino y al principio peso
                lista.append(arista) #agregamos arista a lista

        #Ordenar la lista, con sort podemos usar una lamda, por cada sort ordena por la posicion 0
        lista.sort(key=lambda arista:arista[0]) #osea cero #reverse true para que saque el minimo
        #pprint(lista)

        ds = self.make_set(grafo) #regresa ds

        pprint(self.imprimir_cojunto(ds))
        #Definir el conjunto CONJUNTO DISJUNTO

        #Mientras no esta vacia la lista ordenada hacer:
        while len(lista) > 0:
            arista = lista[-1]
            lista.pop()
           # print(arista)
        #Hacer MAKESET: lo que hace es por cada crear un subconjunto, cada nodo va a estar dentro de una lista
            peso = arista[0]
            origen = arista[1] #sus posiciones
            destino = arista[2]
            
            if self.find_set(origen, ds) != self.find_set(destino, ds):
                arbol.append(arista) #le paso la arista que sacamos de la lista
                self.union(origen,destino, ds)
                print("arista: "+ "(" + str(peso) + ",",str(origen), str(destino) +")")
                print(self.imprimir_ds_aristas(ds))


                self.agregar_resultante(origen, destino, peso)
                self.agregar_resultante(destino, origen, peso)
            
        return arbol, self.__g_resultante


    def union(self, origen, destino, ds):
        i = self.find_set(origen, ds) # [a]
        j = self.find_set(destino, ds) # [d]

        l_origen = ds[i] #la lista de origen que se encuentra dejoinset en su poscion origen
        l_destino = ds[j] #la lista de destino que se encuenta dejoinset en su posicion destino
        l_uion = l_origen + l_destino #concateno [a, d]
        #sacamos donde se encuentra a y d
        
        ds.remove(l_origen) #eliminamos a 
        ds.remove(l_destino) #eliminamos d
        ds.append(l_uion) #ahora si agregmaos despues de borrar para que no esten repetidos

        
    #Creamos find set que recibe un nodo

    def find_set(self,nodo, ds):
        i = 0 
        while i < len(ds): #mientras sea menor de nuestro conjunto - disjunto
            if nodo in ds[i]:
                return i
            i = i + 1


    def make_set(self, grafo):
        ds = [] #Conjunto disjunto 

        #Por cada nodo en grafo
        for nodo in self.__ady:
            ds.append([nodo]) #agregar en el dejoin set el nodo
        return ds 
    
    #Para imprimir en orden las aristas de nuestro algoritmo
    def imprimir_ds_aristas(self, ds: list):
        string = "[ "
        for arista in ds:
            string += "["
            for nodo in arista:
                string += str(nodo)
            string += "] "
        string += "]" + "\n"
        return string
    #Para imprimir el conjunto del cual vamos a trabajar
    def imprimir_cojunto(self, ds: list):
         string = "["
         for arista in ds:
             for nodo in arista:
                 string += "[" + str(nodo) + "] "
                 StopIteration()
         string += "]"
         return string
    

    #Mostrar el grafo resultante 
    def mostrar_grafo(self, grafo: dict):
        string = ""
        for key in grafo.keys():
            string = string + str(key) + ":"
            for value in grafo[key]:
                nodo = value[0]
                peso = value[1]
                string = string + "[" + str(int(peso)) + str(nodo) + ")" + "]" + " "
            string = string + "\n"
        return string


    #Si find-set(origen) es diferente de find-set(destino):
        #Agregar la arista (distancia(origen, destino)) al grafo resultante
        #Unir los conjuntos donde se encuentra el origen y el destino


    #trabajar con la velocidad maxima

    
    def dijkstra(self,inicio:Nodo):
        distancias ={} #diccionario de distancias
        camino = {} 

        #por cada nodo en nuestro grafo
        for nodo in self.__ady:
            #distancias en su llave nodo sera un numero grande
            distancias[nodo]=10000
            #Porque aun no sabemos cual es el papa de cada nodo
            camino[nodo]=""

        distancias[inicio]= 0
        camino[inicio] = inicio
        
        #Creamos una cola de prioridad
        pq = PriorityQueue()
        #Metemos un nodo
        pq.put((0,inicio))
        
        #mientras no este vacia la lista ordenada
        while not pq.empty():

            #se extrae la lista ordenada del nodo n
            nodo = pq.get()

            #asignamos el exponente de n
            n = nodo[1]


            #por cada arista(conexion del nodo n hacer)
            for arista in self.__ady[n]:
                distancia = arista[1] + nodo[0]
                destino = arista[0]

                if distancia < distancias[destino]:
                     #si la distancia hacia el nodo destino + la distancia del nodo n2 es menor
            #que la distancia en el arreglo de distancias
                    distancias[destino] = distancia
                    #En el arreglo de camino se agrega en la posicion del nodo destino
                     #la conexion padre del nodo n extraido

                    camino[destino] = n                
                    
                #Se agrega a la lista ordenada el nodo destino
                    pq.put((distancia,destino))
        return distancias, camino
        
    