from src.Instalacion import Instalacion
import os
__author__ = 'alberto'
import csv
class conexion_instalacion():
    def __init__(self):
        self.__instalaciones = self.__listar_instalaciones()
    def sacar_instalacion(self,instalacionID):
        instalacion = False
        with open(os.path.dirname(__file__)+'/files/instalaciones.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                if(row[0]==instalacionID):
                    instalacion =  Instalacion(row[0],row[1],row[2])
        f.close()
        return instalacion

    def __listar_instalaciones(self):
        instalaciones = []
        with open(os.path.dirname(__file__)+'/files/instalaciones.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                instalacion = Instalacion(row[0],row[1],row[2])
                instalaciones.append(instalacion)
        f.close()
        return instalaciones