from src.Club import Club

__author__ = 'alberto'


def pedir_reserva():
    DNI = raw_input('DNI del socio que desea reservar: ')
    while not club.validarDNI(DNI):
                print '\033[91m'+'El DNI no tiene un formato correcto.'+'\033[0m'
                DNI =raw_input('DNI: ')
    fecha = raw_input('Fecha y hora para la reserva (dd/mm/aa HH): ')
    while not club.validarFecha(fecha):
                print '\033[91m'+'La fecha no tiene un formato correcto.'+'\033[0m'
                fecha = raw_input('Fecha y hora para la reserva (dd/mm/aa HH): ')
    instalacionID = raw_input('Pista que desea reservar: ')
    while not club.validarInstalacion(instalacionID):
                print '\033[91m'+'La instalacion no existe.'+'\033[0m'
                instalacionID = raw_input('Pista que desea reservar: ')
    return club.crear_reserva(DNI,fecha, instalacionID)

def consultar_reserva():
    DNI = raw_input('DNI del socio que ha reservado: ')
    while not club.validarDNI(DNI):
                print '\033[91m'+'El DNI no tiene un formato correcto.'+'\033[0m'
                DNI =raw_input('DNI: ')
    fecha = raw_input('Fecha y hora para la reserva (dd/mm/aa HH): ')
    while not club.validarFecha(fecha):
                print '\033[91m'+'La fecha no tiene un formato correcto.'+'\033[0m'
                fecha = raw_input('Fecha y hora para la reserva (dd/mm/aa HH): ')
    reserva = club.consultar_reserva(DNI, fecha)
    return reserva

def pedir_datos_persona():
    DNI =raw_input('DNI: ')
    while not club.validarDNI(DNI):
        print '\033[91m'+'El DNI no tiene un formato correcto.'+'\033[0m'
        DNI =raw_input('DNI: ')
    nombre = raw_input('Nombre: ')
    apellidos = raw_input('Apellidos: ')
    movil = raw_input('Movil: ')
    while not club.validarTelefono(movil):
        print '\033[91m'+'El telefono no tiene un formato correcto. Deben ser 9 digitos'+'\033[0m'
        movil = raw_input('Movil: ')
    correo = raw_input('Correo electronico: ')
    while not club.validarEmail(correo):
        print '\033[91m'+'El email no es correcto.'+'\033[0m'
        correo = raw_input('Correo electronico: ')
    datos = [DNI,nombre,apellidos,movil,correo]
    return datos


