miVariable  = "hola desde python "
x = 2
y = 3
z= x+y 
game_over = False


for i in range(0,10):
	if i == z and i > y:
		print("\n")
	elif i == z or i == x:
		print("*")

	print(miVariable)

print(z,x,y)
print(" \n direcciones de memoria \n")
print(id(miVariable))# esta es la direccion de memoria 
print(id(z))
print(id(x))
print(id(y))


coment = "loa tipos de datos en python son entero float char string bool "
print(coment)

print(type(x))
print(type(coment))
print(type(game_over))