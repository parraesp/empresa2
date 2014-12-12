__author__ = 'alberto'


class Clase():
    """
        Clase para gestionar clases de padel.
    """
    def __init__(self, profesor, reserva):
        """
        Constructor de la clase departamento

        :param: Profesor que impartira la clase
        :param: Reserva asociada a la clase
        """
        self.__profesor = profesor
        self.__reserva = reserva

    def get_profesor(self):
        """
        Devuelve el profesor de una determinada clase

        :return: Profesor
        """
        return self.__profesor

    def get_reserva(self):
        """
        Devuelve la reserva de una determinada clase

        :return: Reserva
        """
        return self.__reserva

    def set_profesor(self, profesor):
        """
        Asigna un profesor a una clase

        :param: Profesor
        """
        self.__profesor = profesor

    def set_reservaI(self, reserva):
        """
        Asigna una reserva a una clase

        :param: Reserva
        """
        self.__reserva = reserva

    def __str__(self):
        """
        Devuelve en una cadena toda la informacion de una clase

        :return: Clase
        """
        return self.__profesor.__str__()+self.__reserva.__str__()