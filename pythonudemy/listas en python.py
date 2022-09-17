# listas en python 
nombres =  ['juan','karla','ricardo','maria']
print(nombres)
for i in nombres:
	print(i)

print(nombres[0:2])
print(nombres[1:3]) #siendo el ultimo digito 3  excluyente
print(nombres[:])
print(nombres[1:])
print(nombres[:3])

nombres[3] = 'checo'
print(nombres[3]) 

for nombre in nombres:
	print(nombre)

else: 
	print('--no mas nombres--')


#largo de la lista ?
print(len(nombres))
#agregar elementos a la lista 
nombres.append('jareth')
print(nombres)
print(len(nombres))
#insertar un elemento en un indice en especifico
nombres.insert(3,'otto')
print(nombres)
#quitar un valor 
nombres.remove('ricardo')
print(nombres)
#remover el ultimo elemento mediante funcion pop
nombres.pop()
print(nombres)
#eliminar un elemento de un indice indicado
del nombres[2]
print(nombres)
#limpiar todos los elementos de la lista 
nombres.clear()
print(nombres)

#borrar por completo la lista 
del nombres
print(nombres)
	