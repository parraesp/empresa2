from src.Socio import Socio
__author__ = 'alberto'
import csv
import shutil
import os
from tempfile import NamedTemporaryFile


class conexion_socio():
    def __init__(self):
        self.__socios = self.__listar_socios()

    def __listar_socios(self):
        socios = []
        with open(os.path.dirname(__file__)+'/files/socios.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                socio = Socio(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
                socios.append(socio)
        f.close()
        return socios
    def guardar_socio(self,socio):
        f = open(os.path.dirname(__file__)+'/files/socios.csv','a+')
        texto =''
        texto+=socio.DNI+'\t'
        texto+=socio.nombre+'\t'
        texto+=socio.apellidos+'\t'
        texto+=socio.movil+'\t'
        texto+=socio.correo+'\t'
        texto+=socio.fechaAlta+'\t'
        texto+=str(socio.estado)+'\n'
        f.write(texto)
        f.close()
        self.__socios.append(socio)

    def sacar_socio(self,DNI):
        valor = -1
        cont = 0
        encontrado = False
        while(cont<len(self.__socios) and not(encontrado)):
            if(self.__socios[cont].DNI==DNI):
                encontrado = True
                valor=self.__socios[cont]
            else:
                cont=cont+1
        return valor

    def dar_baja_socio(self,socio):
        ind = self.__socios.index(socio)
        self.__socios[ind].cambiar_estado()
        #Ahora lo cambiamos en el archivo
        tempfile = NamedTemporaryFile(delete=False)

        with open(os.path.dirname(__file__)+'/files/socios.csv', 'rb') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter='\t')
            writer = csv.writer(tempfile, delimiter='\t')

            for row in reader:
                if(row[0]==self.__socios[ind].DNI):
                    row[6]=False
                    writer.writerow(row)
                else:
                    writer.writerow(row)
        shutil.move(tempfile.name, os.path.dirname(__file__)+'/files/socios.csv')
        csvFile.close()
        tempfile.close()

    def cambiar_socio(self,DNI,nombre,apellidos,movil,correo):
        cont = 0
        encontrado = False
        while(cont<len(self.__socios) and not(encontrado)):
            if(self.__socios[cont].DNI==DNI):
                encontrado = True
            else:
                cont=cont+1
        self.__socios[cont].set_nombre(nombre)
        self.__socios[cont].set_apellidos(apellidos)
        self.__socios[cont].set_movil(movil)
        self.__socios[cont].set_correo(correo)
        #Ahora lo cambiamos en el archivo
        tempfile = NamedTemporaryFile(delete=False)

        with open(os.path.dirname(__file__)+'/files/socios.csv', 'rb') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter='\t')
            writer = csv.writer(tempfile, delimiter='\t')

            for row in reader:
                if(row[0]==self.__socios[cont].DNI):
                    row[0]=DNI
                    row[1]=nombre
                    row[2]=apellidos
                    row[3]=movil
                    row[4]=correo
                    writer.writerow(row)
                else:
                    writer.writerow(row)
        shutil.move(tempfile.name, os.path.dirname(__file__)+'/files/socios.csv')
        csvFile.close()
        tempfile.close()