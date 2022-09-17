#uso de modulos y clases en python 
#para importar todas las clases se usa el comadno 
#from encapsulamiento en python inmpor *
from Persona import Person

print('creacion de objetos'.center(50,'-'))
persona1 = Person('karla','gomez',30)
persona1.mostrar()
print(__name__)

#destructor de objetos 
print('eliminacion de objetos'.center(50,'-'))
del persona1



