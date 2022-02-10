from edu.utilidades.cargador import Cargador

from edu.cableado.api import IModerador,IEntrada, ISalida,IRegla

import tkinter as tk

class Orquestador(IModerador):    
    
    def __init__(self,ruta):
        self.ruta = ruta   
        
    def moderar_componentes(self):
        crg = Cargador(self.ruta,['back','front'])
        
        try:
            entr:IEntrada = crg._from_(IEntrada.__module__)._import_(IEntrada.__name__)()
            entr.recibir_informacion()
            
            salid:ISalida = crg._from_(ISalida.__module__)._import_(ISalida.__name__)() 
            salid.desplegar_informacion()
        except Exception as e1:
            master = tk.Tk()       
            tk.Message(master, text="no hay GUI").pack()
            tk.mainloop() 
        
        try:
            core :IRegla = crg._from_(IRegla.__module__)._import_(IRegla.__name__)() 
            core.verificar_reglas()
        except Exception as e2:
            master = tk.Tk()       
            tk.Message(master, text="no hay Core").pack()
            tk.mainloop()        

   