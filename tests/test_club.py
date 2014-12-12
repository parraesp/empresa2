from unittest import TestCase
from src.Club import Club
from src.Socio import Socio
from src.Profesor import Profesor
from mockito import mock

__author__ = 'Ricardo'


class TestClub(TestCase):
    def test_validarDNI(self):
        club = Club()
        self.assertTrue(club.validarDNI('12345678A'))
        self.assertTrue(club.validarDNI('12345678a'))
        self.assertFalse(club.validarDNI('olakase'))
        self.assertFalse(club.validarDNI('123456789'))
        self.assertFalse(club.validarDNI(''))
        self.assertFalse(club.validarDNI('12345678-a'))
        self.assertFalse(club.validarDNI('1234567a8'))

    def test_obtener_socio(self):
        club = Club()
        self.assertIsInstance(club.obtener_socio("49116999K"), Socio)
        self.assertEqual(club.obtener_socio("socioNoExistente"), -1)

    def test_editar_socio(self):
        club = Club()
        club.editar_socio("49116999K","Juan Jose", "Perez","666209821","email_nuevo@example.org")
        socio = club.obtener_socio("49116999K")
        self.assertEqual(socio.nombre,"Juan Jose")
        self.assertEqual(socio.apellidos,"Perez")
        self.assertEqual(socio.movil,"666209821")
        self.assertEqual(socio.correo,"email_nuevo@example.org")

    def test_dar_baja_socio(self):
        club = Club()
        club.dar_baja_socio("49116999K")
        socio = club.obtener_socio("49116999K")
        self.assertFalse(socio.estado)

    def alta_socio(self):
        club = Club()
        club.alta_socio("49116999J","Ernesto", "de la Serna","633456564","rotesherztz@mail.de")
        socio = club.obtener_socio("49116999J")
        self.assertEqual(socio.nombre,"Ernesto")
        self.assertEqual(socio.apellidos,"de la Serna")
        self.assertEqual(socio.movil,"633456564")
        self.assertEqual(socio.correo,"rotesherztz@mail.de")

    def test_obtener_profesor(self):
        club = Club()
        self.assertIsInstance(club.obtener_profesor("25335374T"), Profesor)
        self.assertEqual(club.obtener_profesor("profesorNoExistente"), -1)

    def test_editar_profesor(self):
        club = Club()
        club.editar_profesor("25335374T","Don Juan", "Tenorio","666209821","email_nuevo@example.org",2500,"Completa")
        profesor = club.obtener_profesor("25335374T")
        self.assertEqual(profesor.nombre,"Don Juan")
        self.assertEqual(profesor.apellidos,"Tenorio")
        self.assertEqual(profesor.movil,"666209821")
        self.assertEqual(profesor.correo,"email_nuevo@example.org")
        self.assertEqual(profesor.get_salario(),2500)
        self.assertEqual(profesor.get_jornada(),"Completa")

    def test_dar_baja_profesor(self):
        club = Club()
        club.dar_baja_profesor("25335374T")
        profesor = club.obtener_profesor("25335374T")
        self.assertFalse(profesor.estado)

    def alta_profesor(self):
        club = Club()
        club.alta_profesor("49116999A","Eva", "Castro","733456564","eslebt@derkom.in",3000,"Completa")
        profesor = club.obtener_profesor("49116999A")
        self.assertEqual(profesor.nombre,"Eva")
        self.assertEqual(profesor.apellidos,"Castro")
        self.assertEqual(profesor.movil,"733456564")
        self.assertEqual(profesor.correo,"eslebt@derkom.in")
        self.assertEqual(profesor.get_salario(),3000)
        self.assertEqual(profesor.get_jornada(),"Completa")