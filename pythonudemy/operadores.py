n_uno = int(input('ingrese un valor entero: '))
num_uno = int(input("presion uno:"))
num_dos = int(input("presion dos:"))
g = 9.81
vel = 15
densi = int(input("ingrese la densidad: "))
 

if n_uno % 2 ==0:
	print(f"{n_uno} es par")
else:
	print(f'{n_uno} es non')


suma = num_uno + num_dos
resta = num_dos -num_uno
print("Resultado suma: ",suma)
print(f'La presion total es : {suma} kpa')
print(f'La diferencia de presiones es: {resta} Kpa')
sg = densi * g
e_fluido = num_uno/sg
e_cinetica = (vel**2)/(2*g) 
print(f'el peso especifico: {sg}')
print(f'la energia interna del fluido: {e_fluido} kj')
print(f'la energia cinetica del fluido: {e_cinetica} kj')
e_cinetica_tot = e_cinetica//1
print(f'energia cineica redondeada {e_cinetica_tot}')
