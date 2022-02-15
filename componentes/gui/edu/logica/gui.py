from edu.cableado.api import IEntrada,ISalida

import tkinter as tk

class GUI(IEntrada,ISalida):
    def __init__(self):
        self.iv = InformeVentas()
        self.inv = Inventario()
        self.pr = Producto()
        self.cr = Carrito()
    
    def recibir_informacion(self):
        self.inv.recibir_informacion()
        self.cr.recibir_informacion()
        # master = tk.Tk()       
        # tk.Message(master, text="recibiendo informacion").pack()
        # tk.mainloop()  
        
   
    def desplegar_informacion(self):
        self.iv.desplegar_informacion()
        self.inv.desplegar_informacion()
        self.pr.desplegar_informacion()
        self.cr.desplegar_informacion()
        # master = tk.Tk()       
        # tk.Message(master, text="desplegando informacion").pack()
        # tk.mainloop()  
        
class Home(IEntrada, ISalida):
    def recibir_informacion(self):
        master = tk.Tk()       
        tk.Message(master, text="recibiendo inicio del aplicativo").pack()
        tk.mainloop()  

    def desplegar_informacion(self):
        master = tk.Tk()       
        tk.Message(master, text="desplegando pagina de inicio").pack()
        tk.mainloop()  

class Informacion_empresa(ISalida):
    def desplegar_informacion(self):
        master = tk.Tk()       
        tk.Message(master, text="desplegando informacion de la empresa").pack()
        tk.mainloop()  

class Administracion(IEntrada, ISalida):
    def recibir_informacion(self):
        master = tk.Tk()       
        tk.Message(master, text="recibiendo orden de gestion").pack()
        tk.mainloop()  

    def desplegar_informacion(self):
        master = tk.Tk()       
        tk.Message(master, text="desplegando solucion a la orden").pack()
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

class InformeUsuarios(ISalida):
    def desplegar_informacion(self):
        master = tk.Tk()       
        tk.Message(master, text="desplegando informacion de usuarios").pack()
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

    def desplegar_informacion(self):
        master = tk.Tk()       
        tk.Message(master, text="Pagando").pack()
        tk.mainloop()