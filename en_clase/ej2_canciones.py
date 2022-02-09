"""Ejercicio 2
Desarrolla una clase CD con los siguientes atributos:
    - canciones: un array de objetos de la clase Cancion.
    - contador: la siguiente posición libre del array canciones.

y los siguientes métodos:
    - CD(): constructor predeterminado (creará el array canciones).
    - numeroCanciones(): devuelve el valor del contador de canciones.
    - dameCancion(int): devuelve la Cancion que se encuentra en la posición indicada.
    - grabaCancion(int, Cancion): cambia la Cancion de la posición indicada por la nueva 
        Cancion proporcionada.
    - agrega(Cancion): agrega al final del array la Cancion proporcionada.
    - elimina(int): elimina la Cancion que se encuentra en la posición indicada."""



class Cancion():
    def __init__(self, nombre='', autor='') -> None:
        self.nombre = nombre
        self.autor = autor

class CD():
    def __init__(self,lista=[]) -> None:
        self.list_canciones = lista
        self.contador = len(self.list_canciones)

    def agrega_cancion(self, tema):
        self.list_canciones.append(tema)
        self.contador = len(self.list_canciones)

    def elimina_cancion(self, indice):
        self.list_canciones.pop(indice)
        self.contador = len(self.list_canciones)

    def numero_canciones(self):
        pass