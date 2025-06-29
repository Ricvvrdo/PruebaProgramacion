import os
import DAO.CRUDPelicula

#Contruccion de menus

#Menu principal
def Principal():
        os.system('cls')
        print("================================")
        print("        MENU PRINCIPAL")
        print("================================")
        print("================================")
        print(      "1.- (C) Ingresar")
        print(      "2.- (R) Mostrar")
        print(      "3.- (U) Actualizar")
        print(      "4.- (D) Eliminar")
        print(      "5.- (E) Salir")
        print("================================")

#Menu Mostrar
def MostrarPeliculas():
        os.system('cls')
        print("================================")
        print("      PELICULAS DISPONIBLES     ")
        print("================================")
        print(      "1.- Mostrar todos")
        print(      "2.- Mostrar parcial")
        print(      "3.- Mostrar particular")
        print(      "4.- Volver")
        print("================================")

def menuMostrarPeliculas():
        while True:
                MostrarPeliculas()
                opcion = (input("Seleccione una opcion (1-4): "))

                if opcion == "1":
                        print("Aqui se mostraran todas las peliculas")
                elif opcion == "2":
                        print("Aqui se mostraran peliculas parcialmente")
                elif opcion == "3":
                        print("Aqui se mostrara alguna pelicula en particular")
                elif opcion == "4":
                        print("Volviendo al menu principal...")
                        break
                else:
                        print("Opcion inválida. Intentelo nuevamente")

#Menu ingresar
def IngresarPelicula():
        pass

#Menu eliminar
def EliminarPelicula():
        pass

#Menu modificar
def ModificarPelicula():
        pass
