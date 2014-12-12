from src.Reserva import Reserva

__author__ = 'alberto'
import csv
import os

class conexion_reserva():
    def __init__(self, socios, instalaciones):
        self.__socios = socios
        self.__instalaciones = instalaciones
        self.__reservas = self.__listar_reservas()
    def guardar_reserva(self,reserva):
        f = open(os.path.dirname(__file__)+'/files/reservas.csv','a+')
        texto =''
        texto+= str(reserva.socio.DNI)+'\t'
        texto+=str(reserva.fecha)+'\t'
        texto+=str(reserva.instalacion.id)+'\n'
        f.write(texto)
        f.close()
        self.__reservas.append(reserva)

    def sacar_reserva(self,DNI, fecha):
        valor = -1
        cont = 0
        encontrado = False
        while(cont<len(self.__reservas) and not(encontrado)):
            if(self.__reservas[cont].fecha==fecha.strftime("%d/%m/%y %H:%M") and
            self.__reservas[cont].socio.DNI == DNI):
                encontrado = True
                valor=self.__reservas[cont]
            else:
                cont=cont+1
        return valor

    def borrar_reserva(self,DNI,fecha):
        borrado = False
        reserva = self.sacar_reserva(DNI,fecha)
        if (reserva != -1):
            borrado = True
            self.__reservas.remove(reserva)
            f = open("src/files/reservas.csv","r")
            reservas = f.readlines()
            f.close()

            f = open("src/files/reservas.csv","w")
            for res in reservas:
                resAux = res.split("\t")
                if resAux[1]!=fecha.strftime("%d/%m/%y %H:%M") and resAux[0] != DNI:
                    f.write(res)
            f.close()
        return borrado

    def __listar_reservas(self):
        reservas = []
        with open(os.path.dirname(__file__)+'/files/reservas.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                socio = self.__socios.sacar_socio(row[0])
                instalacion = self.__instalaciones.sacar_instalacion(row[2])
                reserva = Reserva(socio,row[1],instalacion)
                reservas.append(reserva)
        f.close()
        return reservas