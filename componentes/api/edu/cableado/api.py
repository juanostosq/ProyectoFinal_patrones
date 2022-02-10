from abc import ABC, abstractmethod
class IEntrada(ABC):
    @abstractmethod
    def recibir_informacion(self):
        pass
class ISalida(ABC):
    @abstractmethod
    def desplegar_informacion(self):
        pass
class IRegla(ABC):
    @abstractmethod
    def verificar_reglas(self):
        pass
class IModerador(ABC):
    @abstractmethod
    def moderar_componentes(self):
        pass       