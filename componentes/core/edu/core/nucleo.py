from edu.cableado.api import IRegla

import tkinter as tk

class Nucleo(IRegla):
    def verificar_reglas(self):        
        master = tk.Tk()       
        tk.Message(master, text="verificar reglas").pack()
        tk.mainloop()

class Producto(IRegla):
    def verificar_reglas(self):
        master = tk.Tk()
        tk.Message(master, text="Creando producto").pack()
        tk.Message(master, text="Eliminar producto").pack()
        tk.Message(master, text="Leyendo producto").pack()
        tk.Message(master, text="Actualizando producto").pack()
