from src.Torneo import Torneo
import os
__author__ = 'alberto'
import csv
class conexion_torneo():

    def __init__(self,socios):
        self.socios = socios
        self.__torneos = self.__listar_torneos()

    def guardar_torneo(self,torneo):
        f = open(os.path.dirname(__file__)+'/files/torneos.csv','a+')
        self.guardar_torneo_fichero(torneo,f)
        f.close()
        self.__torneos.append(torneo)

    def guardar_torneo_fichero(self,torneo,f):
        texto =''
        texto+=torneo.nombre+'\t'
        for s in torneo.socios:
            texto+=s.DNI+'\t'
        for r in torneo.resultados:
            texto+= r+'\t'
            texto+= str(torneo.resultados[r])+'\t'
        texto+='\n'
        f.write(texto)

    def sacar_torneo(self,nombre):
        valor = -1
        cont = 0
        encontrado = False
        while(cont<len(self.__torneos) and not(encontrado)):
            if(self.__torneos[cont].nombre == nombre):
                encontrado = True
                valor=self.__torneos[cont]
            else:
                cont=cont+1
        return valor

    def poner_resultado(self, torneo, partido,resultado):
        torneo.set_resultado(partido,resultado)
        f = open("src/files/torneos.csv","w")
        for t in self.__torneos:
            self.guardar_torneo_fichero(t,f)
        f.close()

    def borrar_torneo(self,torneo):
        self.__torneos.remove(torneo)
        f = open("src/files/torneos.csv","r")
        torneos = f.readlines()
        f.close()

        f = open("src/files/torneos.csv","w")
        for t in torneos:
            tAux = t.split("\t")
            if tAux[0]!=torneo.nombre:
                f.write(t)
        f.close()


    def __listar_torneos(self):
        torneos = []
        with open(os.path.dirname(__file__)+'/files/torneos.csv') as f:
            content = csv.reader(f, delimiter='\t')
            for row in content:
                if row:
                    socios=[]
                    for i in range(1,9,1):
                        socios.append(self.socios.sacar_socio(row[i]))
                    torneo = Torneo(row[0],socios)
                    for i in range(9,23,2):
                        torneo.set_resultado(row[i],row[i+1])
                    torneos.append(torneo)
        f.close()
        return torneos