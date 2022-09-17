 

print("con que relacion de compresion desea trabajar: ", end="" )
rc = input()
print("ingrese la temperatura t1: ", end = "")
t1 = input() 
print("ingrese la presion p1: ", end = "")
p1 = input()
print("ingrese la energia u1: ", end= "" )
u1 = input()  
print("igrese la presion relativa pr1: ", end="")
pr1 = input()
print("igrese la presion relativa pr1: ", end="")
vr1 = input()

u2 = 0
u3 = 0
u4 = 0

efi_1 = 0 
efi_2 = 0
efi_3 = 0 
efi_4 = 0   




#volumen reltivo 
def vr(vr_ant,rc):
	vr_cal = vr_ant/rc

	return vr_cal


print(vr(621.2, 1))



# parte que interpola 

def interpolar(x0,x,x1,y0,y1):
	#x0 = 10
	#x = 11
	#x1 = 13

	#y0 = 250
	#y1 = 280


	y  = y0 + ((y1-y0)/(x1-x0))*(x-x0)


	return y 



print(interpolar(10,11,13,250,280)) 


#para el estador uno 
print('para el estado 1 ')

