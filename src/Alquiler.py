__author__ = 'Ricardo'


class Alquiler():
    def is_devuelto(self):
        return self.__devuelto

    def get_reserva(self):
        return self.__reserva

    def get_instalaciones(self):
        return self.__instalaciones

    def aniadir_instalacion(self, instalacion):
        self.__instalaciones.append(instalacion)

    def set_devuelto(self, devuelto):
        self.__devuelto = devuelto

    reserva = property(get_reserva)
    instalaciones = property(get_instalaciones)
    devuelto = property(is_devuelto, set_devuelto)

    def __init__(self, reserva):
        self.__reserva = reserva
        self.__instalaciones = []
        self.__devuelto = False

    def __str__(self):
        texto = self.__reserva.__str__()+','
        for i in self.__instalaciones:
            texto += str(i.__str__())
        texto += str(self.devuelto)
        return texto