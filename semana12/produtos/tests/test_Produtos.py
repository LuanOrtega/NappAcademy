from produtos.classes.Produtos import Produto
from produtos.classes.Produtos import CocaCola
from produtos.classes.Produtos import Pepsi
from produtos.classes.Produtos import Dolly
from produtos.classes.Produtos import GuaranaAntartica
from produtos.classes.Caracteristicas import Tamanho600ml
import pytest


class TestColaborador:
    def test_class_Pepsi(self):
        msg = 'Pepsi tamanho: 600ml.'
        objeto = Pepsi(Tamanho600ml())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, Pepsi)
        assert objeto.operation() == msg
    
    def test_class_Pepsi(self):
        msg = 'Pepsi tamanho: 1 Litro.'
        objeto = Pepsi(Tamanho1litro())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, Pepsi)
        assert objeto.operation() == msg
    
    def test_class_Pepsi(self):
        msg = 'Pepsi tamanho: 2 Litros.'
        objeto = Pepsi(Tamanho2litros())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, Pepsi)
        assert objeto.operation() == msg
    
    def test_class_Pepsi(self):
        msg = 'Pepsi tamanho: 3 Litros.'
        objeto = Pepsi(Tamanho3litros())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, Pepsi)
        assert objeto.operation() == msg

    def test_class_CocaCola(self):
        msg = 'CocaCola tamanho: 600ml.'
        objeto = CocaCola(Tamanho600ml())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, CocaCola)
        assert objeto.operation() == msg
    
    def test_class_CocaCola(self):
        msg = 'CocaCola tamanho: 1 Litro.'
        objeto = CocaCola(Tamanho1litro())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, CocaCola)
        assert objeto.operation() == msg
    
    def test_class_CocaCola(self):
        msg = 'CocaCola tamanho: 2 Litros.'
        objeto = CocaCola(Tamanho2litros())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, CocaCola)
        assert objeto.operation() == msg
    
    def test_class_CocaCola(self):
        msg = 'CocaCola tamanho: 3 Litros.'
        objeto = CocaCola(Tamanho3litros())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, CocaCola)
        assert objeto.operation() == msg
    
    def test_class_Dolly(self):
        msg = 'Dolly tamanho: 600ml.'
        objeto = Dolly(Tamanho600ml())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, Dolly)
        assert objeto.operation() == msg
    
    def test_class_Dolly(self):
        msg = 'Dolly tamanho: 1 Litro.'
        objeto = CocaCola(Tamanho1litro())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, Dolly)
        assert objeto.operation() == msg
    
    def test_class_Dolly(self):
        msg = 'Dolly tamanho: 2 Litros.'
        objeto = CocaCola(Tamanho2litros())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, Dolly)
        assert objeto.operation() == msg
    
    def test_class_Dolly(self):
        msg = 'Dolly tamanho: 3 Litros.'
        objeto = CocaCola(Tamanho3litros())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, Dolly)
        assert objeto.operation() == msg
    
    
    def test_class_Dolly(self):
        msg = 'Dolly tamanho: 600ml.'
        objeto = Dolly(Tamanho600ml())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, Dolly)
        assert objeto.operation() == msg
    
    def test_class_Dolly(self):
        msg = 'Dolly tamanho: 1 Litro.'
        objeto = CocaCola(Tamanho1litro())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, Dolly)
        assert objeto.operation() == msg
    
    def test_class_Dolly(self):
        msg = 'Dolly tamanho: 2 Litros.'
        objeto = CocaCola(Tamanho2litros())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, Dolly)
        assert objeto.operation() == msg
    
    def test_class_Dolly(self):
        msg = 'Dolly tamanho: 3 Litros.'
        objeto = CocaCola(Tamanho3litros())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, Dolly)
        assert objeto.operation() == msg
    
    
    def test_class_GuaranaAntartica(self):
        msg = 'Guarana Antartica tamanho: 600ml.'
        objeto = GuaranaAntartica(Tamanho600ml())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, GuaranaAntartica)
        assert objeto.operation() == msg
    
    def test_class_GuaranaAntartica(self):
        msg = 'Guarana Antartica tamanho: 1 Litro.'
        objeto = GuaranaAntartica(Tamanho1litro())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, GuaranaAntartica)
        assert objeto.operation() == msg
    
    def test_class_GuaranaAntartica(self):
        msg = 'Guarana Antartica tamanho: 2 Litros.'
        objeto = GuaranaAntartica(Tamanho2litros())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, GuaranaAntartica)
        assert objeto.operation() == msg
    
    def test_class_GuaranaAntartica(self):
        msg = 'Guarana Antartica tamanho: 3 Litros.'
        objeto = GuaranaAntartica(Tamanho3litros())
        assert isinstance(objeto, Produto)
        assert isinstance(objeto, GuaranaAntartica)
        assert objeto.operation() == msg


    def test_class_abstractClass(self):
        msg_erro = "Can't instantiate abstract class Produto "
        msg_erro = msg_erro + "with abstract methods operation"
        with pytest.raises(TypeError) as error:
            Produto()
        assert str(error.value) == msg_erro
