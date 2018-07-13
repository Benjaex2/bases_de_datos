from app import app
from flask import Flask, flash, redirect, render_template, request, session, abort, request
import psycopg2
conn = psycopg2.connect("dbname=pruebas user=benjaex2 password=dragones")
cur = conn.cursor()

ID_iniciosesion = 0

@app.route('/')
@app.route('/index')
def index():
	sql ="""
	select id,nombre from categorias order by nombre
	"""
	print (sql) 
	cur.execute(sql)
	categorias  = cur.fetchall()
	sql ="""
	select codigo,nombre, precio, precio - descuento as preciodesc from productos where descuento not in (0)
	"""
	print (sql)
	cur.execute(sql)
	productos  = cur.fetchall()
	return render_template("index.html",categorias=categorias,productos=productos)


@app.route('/producto/<post_id>', methods=['GET', 'POST'])
def post(post_id):

	sql ="""
	select codigo,nombre,descripcion, precio, descuento, precio - descuento as preciodesc from productos where codigo = %s
	"""%post_id
	print (sql)
	cur.execute(sql)
	post  = cur.fetchone()

	sql ="""
	select id, nombre from categorias, categorias_productos where id=categoria_id and producto_id = %s 
	"""%(post_id)
	print (sql)
	cur.execute(sql)
	categorias  = cur.fetchall()

	sql ="""
	select talla from inventario where id_prod = %s and cantidad not in (0)
	"""%post_id
	print (sql)
	cur.execute(sql)
	tallas  = cur.fetchone()

	sql ="""
	select talla, cantidad from inventario where id_prod = %s
	"""%post_id
	print (sql)
	cur.execute(sql)
	stock  = cur.fetchone()

	return render_template("post.html",post= post,categorias=categorias, tallas=tallas, stock=stock) 


@app.route('/categoria/<post_id>', methods=['GET', 'POST'])
def categoria(post_id):
	sql ="""
	select id,nombre from categorias order by nombre
	"""
	print (sql) 
	cur.execute(sql)
	categorias  = cur.fetchall()

	sql ="""
	select codigo,productos.nombre, precio, precio - descuento as preciodesc from productos, categorias, categorias_productos where 
	categorias.id = %s and categorias.id = categorias_productos.categoria_id and categorias_productos.producto_id = productos.codigo
	"""%(post_id)
	print (sql)
	cur.execute(sql)
	productos  = cur.fetchall()

	return render_template("index.html",categorias=categorias,productos=productos)

@app.route('/poleras', methods=['GET', 'POST'])
def polera():
	sql ="""
	select id,nombre from categorias order by nombre
	"""
	print (sql) 
	cur.execute(sql)
	categorias  = cur.fetchall()

	sql ="""
	select codigo,productos.nombre, precio, precio - descuento as preciodesc from productos where tipo = 'polera'
	"""
	print (sql)
	cur.execute(sql)
	productos  = cur.fetchall()

	return render_template("index.html",categorias=categorias,productos=productos)

@app.route('/polerones', methods=['GET', 'POST'])
def poleron():
	sql ="""
	select id,nombre from categorias order by nombre
	"""
	print (sql) 
	cur.execute(sql)
	categorias  = cur.fetchall()

	sql ="""
	select codigo,productos.nombre, precio, precio - descuento as preciodesc from productos where tipo = 'poleron'
	"""
	print (sql)
	cur.execute(sql)
	productos  = cur.fetchall()

	return render_template("index.html",categorias=categorias,productos=productos)

@app.route('/compras/<post_id>', methods = ['GET', 'POST'])
def compras(post_id):

	talla = request.form['talla']

	sql = """
	select precio - descuento as preciofinal from productos where codigo = %s
	"""%(post_id)
	print(sql)
	cur.execute(sql)
	monto = cur.fetchall()
	monto = monto[0][0]

	sql = """
	insert into pedidos (id_usuario, monto, cod_producto, cantidad, talla) values (1, %s, %s, 1, '%s') returning id;
	"""%(monto, post_id, talla)
	cur.execute(sql)
	conn.commit()
	pedido_id = cur.fetchone()[0]

	sql = """
	insert into estados (id_pedido, estado) values (%s,'En carro')
	"""%(pedido_id)
	cur.execute(sql)
	conn.commit()

	redirect('/carro')

@app.route('/carro')
def carro():
	sql = """
	select exists(select id_pedido from pedidos, estados where id_usuario = 1 and id_pedido = pedidos.id and estado not in ('Finalizado') )
	"""
	cur.execute(sql)
	existe = cur.fetchall()

	if existe[0][0] == True:
		sql = """
		select estado from pedidos, estados where id_usuario = 1 and estado not in ('Finalizado') and pedidos.id = id_pedido
		"""
		cur.execute(sql)
		estado = cur.fetchall()

		if estado[0][0] == 'En carro':
			sql = """
			select id from pedidos, estados where id_usuario = 1 and estado not in ('Finalizado') and pedidos.id = id_pedido
			"""
			cur.execute(sql)
			id_pedidos = cur.fetchall()
			id_pedidos = id_pedidos[0][0]

			sql = """
			select pedidos.id, nombre, talla, cantidad, monto from pedidos, productos where pedidos.id = %s and and cod_producto = codigo
			"""%(id_pedidos)
			cur.execute(sql)
			post = cur.fetchall()

			return render_template('carro.html', post=post)
		if estado[0][0] == 'En entrega':

			sql = """
			select id from pedidos, estados where id_usuario = 1 and estado not in ('Finalizado') and pedidos.id = id_pedido
			"""
			cur.execute(sql)
			id_pedidos = cur.fetchall()
			id_pedidos = id_pedidos[0][0]

			sql = """
			select pedidos.id, estado, nombre, talla, cantidad, monto from pedidos, productos where pedidos.id = %s and cod_producto = codigo
			"""%(id_pedidos)
			cur.execute(sql)
			post = cur.fetchall()

			return render_template('carro.html', post=post)
	else:
		return render_template('carro_vacio.html')

@app.route('/borrar')
def borrar():
	pass
