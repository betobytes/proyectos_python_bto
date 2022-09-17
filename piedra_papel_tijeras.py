#juego de piedra papel o tijeras
import random

tijeras = '''
    _______
---´   ____)____
          ______)
       __________)
      (_____)
---.__(___)
'''

piedra = '''
    _______
---´   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---´   ____)____
          ______)
          _______)
         ______)
---._______)
'''

eleccion_usuario = None
while eleccion_usuario != 3:
    try:
        print('juguemos piedra papel o tijeras'.center(50,'-'))
        print('\noprime 0 para tijeras')
        print('oprime 1 para piedra')
        print('oprime 2 para papel')
        print('oprime 3 para salir\n')
        eleccion_usuario = int(input('seleccion: '))
        print('\n')

        eleccion_pc = random.randint(0,2)
        elecciones = [tijeras, piedra, papel]

        print(f'tu elejiste:\n {elecciones[eleccion_usuario]}')
        print(f'la pc elijio:\n {elecciones[eleccion_pc]}')

        if elecciones [int(eleccion_usuario-1)] == elecciones[eleccion_pc]:
            print('ganaste\n')
        elif elecciones[int(eleccion_usuario)] == elecciones[eleccion_pc]:
            print('empate\n')
        else:
            print('perdiste\n')

    except Exception as e:
        if eleccion_usuario == 3:
            print('adios usuario'.center(50,'-'))
        else:
            print(f'se genero un error {e}\n')
