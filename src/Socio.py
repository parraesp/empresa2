__author__ = 'francisco'

import time


class Socio():
    """
    Clase encargada de gestionar los socios del club
    """
    def __init__(self, DNI, nombre, apellidos, movil, correo, *otros):
        """
        Constructor de la clase socio.

        :param: DNI
        :param: nombre
        :param: apellidos
        :param: movil
        :param: correo
        :param: parametros a usar en caso de querer cargar un objeto de la persistencia en lugar de crear uno nuevo
        """
        self.__DNI = str(DNI)
        self.__nombre = str(nombre)
        self.__apellidos = str(apellidos)
        self.__movil = str(movil)
        self.__correo = str(correo)
        if (len(otros) == 2):
            self.__fechaAlta = otros[0]
            self.__estado = bool(otros[1])
        else:
            self.__fechaAlta = str(time.strftime("%d/%m/%y"))
            self.__estado = True

    def __str__(self):
        """
        Devuelve los datos de un socio en forma de cadena

        :return: Socio
        """
        return 'DNI: ' + self.__DNI + ', fecha: ' + self.__fechaAlta \
               + ', estado: ' + str(self.__estado)+', correo: ' + str(self.correo)

    def get_DNI(self):
        """
        Devuelve el DNI de un socio

        :return: DNI
        """
        return self.__DNI

    def get_nombre(self):
        """
        Devuelve el nombre de un socio

        :return: nombre
        """
        return self.__nombre

    def get_apellidos(self):
        """
        Devuelve los apellidos de un socio

        :return: apellidos
        """
        return self.__apellidos

    def get_movil(self):
        """
        Devuelve el movil de un socio

        :return: movil
        """
        return self.__movil

    def get_correo(self):
        """
        Devuelve el correo electronico de un socio

        :return: correo
        """
        return self.__correo

    def get_fechaAlta(self):
        """
        Devuelve la fecha de alta de un socio

        :return: fecha_alta
        """
        return self.__fechaAlta

    def get_estado(self):
        """
        Devuelve el estado de un socio

        :return: estado
        """
        return self.__estado

    def set_DNI(self, DNI):
        """
        Asigna un nuevo DNI a un determinado usuario

        :param: DNI
        """
        self.__DNI = DNI

    def cambiar_estado(self):
        """
        Asigna el estado del usuario a "dado de baja"
        """
        self.__estado = False

    def set_fechaAlta(self, fecha):
        """
        Asigna una nueva fecha de alta

        :param: fecha de alta
        """
        self.__fechaAlta = fecha

    def set_nombre(self, nombre):
        """
        Asigna un nuevo nombre a un socio

        :param: nombre
        """
        self.__nombre = nombre

    def set_apellidos(self, apellidos):
        """
        Asigna nuevo(s) apellido(s) al socio
        :param: apellido(s)
        """
        self.__apellidos = apellidos

    def set_correo(self, correo):
        """
        Asigna un nuevo correo electronico

        :param: correo electronico
        """
        self.__correo = correo

    def set_movil(self, movil):
        """
        Asigna un nuevo movil

        :param: movil
        """
        self.__movil = movil

    DNI = property(get_DNI)
    nombre = property(get_nombre)
    apellidos = property(get_apellidos)
    movil = property(get_movil)
    correo = property(get_correo)
    fechaAlta = property(get_fechaAlta, set_fechaAlta)
    estado = property(get_estado)
