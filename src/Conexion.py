from src.conexion_reserva import conexion_reserva
from src.conexion_profesor import conexion_profesor
from src.conexion_alquiler import conexion_alquiler
from src.conexion_clase import conexion_clase
from src.conexion_instalacion import conexion_instalacion
from src.conexion_socio import conexion_socio
from src.conexion_torneo import conexion_torneo

__author__ = 'alberto'


class Conexion():

    def __init__(self):
        self.__conexion_socio = conexion_socio()
        self.__conexion_profesor = conexion_profesor()
        self.__conexion_instalacion = conexion_instalacion()
        self.__conexion_reserva = conexion_reserva(self.__conexion_socio, self.__conexion_instalacion)
        self.__conexion_alquiler = conexion_alquiler(self.__conexion_reserva, self.__conexion_instalacion)
        self.__conexion_clase = conexion_clase()

        self.__conexion_torneo = conexion_torneo(self.__conexion_socio)


    def guardar_socio(self,socio):
        self.__conexion_socio.guardar_socio(socio)

    def guardar_profesor(self,profesor):
        self.__conexion_profesor.guardar_profesor(profesor)

    def sacar_socio(self,DNI):
        return self.__conexion_socio.sacar_socio(DNI)

    def sacar_profesor(self,DNI):
        return self.__conexion_profesor.sacar_profesor(DNI)

    def dar_baja_socio(self,socio):
        self.__conexion_socio.dar_baja_socio(socio)

    def dar_baja_profesor(self,DNI):
        self.__conexion_profesor.dar_baja_profesor(DNI)

    def sacar_instalacion(self,instalacionID):
        return self.__conexion_instalacion.sacar_instalacion(instalacionID)

    def sacar_clase(self,profesor, fecha):
        return self.__conexion_clase.sacar_clase(profesor,fecha)

    def guardar_reserva(self,reserva):
        self.__conexion_reserva.guardar_reserva(reserva)

    def guardar_clase(self,clase):
        self.__conexion_clase.guardar_clase(clase)

    def sacar_reserva(self,DNI, fecha):
        return self.__conexion_reserva.sacar_reserva(DNI,fecha)

    def borrar_reserva(self,DNI,fecha):
        return self.__conexion_reserva.borrar_reserva(DNI,fecha)

    def guardar_alquiler(self,alquiler):
        self.__conexion_alquiler.guardar_alquiler(alquiler)

    def sacar_alquiler(self,reserva):
        return self.__conexion_alquiler.sacar_alquiler(reserva)

    def devolver_alquiler(self,reserva):
        return self.__conexion_alquiler.devolver_alquiler(reserva)

    def guardar_alquiler_fichero(self,alquiler,fichero):
        self.__conexion_alquiler.guardar_alquiler_fichero(alquiler,fichero)

    def borrar_clase(self,profesor,fecha):
        self.__conexion_clase.borrar_clase(profesor,fecha)

    def cambiar_socio(self,DNI,nombre,apellidos,movil,correo):
        self.__conexion_socio.cambiar_socio(DNI,nombre,apellidos,movil,correo)

    def cambiar_profesor(self,DNI,nombre,apellidos,movil,correo,sueldo,jornada):
        self.__conexion_profesor.cambiar_profesor(DNI,nombre,apellidos,movil,correo,sueldo,jornada)

    def guardar_torneo(self,torneo):
        self.__conexion_torneo.guardar_torneo(torneo)

    def guardar_torneo_fichero(self,torneo,f):
        self.__conexion_torneo.guardar_torneo_fichero(torneo,f)

    def sacar_torneo(self,nombre):
        return self.__conexion_torneo.sacar_torneo(nombre)

    def poner_resultado(self, torneo, partido,resultado):
        self.__conexion_torneo.poner_resultado(torneo, partido,resultado)

    def borrar_torneo(self,torneo):
        self.__conexion_torneo.borrar_torneo(torneo)