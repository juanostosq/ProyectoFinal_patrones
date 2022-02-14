from edu.cableado.api import IEntrada,ISalida

import tkinter as tk

class GUI(IEntrada,ISalida):
    
    def recibir_informacion(self):
        master = tk.Tk()       
        tk.Message(master, text="recibiendo informacion").pack()
        tk.mainloop()  
        
   
    def desplegar_informacion(self):
        master = tk.Tk()       
        tk.Message(master, text="desplegando informacion").pack()
        tk.mainloop()  
        
class InformeVentas(ISalida):
    def desplegar_informacion(self):
        master = tk.Tk()       
        tk.Message(master, text="desplegando informacion de ventas").pack()
        tk.mainloop()
        
class Inventario(IEntrada, ISalida):
    def recibir_informacion(self):
        master = tk.Tk()       
        tk.Message(master, text="recibiendo informacion para la gestión de inventarios").pack()
        tk.mainloop()  
        
    def desplegar_informacion(self):
        master = tk.Tk()       
        tk.Message(master, text="desplegando informacion del inventario").pack()
        tk.mainloop()  

class Producto(ISalida):
    def desplegar_informacion(self):
        master = tk.Tk()       
        tk.Message(master, text="Buscando producto").pack()
        tk.Message(master, text="Mostrando producto").pack()
        tk.mainloop()  

class Carrito(IEntrada, ISalida):
    def recibir_informacion(self):
        master = tk.Tk()       
        tk.Message(master, text="Agregando producto").pack()
        tk.Message(master, text="Eliminando producto").pack()
        tk.mainloop()  

    def desplegar_informacion():
        master = tk.Tk()       
        tk.Message(master, text="Pagando").pack()
        tk.mainloop()