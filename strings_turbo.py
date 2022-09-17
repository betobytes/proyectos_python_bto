my_cadena = "hola mundo car  "

print(my_cadena.upper())
print(my_cadena.lower())
print(my_cadena.swapcase())
print(my_cadena.capitalize())
print(my_cadena.replace('hola','bye'))
print(my_cadena.count(' '))

print(my_cadena.startswith('bye'))
print(my_cadena.endswith("world"))

print(my_cadena.split())
print(my_cadena.split('o'))

print(my_cadena.find(' '))
print(my_cadena.find('d'))
	
print(len(my_cadena))
print(my_cadena.index('o'))

print(my_cadena.isnumeric())
print(my_cadena.isalpha())

print(my_cadena[7])
print(my_cadena[0])

mi_cadena_dos = "beto"

print("mi nombre es "+ mi_cadena_dos)
print(f"mi nombre es {mi_cadena_dos}")
print("mi nombre es {0}".format(mi_cadena_dos))