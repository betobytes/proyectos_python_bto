foods=['apples','chicharron','bread','cheese','milk','bananas']

# esto se puede hacer pero es tardado pero no sirve si la lista es dinamica
#print(foods[0])
#print(foods[1])
#print(foods[2])
#print(foods[3])

#print(dir(foods))

#---------------boocles mediante for----------------------

#for  food in foods:#por cada alimento en la lista de alimentos
#	if food == 'bread':
#		break
#	print(food)    # esto recorre cada elemento de la tabla 

#for food in foods:
#	if food=='cheese':
#		print("cheese-check")

#for food in foods:
#	if food == 'bread':
#		break
#	print("you need this")
#	print("")

#for food in foods:
#    if food  == 'chicharron ':
#    	continue
#    print(food)

for number in range(1,8):
	print(number)
print(" ")

for letra in 'humberto':
	print(letra)

#-----------contador----------------

contador = 4

while contador <= 10:
	print(contador)
	contador = contador + 1
	#if contador == 10:
	#	contador = contador-1