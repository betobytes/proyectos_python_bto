counter = 0
while counter < 3:
	print(counter)
	counter += 1
else: 
	print('fin del ciclo')

cadena = 'el molino de las quince letras'

for i in cadena:
	print(i)
	if i == 'q':
		print(f'se encontro l letra {i}')
		break




#for j in range(6):
#	if j % 2 == 0:
#
#		print(f'Vallor: {j}')

for j in range(6):
	if  j % 2 != 0:
		continue# salta el valor de j cuando j no es multiplo de 2 
	print(f'valor: {j}')
