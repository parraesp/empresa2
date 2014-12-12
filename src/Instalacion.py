__author__ = 'Ricardo'


class Instalacion():
    def get_descripcion(self):
        return self.__descripcion

    def get_precio(self):
        return self.__precio

    def get_instalacion_id(self):
        return self.__instalacion_id

    id = property(get_instalacion_id)
    descripcion = property(get_descripcion)
    precio = property(get_precio)

    def __init__(self, instalacion_id, descripcion, precio):
        self.__instalacion_id = instalacion_id
        self.__precio = precio
        self.__descripcion = descripcion

    def __str__(self):
        return self.id + ','+self.descripcion
