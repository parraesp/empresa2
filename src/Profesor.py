from src.Socio import Socio

__author__ = 'alberto'


class Profesor(Socio):
    """
    Clase que gestiona los profesores del club
    """
    def __init__(self, DNI, nombre, apellidos, movil, correo , salario, jornada, *otros):
        """
        Constructor de la clase profesor

        :param: DNI
        :param: nombre
        :param: apellidos
        :param: movil
        :param: correo
        :param: salario
        :param: tipo de jornada
        :param: parametros a usar en caso de querer cargar un objeto de la persistencia en lugar de crear uno nuevo
        """
        if(len(otros) == 2):
            Socio.__init__(self, DNI, nombre, apellidos, movil, correo, otros[0], otros[1])
        else:
            Socio.__init__(self, DNI, nombre, apellidos, movil, correo)
        self.__salario = int(salario)
        self.__jornada = str(jornada)

    def set_salario(self, salario):
        """
        Asgina un nuevo salario a un profesor

        :param: salario
        """
        self.__salario = salario

    def set_jornada(self, jornada):
        """
        Asgina un nuevo tipo de jornada a un profesor

        :param: jornada
        """
        self.__jornada = jornada

    def get_salario(self):
        """
        Devuelve el salario de un profesor

        :return: salario
        """
        return self.__salario

    def get_jornada(self):
        """
        Devuelve el tipo de jornada que tiene un profesor

        :return: jornada
        """
        return self.__jornada