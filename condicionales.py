x=30
#x=40
#x=10

#if x<30:
#if x>30:
if x==30:
	#print("x es menor que 30")
	#print("x es mayor que 30")
	print("x es igual 30")
else:
	print("x es mayor o menor que treinta")

x=10	
if x==30:
	print("x es igual 30")
else:
	print("x es mayor o menor que treinta")

color="red"

if color=='blue':
	print("el color es blue")
elif color=='yellow':
	print("color es yellow")
elif color=='black':
	print("color es black")
else:
	print("el color no esta dentro de los parametros")

#ejemplo usuario
user= 'beto'
las_name='muñoz'
password='tres'

if user == "beto":
	if las_name =='muñoz':
		if password == 'tres':
			print("bienvenido señor es un gusto tenerle de vuelta")
else:
	print("accseso denegado")

password='cuatro'

if user == "beto":
	if las_name =='muñoz':
		if password == 'tres':
			print("bienvenido señor es un gusto tenerle de vuelta")
		else:
			print("acceso denegado")
	else:
		print("accseso denegado")
else:
	print("accseso denegado")


y=3
if y>1 and y<=10:
	print("y es un numero entre 0 y 10")
if y<2 or y<4:
	print("el numero no es 2 ni 4")
if (not(x==y)):
	print("x es diferente de y")

