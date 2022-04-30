from typing import List
from .nodo import Nodo

class Arista:
    def __init__(self, n1:Nodo,n2:Nodo) -> None:
        self.__par = [n1, n2]

    def get_par(self) -> list:
        return self.__par 
    
    def __str__(self) -> str:
        return f"{self.get_par()[0]} {self.get_par()[1]}"

    def dirigido(self) -> bool:
        return False
    
    def ponderado(self) -> bool:
        return True

    def __eq__(self, o: object) -> bool:
        return self.get_par()[0] == o.get_par()[0] and self.get_par()[1] == o.get_par()[1]
    
    def get_nodo1(self) -> Nodo:
        return self.get_par()[0]

    def get_nodo2(self) -> Nodo:
        return self.get_par()[1]


class AristaNoDirigida(Arista):
    def __init__(self, n1: Nodo, n2: Nodo) -> None:
        super().__init__(n1, n2)

    def dirigido(self) -> bool:
        return False

    def ponderado(self) -> bool:
        return False

    def get_nodo1(self) -> Nodo:
        return self.get_par()[0]

    def get_nodo2(self) -> Nodo:
        return self.get_par()[1]


    def __str__(self) -> str:
        return f"{self.get_par()[0]} {self.get_par()[1]}"

class Ponderada:
    def __init__(self, peso) -> None:
        self.__peso = peso

    @property
    def peso(self):
        return self.__peso

class AristaNoDirigidaPonderada(AristaNoDirigida, Ponderada):
    def __init__(self, n1: Nodo, n2: Nodo, peso) -> None:
        AristaNoDirigida.__init__(self, n1, n2)
        Ponderada.__init__(self, peso)

    def ponderado(self) -> bool:
        return True

    def __str__(self) -> str:
        return f"(Nodo: {self.get_par()[0]} ) <-----Artista: {self.peso} -------> (Nodo: {self.get_par()[1]})"

class AristaDirigidaPonderada(Arista, Ponderada):
    def __init__(self, n1: Nodo, n2: Nodo,peso) -> None:
        Arista.__init__(self,n1,n2)
        Ponderada.__init__(self,peso)
        #le pasamos origen destino y el peso

#Ahora si es ponderada y difigida
    def ponderado(self) -> bool:
        return True
    
    def dirigido(self) -> bool:
        return True

#Nos regresa un objeto de la clase nodo(un nodo osea origen x)
    def get_nodo1(self) -> Nodo:
        return self.get_par()[0]

#Nos regresa un objeto de la clase nodo(un nodo destino)
    def get_nodo2(self) -> Nodo:
        return self.get_par()[1]


#Tiene sus propios metodos para imprimir
    def __str__(self) -> str:
        return f"(Nodo: {self.get_par()[0]})-----|Artista {self.peso}|-------> (Nodo: {self.get_par()[1]})"