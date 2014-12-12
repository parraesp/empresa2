from src.Profesor import Profesor
import os

__author__ = 'alberto'
import csv
import shutil
from tempfile import NamedTemporaryFile


class conexion_profesor():
    def __init__(self):
        self.__profesores= self.__listar_profesores()
    def guardar_profesor(self,profesor):
        f = open(os.path.dirname(__file__)+'/files/profesores.csv','a+')
        texto =''
        texto+=profesor.DNI+'\t'
        texto+=profesor.nombre+'\t'
        texto+=profesor.apellidos+'\t'
        texto+=profesor.movil+'\t'
        texto+=profesor.correo+'\t'
        texto+=profesor.fechaAlta+'\t'
        texto+=str(profesor.estado)+'\t'
        texto+=str(profesor.get_salario())+'\t'
        texto+=profesor.get_jornada()+'\n'
        f.write(texto)
        f.close()
        self.__profesores.append(profesor)

    def sacar_profesor(self,DNI):
        valor = -1
        cont = 0
        encontrado = False
        while(cont<len(self.__profesores) and not(encontrado)):
            if(self.__profesores[cont].DNI==DNI):
                encontrado = True
                valor=self.__profesores[cont]
            else:
                cont=cont+1
        return valor

    def dar_baja_profesor(self,DNI):
        cont = 0
        encontrado = False
        while(cont<len(self.__profesores) and not(encontrado)):
            if(self.__profesores[cont].DNI==DNI):
                encontrado = True
            else:
                cont=cont+1
        self.__profesores[cont].cambiar_estado()
        #Ahora lo cambiamos en el archivo
        tempfile = NamedTemporaryFile(delete=False)

        with open(os.path.dirname(__file__)+'/files/profesores.csv', 'rb') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter='\t')
            writer = csv.writer(tempfile, delimiter='\t')

            for row in reader:
                if(row[0]==self.__profesores[cont].DNI):
                    row[6]=False
                    writer.writerow(row)
                else:
                    writer.writerow(row)
        shutil.move(tempfile.name, os.path.dirname(__file__)+'/files/profesores.csv')
        csvFile.close()
        tempfile.close()

    def cambiar_profesor(self,DNI,nombre,apellidos,movil,correo,sueldo,jornada):
        cont = 0
        encontrado = False
        while(cont<len(self.__profesores) and not(encontrado)):
            if(self.__profesores[cont].DNI==DNI):
                encontrado = True
            else:
                cont=cont+1
        self.__profesores[cont].set_nombre(nombre)
        self.__profesores[cont].set_apellidos(apellidos)
        self.__profesores[cont].set_movil(movil)
        self.__profesores[cont].set_correo(correo)
        self.__profesores[cont].set_salario(sueldo)
        self.__profesores[cont].set_jornada(jornada)
        #Ahora lo cambiamos en el archivo
        tempfile = NamedTemporaryFile(delete=False)

        with open(os.path.dirname(__file__)+'/files/profesores.csv', 'rb') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter='\t')
            writer = csv.writer(tempfile, delimiter='\t')

            for row in reader:
                if(row[0]==self.__profesores[cont].DNI):
                    row[0]=DNI
                    row[1]=nombre
                    row[2]=apellidos
                    row[3]=movil
                    row[4]=correo
                    row[7]=sueldo
                    row[8]=jornada
                    writer.writerow(row)
                else:
                    writer.writerow(row)
        shutil.move(tempfile.name, os.path.dirname(__file__)+'/files/profesores.csv')
        csvFile.close()
        tempfile.close()
    def __listar_profesores(self):
        profesores = []
        with open(os.path.dirname(__file__)+'/files/profesores.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                profesor = Profesor(row[0],row[1],row[2],row[3],row[4],row[7],row[8],row[5],row[6])
                profesores.append(profesor)
        return profesores