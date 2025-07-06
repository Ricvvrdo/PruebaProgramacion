import os
from DTO.Pelicula import Pelicula
import DAO.CRUDPelicula

def menuPrincipal():
    os.system('cls')
    print("================================")
    print("        MENU PRINCIPAL")
    print("================================")
    print(      "1.- (C) Ingresar")
    print(      "2.- (R) Mostrar")
    print(      "3.- (U) Actualizar")
    print(      "4.- (D) Eliminar")
    print(      "5.- (E) Salir")
    print("================================")

def menuMostrar():
    os.system('cls')
    print("================================")
    print("        MENU MOSTRAR")
    print("================================")
    print(      "1.- Mostrar Todo")
    print(      "2.- Mostrar Uno")
    print(      "3.- Mostrar Parcial")
    print(      "4.- Volver")
    print("================================")

def ingresarPelicula():
    os.system('cls')
    print("==================================")
    print("    Ingresar datos de pelicula ")
    print("==================================")
    titulo=input("Ingrese titulo: ")
    duracion=int(input("Ingrese duracion (ej: 120(Referente a minutos)): "))
    fecha=input("Ingrese fecha estreno (AAAA-MM-DD): ")
    print("---------------------------------------")
    print("1. Terror")
    print("2. Ciencia Ficción")
    print("3. Drama")
    print("---------------------------------------")
    genero=int(input("Seleccione Genero: "))
    print("---------------------------------------")
    print("1. Español")
    print("2. Inglés")
    print("3. Portugués")
    print("---------------------------------------")
    idioma=int(input("Seleccione idioma: "))
    director=input("Ingrese director: ")
    
    p=Pelicula(None,titulo,duracion,fecha,genero,idioma,director)
    DAO.CRUDPelicula.ingresar(p)
    input("Presione enter para continuar......")


def mostrar():
    while True:
        menuMostrar()
        op2=int(input("Ingrese una Opcción: "))
        if op2==1:
            mostrarTodos()
            input("Presione enter para continuar......")
        elif op2==2:
            mostrarUno()
        elif op2==3:
            mostrarParcial()
        if op2==4:
            break
        else:
            print("Opcion Ingresada esta fuera de rango ....")


def mostrarTodos():
    os.system('cls')
    print("============================")
    print(" Mostrar todas las Peliculas")
    print("============================")
    datos=DAO.CRUDPelicula.mostrarTodos()
    print("\tID\tTítulo\tDuración\tEstreno\tGénero\tIdioma\tDirector")
    for dato in datos:
        print("\t{}\t{}\t{}\t{}\t{}\t{}\t{}".format(dato[0],dato[1],dato[2],dato[3],dato[4],dato[5],dato[6]))


def mostrarParcial():
    os.system('cls')
    print("===================================")
    print(" Mostrar Parcialmente las Peliculas")
    print("======================================")
    cantidad=int(input("Ingrese Cantidad a Mostrar: "))
    datos=DAO.CRUDPelicula.mostrarParcial(cantidad)
    print("\tID\tTítulo\tDuración")
    for dato in datos:
        print("\t{}\t{}\t{}".format(dato[0],dato[1],dato[2]))


def mostrarUno():
    os.system('cls')
    print("=========================")
    print("  Mostrar una sola Pelicula ")
    print("==========================")
    id_pelicula=int(input("Ingrese EL ID Película a buscar: "))
    dato=DAO.CRUDPelicula.mostrarParticular(id_pelicula)

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
    input("Presione Enter para continuar......")

def modificarPelicula():
    nuevosDatos=[]
    os.system('cls')
    print("===============================")
    print("  Modificar una sola Pelicula ")
    print("===============================")
    mostrarTodos()
    op_mod=int(input("Ingrese el ID Película a modificar: "))
    dato=DAO.CRUDPelicula.mostrarParticular(op_mod)

    print("ID Película:{}".format(dato[0]))
    nuevosDatos.append(dato[0])
    print("Título:{}".format(dato[1]))
    nuevosDatos.append(dato[1])
    opm=input("Desea modificar la Duración: {} - [S/N] ".format(dato[2]))
    if opm.upper()=="S":
        duracionNueva=input("Ingrese la nueva duración: ")
        nuevosDatos.append(duracionNueva)
    else:
        nuevosDatos.append(dato[2])
    
    opm=input("Desea modificar la Fecha: {} - [S/N] ".format(dato[3]))
    if opm.upper()=="S":
        fechaNueva=input("Ingrese la nueva fecha: ")
        nuevosDatos.append(fechaNueva)
    else:
        nuevosDatos.append(dato[3])
    
    opm=input("Desea modificar el genero: {} - [S/N] ".format(dato[4]))
    if opm.upper()=="S":
        generoNuevo=input("Ingrese el Nuevo genero: ")
        nuevosDatos.append(generoNuevo)
    else:
        nuevosDatos.append(dato[4])
    
    opm=input("Desea modificar el idioma: {} - [S/N] ".format(dato[5]))
    if opm.upper()=="S":
        idiomaNuevo=input("Ingrese el nuevo idioma: ")
        nuevosDatos.append(idiomaNuevo)
    else:
        nuevosDatos.append(dato[5])
    
    opm=input("Desea modificar el director: {} - [S/N] ".format(dato[6]))
    if opm.upper()=="S":
        directorNuevo=input("Ingrese el nuevo director: ")
        nuevosDatos.append(directorNuevo)
    else:
        nuevosDatos.append(dato[6])

while(True):
    menuPrincipal()
    op=int(input("Ingrese una Opción: "))
    if op==1:
        ingresarPelicula()
    elif op==2:
        mostrar()
    elif op==3:
        modificarPelicula()
    if op==4:
        input("Eliminar")
    if op==5:
        op2=input("Desea Salir S[SI]/N[NO]: ".upper())
        if op2=="S":
            exit()
    else:
        print("Opción está fuera de Rango....")