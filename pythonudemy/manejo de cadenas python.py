#concatenacion de cadenas 

cadena_uno = "muse"  
cadena_dos  = "supermasive black holes"
print("Este album reproduce la musica de " + cadena_uno)# conacatenacion 
print("dico " + cadena_dos + " " + cadena_uno)

print("\nreproduciendo musica de:", cadena_uno)
print("\nalbum:", cadena_dos, cadena_uno)
print("\n")

#cuando se realizan operaciones no usar comillas ya que estos los convierten en caracter y se 
# manejara como tal 

num_uno = "1"
num_dos = "2"

print("conacatenacion:", num_uno + num_dos)
print("suma", int(num_uno) + int(num_dos))#funcion int lee el str y lo convierte en un int
	
num_uno = 1
num_dos = 2

print(num_uno + num_dos) 

mi_variable = False
print(mi_variable)
mi_var = 4<5
print(mi_var)

if mi_variable:
	print("el resultado es verdadero")
elif mi_var:
	print("fue falso")