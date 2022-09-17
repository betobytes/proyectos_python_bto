from tkinter import *
from time import strftime 

ventana = Tk()
ventana.title("reloj")
taman= 32
def time():
	
	string = strftime(" [ %H : %M : %S  %p ]")
	label.config(text = string)
	label.after(1000, time)

label  = Label(ventana, font=("ds-digital",taman), background= "black", foreground="cyan" )
label.pack(anchor = "center")
time()


mainloop()




