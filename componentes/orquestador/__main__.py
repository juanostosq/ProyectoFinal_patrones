import sys
import os
from os.path import join

ruta = os.path.abspath(os.path.curdir)
#if not ruta.endswith('orquestador'):
#    ruta=os.path.dirname(os.path.abspath(__file__))
#print(ruta+"...")
rueda = join(join(ruta,'api'),'api.whl')
sys.path.append(rueda)

from edu.principal.orquestador import Orquestador

if __name__ == "__main__":  
   orq = Orquestador(ruta)
   orq.moderar_componentes()   