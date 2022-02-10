from edu.cableado.api import IRegla

import tkinter as tk

class Nucleo(IRegla):
    def verificar_reglas(self):        
        master = tk.Tk()       
        tk.Message(master, text="verificar reglas").pack()
        tk.mainloop()                