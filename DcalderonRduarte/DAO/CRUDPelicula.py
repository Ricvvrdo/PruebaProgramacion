from DAO.Conexion import Conexion
from DTO.Pelicula import Pelicula

host='localhost'
user='root'
password=''
db='bd_peliculas'

def ingresar(p): 
    try:
        con = Conexion(host,user,password,db)
        sql = "insert into pelicula set titulo_pelicula='{}', duracion={}, fecha_de_estreno='{}', "\
              "genero={}, idioma={}, director='{}'".format(
                p.titulo, p.duracion, p.fecha_estreno, p.genero, p.idioma, p.director)
        con.ejecuta_query(sql)
        con.commit()
        input("\n\nPelicula ingresada con exito :)\nPresione Enter para continuar")
        con.desconectar()
    except Exception as e:
        print("\nError en ingresar pelicula: {}".format(e))

def modificar(p): 
    try:
        con = Conexion(host, user, password, db)
        sql = "update pelicula set titulo_pelicula='{}', duracion={}, fecha_de_estreno='{}', "\
              "genero={}, idioma={}, director='{}' where id_pelicula={}".format(
                p[1], p[2], p[3], p[4], p[5], p[6], p[0])
        con.ejecuta_query(sql)
        con.commit()
        input("\n\nPelicula modificada con exito :)\nPresione Enter para continuar")
        con.desconectar()
    except Exception as e:
        print("\nError al modificar la pelicula: {}".format(e))

def eliminar(id_pelicula):
    try:
        con = Conexion(host, user, password, db)
        sql = "delete from pelicula where id_pelicula={}".format(id_pelicula)
        con.ejecuta_query(sql)
        con.commit()
        input("\n\nPelicula eliminada con exito :)\nPresione Enter para continuar")
        con.desconectar()
    except Exception as e:
        print("\nError al eliminar la pelicula: {}".format(e))


def mostrarTodos():
    try:
        con = Conexion(host, user, password, db)
        sql = "select * from pelicula"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as e:
        print("\nError al mostrar todas las peliculas: {}".format(e))
        return None

def mostrarParcial(cantidad):
    try:
        con = Conexion(host,user,password,db)
        sql = "select * from pelicula"
        cursor = con.ejecuta_query(sql)
        datos = cursor.fetchmany(size=cantidad)
        con.desconectar()
        return datos
    except Exception as e:
        print("\nError al mostrar parcialmente las películas: {}".format(e))
        return None

def mostrarParticular(id_pelicula):
    try:
        con = Conexion(host,user,password,db)
        sql = "select * from pelicula where id_pelicula={}".format(id_pelicula)
        cursor = con.ejecuta_query(sql)
        dato = cursor.fetchone()
        con.desconectar()
        return dato
    except Exception as e:
        print("\nError al mostrar la pelicula solicitada: {}".format(e))
        return None
