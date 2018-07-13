#!/usr/bin/env python
# -*- coding: utf-8 -*-
import psycopg2
conn = psycopg2.connect('dbname=rut_199018795 user=postgres password=alumno')
cur = conn.cursor()

sql ="""
insert into usuarios (nombre, contrasena, correo, direccion, creado) values 
('benjaex2', 'hola123', 'benjaex2@gmail.com', 'roberto espinoza 1996', now()),
('nicolito', 'hola321', 'nicolas_reyes@gmail.com', 'calle falsa 123', now());
"""
cur.execute(sql)

sql ="""
insert into productos (codigo, nombre, tipo, descripcion, precio, descuento) values
(1,'Polera Ant-Man', 'polera', 'Polera del superheroe de Marvel', 10000 , 2000),
(2,'Polera Deku','polera', 'Polera del personaje principal de Boku no Hero Academia',10000 , 0),
(3,'Polera Mr. Robot','polera', 'Polera de la popular serie de television',10000 , 0),
(4,'Polera Jon Snow','polera', 'Polera de la popular serie de television', 10000,2000),
(5,'Polera Heinsenberg','polera', 'Polera de el personaje principal de Breaking Bad', 10000, 0),
(6,'Polera Dr. Strange','polera', 'Polera del superheroe de Marvel',10000 ,1000),
(7,'Poleron Ant-Man','poleron', 'Poleron del superheroe de Marvel',22000 , 3500),
(8,'Poleron Deku','poleron', 'Poleron de el personaje principal de Boku no Hero academia',22000 , 0),
(9,'Poleron Mr. Robot','poleron', 'Poleron de la popular serie de television', 22000, 0),
(10,'Poleron Jon Snow','poleron', 'Poleron de la popular serie de television', 22000, 2000),
(11,'Poleron Heinsenberg','poleron', 'Poleron de el personaje principal de Breaking Bad', 22000, 0), 
(12,'Poleron Dr. Strange','poleron', 'Poleron del superheroe de Marvel', 22000, 3500);
"""
cur.execute(sql)

sql ="""
insert into pedidos (id_usuario, monto, cod_producto, cantidad, talla) values
(1, 20000, 2, 2, 'L'),
(2, 18500, 7, 1, 'XL');
"""
cur.execute(sql)


sql ="""
insert into estados (id_pedido, estado) values 
(1, 'En carro'),
(2, 'En proceso');
"""
cur.execute(sql)

sql ="""
insert into inventario (id_prod, talla, cantidad) values 
(1,'S',1),(1,'M',12),(1,'L',6),(1,'XL',12),
(2,'S',2),(2,'M',11),(2,'L',5),(2,'XL',11),
(3,'S',3),(3,'M',10),(3,'L',5),(3,'XL',10),
(4,'S',4),(4,'M',9),(4,'L',3),(4,'XL',9),
(5,'S',5),(5,'M',8),(5,'L',2),(5,'XL',8),
(6,'S',6),(6,'M',7),(6,'L',1),(6,'XL',7),
(7,'S',7),(7,'M',6),(7,'L',7),(7,'XL',1),
(8,'S',8),(8,'M',5),(8,'L',8),(8,'XL',2),
(9,'S',9),(9,'M',4),(9,'L',9),(9,'XL',3),
(10,'S',10),(10,'M',3),(10,'L',10),(10,'XL',4),
(11,'S',11),(11,'M',2),(11,'L',11),(11,'XL',5),
(12,'S',12),(12,'M',1),(12,'L',12),(12,'XL',6);
"""
cur.execute(sql)

sql ="""
insert into categorias (nombre, creado) values 
('Serie',now()),
('Marvel',now()),
('Anime',now()),
('Pelicula',now()),
('Television',now());
"""
cur.execute(sql)

sql ="""
insert into categorias_productos (categoria_id, producto_id) values 
(4,1),(2,1),
(1,2),(3,2),
(1,3),(5,3),
(1,4),(5,4),
(1,5),(5,5),
(4,6),(2,6),
(4,7),(2,7),
(1,8),(3,8),
(1,9),(5,9),
(1,10),(5,10),
(1,11),(5,11),
(4,12),(2,12);
"""
cur.execute(sql)


conn.commit()
