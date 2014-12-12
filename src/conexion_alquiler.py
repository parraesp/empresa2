from src.Alquiler import Alquiler
import os

__author__ = 'alberto'
import csv
from datetime import datetime


class conexion_alquiler():

    def __init__(self, reservas, instalaciones):
        self.reservas = reservas
        self.instalaciones = instalaciones
        self.__alquileres = self.__listar_alquileres()

    def guardar_alquiler(self,alquiler):
        f = open(os.path.dirname(__file__)+'/files/alquileres.csv','a+')
        self.guardar_alquiler_fichero(alquiler,f)
        f.close()
        self.__alquileres.append(alquiler)

    def sacar_alquiler(self,reserva):
        valor = -1
        cont = 0
        encontrado = False
        while(cont<len(self.__alquileres) and not(encontrado)):
            if(self.__alquileres[cont].reserva == reserva):
                encontrado = True
                valor=self.__alquileres[cont]
            else:
                cont=cont+1
        return valor

    def devolver_alquiler(self,reserva):
        valor = -1
        cont = 0
        encontrado = False
        while(cont<len(self.__alquileres) and not(encontrado)):
            if(self.__alquileres[cont].reserva == reserva):
                encontrado = True
                self.__alquileres[cont].devuelto = True
                valor=self.__alquileres[cont]
            else:
                cont=cont+1

        f = open("src/files/alquileres.csv","w")
        for alq in self.__alquileres:
            self.guardar_alquiler_fichero(alq,f)
        f.close()
        return valor

    def guardar_alquiler_fichero(self,alquiler,fichero):
        texto =''
        texto +=alquiler.reserva.socio.DNI+'\t'
        texto+= str(alquiler.reserva.fecha)+'\t'
        for ins in alquiler.instalaciones:
            texto+=str(ins.id)+'\t'
        texto+=str(alquiler.devuelto)+'\n'
        fichero.write(texto)

    def __listar_alquileres(self):
        alquileres = []
        with open(os.path.dirname(__file__)+'/files/alquileres.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                fecha = datetime.strptime(row[1], "%d/%m/%y %H:%M")
                reserva = self.reservas.sacar_reserva(row[0],fecha)
                alquiler = Alquiler(reserva)
                for i in range(2,len(row)-1,1):
                    instalacion = self.instalaciones.sacar_instalacion(row[i])
                    alquiler.aniadir_instalacion(instalacion)
                if (row[len(row)-1] == 'True'):
                    alquiler.devuelto = True
                else:
                    alquiler.devuelto = False
                alquileres.append(alquiler)
        f.close()
        return alquileres