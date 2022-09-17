#excepciones en python
from NumerosIdenticosException import NumerosIdenticosException

resultado = None
resultado_dos = None
#a = 10
#b = 0
#c = 20
try:   #forzamos un error de codigo

    a = int(input('ingrese el valor de a: '))
    b = int(input('ingrese el valor de b: '))
    c = int(input('ingrese el valor de c: '))
    if a == b:
        #raise se utiliza para arrojar cualquier tipo de eleccion 
        raise NumerosIdenticosException('numeros identicos (clase NumerosIdenticosException)')
    print('\n')

    resultado = a/c
    resutltado_dos = c/b

 #se rePcomienda capturar excepciones con clases mas genericas
 #siempre poner la clase de mayor gerarquia al final
 #except permite continuar a pesar de la existencia de errores

except ZeroDivisionError as e:
     #except Exception as e:
    print(f'ZeroDivisionError - Ocurrio un error {e}')
except TypeError as te:
    print(f'TypeError - ocurrio un error {te}')
except Exception as e:
    print(f'Exception ocurrio un errror: {e}')

#este bloque es opcional
else:
    print('sin excepciones')
#el bloque finally siempre se ejecuta con excepciones o sin ellos
finally:
    print('ejecucion del bloque finally')
print('\n')

print(f'Resultado {resultado}')
print('Continuamos...')
