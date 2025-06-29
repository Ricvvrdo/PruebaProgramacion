from DAO.Conexion import Conexion
from DTO.Pelicula import Pelicula

host ='localhost'
user ='root'
password =''
db ='bd_peliculas'

def ingresar(p):
    try:
        con=Conexion(host,user,password,db)
        sql="insert into pelicula set titulo_pelicula='{}', duracion={}, fecha_de_estreno='{}', genero={}, idioma={}, director='{}'".format(p.titulo, p.duracion, p.fecha_estreno, p.genero, p.idioma, p.director)
        con.ejecuta_query(sql)
        con.commit()
        input("\n\nPelicula ingresada con exito :)\nPresione Enter para continuar")
        con.desconectar()
    except Exception as e:
        print("\nError en ingresar: {}".format(e))

def eliminar(id_pelicula):
    try:
        con=Conexion(host,user,password,db)
        sql="delete from pelicula where id_pelicula={}".format(id_pelicula)
        con.ejecuta_query(sql)
        con.commit()
        input("\n\nPelicula eliminada con exito\nPresione Enter para continuar")
        con.desconectar()
    except Exception as e:
        print("\nError en Eliminar: {}".format(e))

def modificar(p):
    try:
        con=Conexion(host,user,password,db)
        sql="update pelicula set titulo_pelicula='{}', duracion={}, fecha_de_estreno='{}', genero={}, idioma={}, director='{}' where id_pelicula={}".format(p[1], p[2], p[3], p[4], p[5], p[6], p[0])
        con.ejecuta_query(sql)
        con.commit()
        input("\n\nPelicula modificada con exito\nPresione Enter para continuar")
        con.desconectar()
    except Exception as e:
        print("\nERROR en Modificar: {}".format(e))

def mostrarTodos():
    try:
        con=Conexion(host,user,password,db)
        sql="select * from pelicula"
        cursor=con.ejecuta_query(sql)
        datos=cursor.fetchall()
        con.desconectar()
        return datos
    except Exception as e:
        print("\nError en mostrar todos: {}".format(e))
        return None

def mostrarParcial(cantidad):
    try:
        con=Conexion(host,user,password,db)
        sql="select * from pelicula"
        cursor=con.ejecuta_query(sql)
        datos=cursor.fetchmany(size=cantidad)
        con.desconectar()
        return datos
    except Exception as e:
        print("\nError en mostrar parcial: {}".format(e))
        return None

def mostrarParticular(id_pelicula):
    try:
        con=Conexion(host, user, password, db)
        sql="select * from pelicula where id_pelicula={}".format(id_pelicula)
        cursor=con.ejecuta_query(sql)
        dato=cursor.fetchone()
        con.desconectar()
        return dato
    except Exception as e:
        print("\nError en mostrar particular: {}".format(e))
        return None