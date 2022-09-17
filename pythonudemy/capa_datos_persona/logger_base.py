import logging as log

#log.basicConfig(level = log.WARNING)
log.basicConfig(level  = log.DEBUG,
                format = '%(asctime)s: %(levelname)s [%(filename)s : %(lineno)s] %(message)s',
                datefmt = '%I:%M:%S %p',
                handlers = [
                            log.FileHandler('capa_datos.log'),
                            log.StreamHandler()
                           ]
                )


if __name__ =='__main__':
    log.debug(' mensaje a nivel debug')
    log.info(' mensaje a nivel info ')
    log.warning(' mensaje a nivel warning ')
    log.error(' mensaje a nivel critico')
    log.critical(' mensaje a nivel error')












"""#manejo de loggin
import logging as log

#log.basicConfig(level = log.DEBUG) segun la jerariqui del loggin el modo debug es el mas basico
                                 #y no se recomienda por que brinda demasiada informacion del script

#log.basicConfig(level = log.ERROR)#---conesta linea activa mostrara solo lo que este despues de su jerarquia

log.basicConfig( level = log.DEBUG, format = '%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s', datefmt = '%I:%M:%S %p', handlers = [log.FileHandler('capa_datos.log'),log.StreamHandler()] )

if __name__ == '__main__':

    log.debug('mensaje a nivel de debug')
    log.info('mensaje a nivel de info')
    log.warning('mensaje a nivel de warning')
    log.error('mensajea a nivel de error')
    log.critical('mensaje a nivel critico')



#manejo de loggin
import logging as log

log.basicConfig(level = log.DEBUG,
                format = '%(asctime)s : %(levelname)s [%(filename)s : %(lineno)s] %(messages)s',
                datefmt = '%I:%M:%S %p',
                handlers = [log.FileHandler('capa_datos.log'),log.StreamHandler()] )

if __name__ == '__main__':
    log.debug('mensaje a nivel debug')
    log.info('mensaje a nivel info')
    log.warning('mensase a nivel warning')
    log.error('mensaje a nivel error')
    log.critical('mensaje a nivel critico')

"""
