from tkinter import *
from time import strftime

ventana = Tk()
ventana.title("reloj")
tamano = 32

def time():
	string = strftime(" [ %H : %M : %S  %p ]")
	label.config(text = string)
	label.after(1000, time)

label  = Label(ventana, font=("ds-digital", tamano), background= "limegreen", foreground="black" )
label.pack(anchor = "center")
time()

mainloop()
