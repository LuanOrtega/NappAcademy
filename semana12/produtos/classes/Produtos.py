from abc import ABC, abstractmethod
from produtos.classes.Caracteristicas import Caracteristicas


class Produto(ABC):
    def __init__(self, implementation):
        try:
            if issubclass(type(implementation), Caracteristicas):
                self.implementation = implementation
        except Exception as e:
            print(f'Ocorreu uma exceção: {e}')

    @abstractmethod
    def operation(self):
        pass


class CocaCola(Produto):
    def operation(self):
        return (f"CocaCola tamanho:"
                f"{self.implementation.operation_implementation()}")


class Pepsi(Produto):
    def operation(self):
        return (f"Pepsi tamanho:"
                f"{self.implementation.operation_implementation()}")

class Dolly(Produto):
    def operation(self):
        return (f"Dolly tamanho:"
                f"{self.implementation.operation_implementation()}")

class GuaranaAntartica(Produto):
    def operation(self):
        return (f"Guarana Antartica tamanho:"
                f"{self.implementation.operation_implementation()}")