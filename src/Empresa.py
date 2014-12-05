__author__ = 'alberto'

class Empresa():
    """
    La clase empresa contiene el conjunto de departamentos de la empresa
    """
    def __init__(self, nombre_empresa, cif, razon_social):
        """
        Constructor de la clase empresa

        :param nombre_empresa: nombre de la empresa
        :param cif: cif de la empresa
        :param razon_social: motivo de creacion de la empresa
        :param departamentos: departamentos de la empresa
        :param type departamentos: Departamento
        """
        self.nombre_empresa = nombre_empresa
        self.cif = cif
        self.razon_social = razon_social
        self.lista_departamentos = []
