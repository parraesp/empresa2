__author__ = 'Alberto L'


class Departamento:
    """
        Clase para gestionar departamentos
    """
    def __init__(self, nombre_depto, id_depto):
        """
        Constructor de la clase departamento

        :param: Nombre del departamento a crear
        :param: Identificador del departamento
        """
        self.nombre_depto = nombre_depto
        self.id_depto = id_depto
        self.lista_empleados = []

    def aniadir_empleado(self, empleado):
        """
        Aniade un empleado al departamento

        :param: Empleado
        """
        self.lista_empleados.append(empleado)

    def get_salario_total(self):
        """
        Devuelve el salario total del departamento

        :return: Salario_dpto
        """
        suma = 0
        for i in self.lista_empleados:
            suma += i.get_salario()
        return suma

    def get_nombre_depto(self):
        """
        Devuelve el nombre del departamento

        :return: Nombre
        """
        return self.nombre_depto

    def get_salario_total_mensual(self):
        """
        Devuelve el salario mensual del dpto

        :return: Salario_mensual
        """
        suma = 0.0
        for i in self.lista_empleados:
            suma += i.get_salario_mensual()
        return suma
