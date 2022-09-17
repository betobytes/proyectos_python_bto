#TUPLAS() EN PYTHON 
frutas = ('naranja','platano','guayaba')#no se pueden agragar mas elementos de un tupla 

print(len(frutas))
print(frutas[0])
print(frutas[-1])
print(frutas[:])

for fruta in frutas:
	print(fruta, end=' ')

#para modificar los elementos de una tupla 
frutalist = list(frutas)
frutalist[0] = 'manazana'
frutas = tuple(frutalist)
print('\n ')
print(frutas)




