#un set no mantiene un orden ni permite mantener elementos duplicdos 
planetas = {'marte','venus','jupiter'}

print(planetas)

#logitud de el set 
print(len(planetas))

print('marte' in planetas)
planetas.add('tierra')
print(planetas)
planetas.add('tierra')
planetas.remove('tierra')
print(planetas)

planetas.discard('jupiter')
print(planetas)

#limpiar set 
planetas.clear()
print(planetas)

#eliminar el set 
del planetas
