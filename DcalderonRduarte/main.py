import os
from DTO.Pelicula import Pelicula
import DAO.CRUDPelicula

def menuPrincipal():
    os.system('cls')
    print("================================")
    print("        MENU PRINCIPAL")
    print("================================")
    print("1.- (C) Ingresar")
    print("2.- (R) Mostrar")
    print("3.- (U) Actualizar")
    print("4.- (D) Eliminar")
    print("5.- (E) Salir")
    print("================================")

def menuMostrar():
    os.system('cls')
    print("================================")
    print("        MENU MOSTRAR")
    print("================================")
    print("1.- Mostrar Todo")
    print("2.- Mostrar Uno")
    print("3.- Mostrar Parcial")
    print("4.- Volver")
    print("================================")

def ingresarPelicula():
    os.system('cls')
    print("==================================")
    print("    Ingresar datos de pelicula ")
    print("==================================")
    titulo = input("Ingrese titulo: ")
    
    while True:
        try:
            duracion = int(input("Ingrese duracion (ej: 120(Referente a minutos)): "))
            break
        except:
            print("Debe ingresar un numero entero")

    fecha = input("Ingrese fecha estreno (AAAA-MM-DD): ")
    
    # Validación de género
    while True:
        print("---------------------------------------")
        print("1. Terror")
        print("2. Ciencia Ficcion")
        print("3. Drama")
        print("---------------------------------------")
        try:
            genero = int(input("Seleccione Genero: "))
            if 1 <= genero <= 3:
                break
            else:
                print("Opcion no valida. Ingrese 1, 2 o 3")
        except:
            print("Debe ingresar un numero")

    # Validación de idioma
    while True:
        print("---------------------------------------")
        print("1. Español")
        print("2. Ingles")
        print("3. Portugues")
        print("---------------------------------------")
        try:
            idioma = int(input("Seleccione idioma: "))
            if 1 <= idioma <= 3:
                break
            else:
                print("Opcion no valida. Ingrese 1, 2 o 3")
        except:
            print("Debe ingresar un numero")

    director = input("Ingrese director: ")
    
    p = Pelicula(None, titulo, duracion, fecha, genero, idioma, director)
    DAO.CRUDPelicula.ingresar(p)
    input("Presione enter para continuar......")

def mostrar():
    while True:
        menuMostrar()
        op2 = input("Ingrese una Opccion: ")
        if op2 == "1":
            mostrarTodos()
            input("Presione enter para continuar......")
        elif op2 == "2":
            mostrarUno()
        elif op2 == "3":
            mostrarParcial()
        elif op2 == "4":
            break
        else:
            print("Opcion Ingresada esta fuera de rango ....")

