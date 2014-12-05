__author__ = 'Alberto L'


class Empleado:
    """
    Clase que gestiona todos los atributos de un empleado
    """
    def __init__(self, nombre, apellidos, dni, direccion, edad, email, salario):
        """
        Constructor de la clase empleado

        :param nombre: nombre del empleado
        :param apellidos: apellidos del empleado
        :param dni: DNI del empleado
        :param direccion: direccion del empleado
        :param edad: edad del empleado
        :param email: email del empleado
        :param salario: salario del empleado
        :type salario: entero
        """
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.edad = edad
        self.email = email
        self.salario = salario

    def get_salario(self):
        """
        Devuelve el salario del empleado

        :return: Salario
        """
        return self.salario

    def get_dni(self):
        """
        Devuelve el DNI del empleado

        :return: DNI
        """
        return self.dni

    def get_nombre_apellidos(self):
        """
        Devuelve el nombre del empleado

        :return: Nombre
        """
        return self.nombre + " " + self.apellidos

    def get_edad(self):
        """
        Devuelve el edad del empleado

        :return: Edad
        """
        return self.edad

    def get_email(self):
        """
        Devuelve el email del empleado

        :return: Email
        """
        return self.email

    def get_salario_mensual(self):
        """
        Devuelve el salario mensual del empleado

        :return: Salario
        """
        return self.salario/12.0