seleccion = -1
print 'Bienvenido al sistema de gestion de clubes de padel'
print '==================================================='
print "Cargando el club..."
club = Club()
print "Club cargado"
while(seleccion!='0'):
    print '1. Socios'
    print '2. Reservas'
    print '3. Alquileres'
    print '4. Profesores'
    print '5. Clases'
    print '6. Torneos'
    print '0. Salir'
    seleccion = raw_input('Haga su seleccion: ')

    if(seleccion=='1'):
        print 'Haga su seleccion: '
        print '1. Crear socio'
        print '2. Editar socio'
        print '3. Dar socio de baja'
        print '4. Consultar socio'
        seleccion = raw_input('Haga su seleccion: ')

        if(seleccion=='1'):
            datos = pedir_datos_persona()
            club.alta_socio(datos[0],datos[1],datos[2],datos[3],datos[4])
            seleccion = '-1'
        if(seleccion=='2'):
            DNI = raw_input('Editar datos del socio: ')
            while not club.validarDNI(DNI):
                print '\033[91m'+'El DNI no tiene un formato correcto.'+'\033[0m'
                DNI =raw_input('DNI: ')
            socio = club.obtener_socio(DNI)
            if (socio != -1):
                print 'Introduzca nuevos valores: '
                print socio
                nombre = raw_input('Nombre: '+str(socio.nombre))
                apellidos = raw_input('Apellidos: '+str(socio.apellidos))
                movil = raw_input('Movil: '+str(socio.movil))
                while not club.validarTelefono(movil):
                    print '\033[91m'+'El telefono no tiene un formato correcto. Deben ser 9 digitos'+'\033[0m'
                    movil = raw_input('Movil: '+str(socio.movil))
                correo = raw_input('Correo electronico: '+str(socio.correo))
                while not club.validarEmail(correo):
                    print '\033[91m'+'El email no es correcto.'+'\033[0m'
                    correo = raw_input('Correo electronico: '+str(socio.correo))
                club.editar_socio(DNI,nombre,apellidos,movil,correo)
            else:
                print '\033[91m'+'No existe ningun socio con ese DNI.'+'\033[0m'
            seleccion = '-1'
        if(seleccion=='3'):
            DNI = raw_input('Introduzca el DNI del usuario a dar de baja: ')
            while not club.validarDNI(DNI):
                print '\033[91m'+'El DNI no tiene un formato correcto.'+'\033[0m'
            socio = club.dar_baja_socio(DNI)
            if (socio == -1):
                print '\033[91m'+'No existe ningun socio con ese DNI.'+'\033[0m'
            seleccion = '-1'
        if(seleccion=='4'):
            DNI = raw_input('Introduzca el DNI del usuario a consultar: ')
            while not club.validarDNI(DNI):
                print '\033[91m'+'El DNI no tiene un formato correcto.'+'\033[0m'
            socio = club.obtener_socio(DNI)
            if (socio != -1):
                print socio
            else:
                print '\033[91m'+'No existe ningun socio con ese DNI.'+'\033[0m'
            seleccion = '-1'


    if (seleccion=='2'):
        print 'Haga su seleccion: '
        print '1. Crear reserva'
        print '2. Cancelar reserva'
        print '3. Consultar reservas'
        seleccion = raw_input('Haga su seleccion: ')
        if (seleccion=='1'):
            reserva = pedir_reserva()
        if(seleccion=='2'):
            DNI = raw_input('DNI del socio que desea reservar: ')
            while not club.validarDNI(DNI):
                print '\033[91m'+'El DNI no tiene un formato correcto.'+'\033[0m'
                DNI =raw_input('DNI: ')
            fecha = raw_input('Fecha y hora para la reserva (dd/mm/aa HH): ')
            while not club.validarFecha(fecha):
                print '\033[91m'+'La fecha no tiene un formato correcto.'+'\033[0m'
                fecha = raw_input('Fecha y hora para la reserva (dd/mm/aa HH): ')
            if(club.cancelar_reserva(DNI, fecha)):
                print "La reserva ha sido cancelada"
            else:
                print "No existia ninguna reserva para esa fecha"
        if (seleccion=='3'):
            reserva = consultar_reserva()
            if (reserva != -1):
                print reserva
            else:
                print "No existe una reserva para esa fecha"


    if (seleccion=='3'):
        print 'Haga su seleccion: '
        print '1. Crear alquiler'
        print '2. Devolver alquiler'
        print '3. Consultar alquiler'
        seleccion = raw_input('Haga su seleccion: ')
        if (seleccion=='1'):
            reserva = consultar_reserva()
            if (reserva != -1):
                inst = '-1'
                ids = []
                while(inst!= '0'):
                    if (inst != '-1'):
                        ids.append(inst)
                    print 'Introduzca el id de la instalacion a alquilar o 0 para salir.'
                    inst = raw_input('Instalacion: ')
                    while not club.validarInstalacion(inst) and inst != '0':
                        print '\033[91m'+'La instalacion no existe.'+'\033[0m'
                        inst = raw_input('Introduzca el id de la instalacion a alquilar o 0 para salir: ')
                club.crear_alquiler(reserva,ids)
            else:
                print "No existe una reserva para esa fecha"
        if (seleccion=='2'):
            reserva = consultar_reserva()
            if (reserva != -1):
                club.devolver_alquiler(reserva)
        if (seleccion=='3'):
            reserva = consultar_reserva()
            alquiler = club.consultar_alquiler(reserva)
            if (alquiler != -1):
                print alquiler
            else:
                print "No existe una alquiler para esa fecha"


    if(seleccion=='4'):
        print 'Haga su seleccion: '
        print '1. Crear profesor'
        print '2. Editar profesor'
        print '3. Dar profesor de baja'
        print '4. Consultar profesor'
        seleccion = raw_input('Haga su seleccion: ')
        if(seleccion=='1'):
            datos = pedir_datos_persona()
            salario = raw_input('Salario en euros: ')
            jornada = raw_input('Tipo de jornada: ')
            club.alta_profesor(datos[0],datos[1],datos[2],datos[3],datos[4],salario,jornada)
        if(seleccion=='2'):
            DNI = raw_input('DNI del profesor: ')
            while not club.validarDNI(DNI):
                print '\033[91m'+'El DNI no tiene un formato correcto.'+'\033[0m'
                DNI =raw_input('DNI: ')
            profesor = club.obtener_profesor(DNI)
            print 'Introduzca nuevos valores: '
            print profesor
            nombre = raw_input('Nombre: ')
            apellidos = raw_input('Apellidos: ')
            movil = raw_input('Movil: ')
            while not club.validarTelefono(movil):
                print '\033[91m'+'El telefono no tiene un formato correcto. Deben ser 9 digitos'+'\033[0m'
                movil = raw_input('Movil: ')
            correo = raw_input('Correo electronico: ')
            while not club.validarEmail(correo):
                print '\033[91m'+'El email no es correcto.'+'\033[0m'
                correo = raw_input('Correo electronico: ')
            sueldo = raw_input('Sueldo: ')
            jornada = raw_input('Jornada: ')
            club.editar_profesor(DNI,nombre,apellidos,movil,correo, sueldo, jornada)
        if(seleccion=='3'):
            DNI = raw_input('Introduzca el DNI del profesor a dar de baja: ')
            while not club.validarDNI(DNI):
                print '\033[91m'+'El DNI no tiene un formato correcto.'+'\033[0m'
                DNI =raw_input('DNI: ')
            club.dar_baja_profesor(DNI)
        if(seleccion=='4'):
            DNI = raw_input('Introduzca el DNI del profesor a consultar: ')
            while not club.validarDNI(DNI):
                print '\033[91m'+'El DNI no tiene un formato correcto.'+'\033[0m'
                DNI =raw_input('DNI: ')
            profesor = club.obtener_profesor(DNI)
            if profesor != -1:
                print profesor
            else:
                print 'No existe dicho profesor.'

    if(seleccion == '5'):
        print 'Haga su seleccion: '
        print '1. Registrar Clase'
        print '2. Cancelar clase'
        print '3. Consultar informacion clase'
        seleccion = raw_input('Haga su seleccion: ')
        if(seleccion == '1'):
            reserva = pedir_reserva()
            dni_profesor = raw_input('Introduzca DNI profesor: ')
            while not club.validarDNI(dni_profesor):
                print '\033[91m'+'El DNI no tiene un formato correcto.'+'\033[0m'
                dni_profesor =raw_input('Introduzca DNI profesor: ')
            profesor = club.obtener_profesor(dni_profesor)
            club.registrar_clase(profesor, reserva)
        if(seleccion == '2'):
            DNI = raw_input('Introduzca el DNI del profesor que da la clase:')
            while not club.validarDNI(DNI):
                print '\033[91m'+'El DNI no tiene un formato correcto.'+'\033[0m'
                DNI =raw_input('DNI: ')
            fecha = raw_input('Fecha y hora para la clase (dd/mm/aa HH): ')
            while not club.validarFecha(fecha):
                print '\033[91m'+'La fecha no tiene un formato correcto.'+'\033[0m'
                fecha = raw_input('Fecha y hora para la clase (dd/mm/aa HH): ')
            club.cancelar_clase(DNI,fecha)
        if(seleccion == '3'):
            DNI = raw_input('Introduzca el DNI del profesor que da la clase:')
            while not club.validarDNI(DNI):
                print '\033[91m'+'El DNI no tiene un formato correcto.'+'\033[0m'
                DNI =raw_input('DNI: ')
            fecha = raw_input('Fecha y hora para la clase (dd/mm/aa HH): ')
            while not club.validarFecha(fecha):
                print '\033[91m'+'La fecha no tiene un formato correcto.'+'\033[0m'
                fecha = raw_input('Fecha y hora para la clase (dd/mm/aa HH): ')
            clase = club.obtener_clase(DNI,fecha)
            if clase != -1:
                print clase
            else:
                print 'No existe clase dicha clase.'

    if(seleccion == '6'):
        print 'Haga su seleccion: '
        print '1. Crear Torneo.'
        print '2. Introducir resultado.'
        print '3. Borrar torneo.'
        print '4. Consultar torneo.'
        seleccion = raw_input('Haga su seleccion: ')
        if (seleccion == '1'):
            nombre = raw_input('Introduzca el nombre del torneo: ')
            i = 0
            socios = []
            while i<8:
                DNI = raw_input('Introduzca el DNI del participante: ')
                while not club.validarDNI(DNI):
                    print '\033[91m'+'El DNI no tiene un formato correcto.'+'\033[0m'
                    DNI =raw_input('DNI: ')
                socio = club.obtener_socio(DNI)
                if (socio != -1):
                    socios.append(socio)
                    i+=1
                else:
                    print 'No existe socio para ese DNI.'
            fecha = raw_input('Introduzca una fecha para empezar el torneo: ')
            while not club.validarFecha(fecha):
                print '\033[91m'+'La fecha no tiene un formato correcto.'+'\033[0m'
                fecha = raw_input('Fecha y hora para la clase (dd/mm/aa HH): ')
            club.crear_torneo(nombre, socios, fecha)

        if seleccion == '2':
            nombre = raw_input('Introduzca el nombre del torneo: ')
            partido = raw_input('Introduzca el partido del torneo: ')
            resultado = raw_input('Introduzca el resultado del partido: ')
            club.introducir_resultado(nombre,partido,resultado)

        if seleccion == '3':
            nombre = raw_input('Introduzca el nombre del torneo: ')
            torneo = club.borrar_torneo(nombre)
            if torneo ==-1:
               print 'No existe un toreno con ese nombre.'

        if seleccion == '4':
            nombre = raw_input('Introduzca el nombre del torneo: ')
            torneo = club.consultar_torneo(nombre)
            if torneo !=-1:
                print torneo
            else:
                print 'No existe un toreno con ese nombre.'
