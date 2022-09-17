#un diccionario es similar a un objeto
#clase diccionario 


producto = {
	"nombre":"libro",
	"cantidad":1,
	"precio":100

}

persona={
	"first_name":"ryan",
	"second_name":"garcia",
}

x=type(producto)

print(x)

#print(dir(producto))

print(persona.keys())#------esto solo imprime el valor de las llaves
print(persona.items())#------esto imprime el valor del complemento

#del persona------------esto elimina el diccionario de persona
#print(persona) 

persona.clear()#-------esto vacia el diccionario
print(persona)

productos=[#se pone corchete cuadrado pra hacer diccionarios de conjuntos 
	{"name":"book","precio":10},
	{"name":"patineta","precio":500}
]

print(productos)

