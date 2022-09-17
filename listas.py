
colors = ['red','green','blue']

number_list = list([1,2,3,4])
print(number_list)
print(type(number_list))

#r= list(range(1,2000))
#print(r)
#print(type(colors))
#print(colors[1])
#print('black' in colors )#regresa false o true dependiendo que se encuentre o no 
#print(colors)
#olors[1] = 'black'
#print(colors)

#print(dir(colors))

#colors.extend(['brown','yellow'])

#colors.append('black')
colors.insert(1,'black')
#colors.insert(-1,'yellow')
colors.insert(len(colors),'yellow')#agrega justo al ultimo 
#//print(colors)
#//colors.pop()#con este metodo s quita el ultimo valor agregado 
#/print(colors)

#//colors.pop()
#//colors.pop()..........el uso doble de pop borra 2 indices de la tabla

print(colors)

##--------------------##

#colors.remove('red')-----o se puede utilizar la posicion del inddice
colors.pop(0)#se hace mediante .pop(//pocision del directorio)
print(colors)

colors.sort(reverse=True)

print(colors.index('green'))
print(colors.count('black'))