def mostrarTodos():
    os.system('cls')
    print("============================")
    print(" Mostrar todas las Peliculas")
    print("============================")
    datos = DAO.CRUDPelicula.mostrarTodos()
    if datos:
        print("\tID\tTítulo\tDuración\tEstreno\tGénero\tIdioma\tDirector")
        for dato in datos:
            print("\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(dato[0],dato[1],dato[2],dato[3],dato[4],dato[5],dato[6]))
    else:
        print("No hay peliculas registradas")

def mostrarParcial():
    os.system('cls')
    print("===================================")
    print(" Mostrar Parcialmente las Peliculas")
    print("======================================")
    try:
        cantidad = int(input("Ingrese Cantidad a Mostrar: "))
        datos = DAO.CRUDPelicula.mostrarParcial(cantidad)
        if datos:
            print("\tID\tTítulo\tDuración")
            for dato in datos:
                print("\t{}\t{}\t{}".format(dato[0],dato[1],dato[2]))
        else:
            print("No hay peliculas para mostrar")
    except:
        print("Debe ingresar un numero valido")

def mostrarUno():
    os.system('cls')
    print("=========================")
    print("  Mostrar una sola Pelicula ")
    print("==========================")
    try:
        id_pelicula = int(input("Ingrese EL ID Película a buscar: "))
        dato = DAO.CRUDPelicula.mostrarParticular(id_pelicula)
        if dato:
            print("===============================")
            print("    Datos de la Pelicula")
            print("===============================")
            print("ID Película        :{}".format(dato[0]))
            print("Título             :{}".format(dato[1]))
            print("Duración           :{}".format(dato[2]))
            print("Fecha Estreno      :{}".format(dato[3]))
            print("Género             :{}".format(dato[4]))
            print("Idioma             :{}".format(dato[5]))
            print("Director           :{}".format(dato[6]))
        else:
            print("No se encontro la pelicula con ese ID")
    except:
        print("ID invalido")
    input("Presione Enter para continuar......")

def modificarPelicula():
    nuevosDatos=[]
    os.system('cls')
    print("****************************")
    print("  Modificar Una Película")
    print("****************************")
    
    # Validación de ID
    while True:
        try:
            mostrarTodos()
            op_mod=int(input("Ingrese el ID Película a modificar: "))
            dato=DAO.CRUDPelicula.mostrarParticular(op_mod)
            if dato:
                nuevosDatos.append(dato[0])
                break
            print("¡No existe película con ese ID!")
        except:
            print("¡Debe ingresar un número!")

    # Título
    print("Título:{}".format(dato[1]))
    while True:
        opm=input("Desea modificar el Título: {} - [S/N] ".format(dato[1])).upper()
        if opm in ['S','N']:
            if opm=="S":
                nuevosDatos.append(input("Nuevo título: "))
            else:
                nuevosDatos.append(dato[1])
            break
        print("¡Solo ingrese S o N!")

    # Duración
    print("Duración:{}".format(dato[2]))
    while True:
        opm=input("Desea modificar la Duración: {} - [S/N] ".format(dato[2])).upper()
        if opm in ['S','N']:
            if opm=="S":
                while True:
                    duracion=input("Nueva duración: ")
                    if duracion.isdigit():
                        nuevosDatos.append(int(duracion))
                        break
                    print("¡Debe ser número entero!")
            else:
                nuevosDatos.append(dato[2])
            break
        print("¡Solo ingrese S o N!")

    # Fecha Estreno
    print("Fecha Estreno:{}".format(dato[3]))
    while True:
        opm=input("Desea modificar la Fecha: {} - [S/N] ".format(dato[3])).upper()
        if opm in ['S','N']:
            if opm=="S":
                while True:
                    fecha=input("Nueva fecha (AAAA-MM-DD): ")
                    if len(fecha)==10 and fecha[4]=='-' and fecha[7]=='-':
                        nuevosDatos.append(fecha)
                        break
                    print("¡Formato debe ser AAAA-MM-DD!")
            else:
                nuevosDatos.append(dato[3])
            break
        print("¡Solo ingrese S o N!")

    # Género
    print("Género:{}".format(dato[4]))
    while True:
        opm=input("Desea modificar el Género: {} - [S/N] ".format(dato[4])).upper()
        if opm in ['S','N']:
            if opm=="S":
                while True:
                    print("1.Terror 2.Ciencia Ficción 3.Drama")
                    gen=input("Nuevo género (1-3): ")
                    if gen in ['1','2','3']:
                        nuevosDatos.append(int(gen))
                        break
                    print("¡Solo ingrese 1, 2 o 3!")
            else:
                nuevosDatos.append(dato[4])
            break
        print("¡Solo ingrese S o N!")

    # Idioma
    print("Idioma:{}".format(dato[5]))
    while True:
        opm=input("Desea modificar el Idioma: {} - [S/N] ".format(dato[5])).upper()
        if opm in ['S','N']:
            if opm=="S":
                while True:
                    print("1.Español 2.Inglés 3.Portugués")
                    idioma=input("Nuevo idioma (1-3): ")
                    if idioma in ['1','2','3']:
                        nuevosDatos.append(int(idioma))
                        break
                    print("¡Solo ingrese 1, 2 o 3!")
            else:
                nuevosDatos.append(dato[5])
            break
        print("¡Solo ingrese S o N!")

    # Director
    print("Director:{}".format(dato[6]))
    while True:
        opm=input("Desea modificar el Director: {} - [S/N] ".format(dato[6])).upper()
        if opm in ['S','N']:
            if opm=="S":
                nuevosDatos.append(input("Nuevo director: "))
            else:
                nuevosDatos.append(dato[6])
            break
        print("¡Solo ingrese S o N!")

    p=Pelicula(nuevosDatos[0],nuevosDatos[1],nuevosDatos[2],nuevosDatos[3],
              nuevosDatos[4],nuevosDatos[5],nuevosDatos[6])
    DAO.CRUDPelicula.modificar(p)
    input("Película modificada. Presione Enter...")
def eliminarPelicula():
    try:
        os.system('cls')
        print("================================")
        print("      ELIMINAR PELICULA")
        print("================================")
        mostrarTodos()
        id_pelicula = int(input("Ingrese ID de pelicula a eliminar: "))
        
        dato = DAO.CRUDPelicula.mostrarParticular(id_pelicula)
        if not dato:  # CORRECCIÓN: Cambiado para verificar correctamente
            print("\nNo existe pelicula con ese ID!")
            input("Presione Enter para continuar...")
            return
            
        print("\n--------------------------------")
        print("ID:", dato[0])
        print("Titulo:", dato[1])
        print("--------------------------------")
        confirmar = input("Confirmar eliminacion? S/N: ").upper()
        if confirmar == "S":
            DAO.CRUDPelicula.eliminar(id_pelicula)
            input("\nPelicula eliminada. Presione Enter...")
            
    except Exception as e:  # Mejor manejo de excepciones
        print(f"\nError al eliminar: {e}")
        input("Presione Enter para continuar...")

while True:
    menuPrincipal()
    op = input("Ingrese una Opción: ")
    
    if op == "1":
        ingresarPelicula()
    elif op == "2":
        mostrar()
    elif op == "3":
        modificarPelicula()
    elif op == "4":
        eliminarPelicula()
    elif op == "5":
        op2 = input("Desea salir S[SI]/N[NO]: ").upper()
        if op2 == "S":
            print("Saliendo del sistema...")
            break
    else:
        print("Opcion esta fuera de Rango....")
        input("Presione Enter para continuar...")