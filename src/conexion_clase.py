from src import Clase
import os

__author__ = 'alberto'
import csv
import shutil
from tempfile import NamedTemporaryFile
from datetime import datetime
class conexion_clase():
    def __init__(self):
        self.__clases = self.__listar_clases()

    def sacar_clase(self,profesor, fecha):
        valor = -1
        cont = 0
        encontrado = False
        while(cont<len(self.__clases) and not(encontrado)):
            if(self.__clases[cont].get_profesor().DNI==profesor and self.__clases[cont].get_reserva().get_fecha()==fecha):
                encontrado = True
                valor=self.__clases[cont]
            else:
                cont=cont+1
        return valor

    def guardar_clase(self,clase):
        f = open(os.path.dirname(__file__)+'/files/clases.csv','a+')
        texto =''
        texto+= clase.get_profesor().get_DNI()+'\t'
        texto+= str(clase.get_reserva().get_fecha().strftime("%d/%m/%y %H:%M"))+'\n'
        f.write(texto)
        f.close()
        self.__clases.append(clase)

    def borrar_clase(self,profesor,fecha):
        tempfile = NamedTemporaryFile(delete=False)

        with open(os.path.dirname(__file__)+'/files/clases.csv', 'rb') as csvFile, tempfile:
            reader = csv.reader(csvFile, delimiter='\t')
            writer = csv.writer(tempfile, delimiter='\t')

            for row in reader:
                if(row[0]!=profesor and row[1]!=str(fecha)):
                    writer.writerow(row)
        shutil.move(tempfile.name, os.path.dirname(__file__)+'/files/clases.csv')
        csvFile.close()
        tempfile.close()

    def __listar_clases(self):
        clases = []
        with open(os.path.dirname(__file__)+'/files/clases.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                fecha = datetime.strptime(row[1], "%d/%m/%y %H:%M")
                clase = Clase(self.sacar_profesor(row[0]),self.sacar_reserva(fecha))
                clases.append(clase)
        f.close()
        return clases