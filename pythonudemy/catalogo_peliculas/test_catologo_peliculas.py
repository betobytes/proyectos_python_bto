from Pelicula import Pelicula
from catalogo_pelicula import CatalogoPeliculas as cp
opcion = None

while opcion != 4:
    try:
        print(' OPCIONES: '.center(50,'-'))
        print(' 1. Agregar peliculas:')
        print(' 2. Lista de peliculas')
        print(' 3. Eliminar catalogo de peliculas')
        print(' 4. Salir \n ')
        opcion = int(input(' Escribe tu opcion entre 1-4: '))

        if opcion == 1:
            nombre_pelicula = input(' Proporciona el nombre de la pelicula: ')
            print('\n')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        elif opcion == 2:
            cp.listar_peliculas()
        elif opcion == 3:
            cp.eliminar_peliculas()

    except Exception as e :
        print(f'\nocuarrio un error {e} \n')
        print(' por favor selccione una opcion \n')
        print('\n')
        opcion = None

else:
    print('\n saliendo del programa...')
