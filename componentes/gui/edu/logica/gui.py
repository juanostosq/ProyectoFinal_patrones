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