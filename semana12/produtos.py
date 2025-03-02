from produtos.classes.Produtos import CocaCola, Pepsi, Dolly, GuaranaAntartica
from produtos.classes.Caracteristicas import Tamanho600ml, Tamanho1litro, Tamanho2litros, Tamanho3litros


def client_code(produto):
    print(produto.operation())


if __name__ == "__main__":
    #Chamada Coca Cola
    print('Chamada Coca Cola')
    tamanho = Tamanho600ml()
    produto = CocaCola(tamanho)
    client_code(produto)

    tamanho = Tamanho1litro()
    produto = CocaCola(tamanho)
    client_code(produto)

    tamanho = Tamanho2litros()
    produto = CocaCola(tamanho)
    client_code(produto)

    tamanho = Tamanho3litros()
    produto = CocaCola(tamanho)
    client_code(produto)

    print('=-' * 40)

    #Chamada Pepsi
    print('Chamada Pepsi')
    tamanho = Tamanho600ml()
    produto = Pepsi(tamanho)
    client_code(produto)

    tamanho = Tamanho1litro()
    produto = Pepsi(tamanho)
    client_code(produto)

    tamanho = Tamanho2litros()
    produto = Pepsi(tamanho)
    client_code(produto)

    tamanho = Tamanho3litros()
    produto = Pepsi(tamanho)
    client_code(produto)
    
    print('=-' * 40)

    #Chamada Dolly 
    print('Chamada Dolly')
    tamanho = Tamanho600ml()
    produto = Dolly(tamanho)
    client_code(produto)

    tamanho = Tamanho1litro()
    produto = Dolly(tamanho)
    client_code(produto)

    tamanho = Tamanho2litros()
    produto = Dolly(tamanho)
    client_code(produto)

    tamanho = Tamanho3litros()
    produto = Dolly(tamanho)
    client_code(produto)
    
    print('=-' * 40)

    #Chamada Guarana Antartica
    print('Chamada Guarana Antartica')
    tamanho = Tamanho600ml()
    produto = GuaranaAntartica(tamanho)
    client_code(produto)

    tamanho = Tamanho1litro()
    produto = GuaranaAntartica(tamanho)
    client_code(produto)

    tamanho = Tamanho2litros()
    produto = GuaranaAntartica(tamanho)
    client_code(produto)

    tamanho = Tamanho3litros()
    produto = GuaranaAntartica(tamanho)
    client_code(produto)

