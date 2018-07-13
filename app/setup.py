import psycopg2
conn = psycopg2.connect("dbname=rut_199018795 user=postgres password=alumno")


cur = conn.cursor()
sql ="""DROP SCHEMA public CASCADE;
CREATE SCHEMA public;"""

cur.execute(sql)
sql ="""
CREATE TABLE usuarios
           (id serial PRIMARY KEY, nombre varchar(20), contrasena varchar(25), correo text not null unique, direccion varchar, creado timestamp DEFAULT NOW());
"""
cur.execute(sql)


sql ="""
CREATE TABLE estados
           (id_pedido integer PRIMARY KEY, estado varchar(15));
"""


cur.execute(sql)
sql ="""
CREATE TABLE productos
           (codigo integer PRIMARY KEY, nombre varchar, tipo varchar(10), precio integer, descuento integer, descripcion varchar);
"""


cur.execute(sql)

sql ="""
CREATE TABLE pedidos
           (id serial PRIMARY KEY, id_usuario integer, monto integer, cod_producto integer, cantidad integer, talla varchar(3));
"""


cur.execute(sql)
sql ="""
CREATE TABLE inventario
           (id_prod integer, talla varchar(2), cantidad integer);
"""


cur.execute(sql)
sql ="""
CREATE TABLE productos_pedidos
           (productos_codigo integer, pedidos_id integer);
"""


cur.execute(sql)


sql ="""
CREATE TABLE categorias
           (id serial PRIMARY KEY, nombre varchar(40), creado timestamp);

"""
cur.execute(sql)

sql ="""
CREATE TABLE categorias_productos 
           (categoria_id integer, producto_id integer);
"""


cur.execute(sql)

conn.commit()
cur.close()
conn.close()
