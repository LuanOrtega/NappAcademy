from integrador.classes.Abstracao import Abstracao


def carregar_credenciais(arquivo):
    credenciais = {}
    try:
        with open(arquivo) as file:
            for line in file:
                if not line.startswith('#'):
                    if not line.startswith('\n'):
                        key, valor = line.split('==>')
                        valor = valor.replace('\n', '')
                        credenciais[key] = valor
    except FileNotFoundError:
        raise FileNotFoundError('Arquivo não encontrado: ' + arquivo)
    return credenciais


if __name__ == "__main__":
    arquivos = []
    arquivos += ['credenciais1.txt', 'credenciais2.txt']
    arquivos += ['credenciais3.txt', 'credenciais4.txt']

    for arquivo in arquivos:
        credenciais = carregar_credenciais(arquivo)
        context = Abstracao(**credenciais)
        dados = context.extrair_dados()
        dados_relatorio = context.relatorio_simples()
        print(f'Relatório arquivo: {arquivo}\n{dados_relatorio}\n')
        context.criar_relatorio()
        print(160 * '*')
    
#------------------------------------------------------------------------------------------
#Respostas:
#Desafio 3:
    # Não refatoraria o código, pois a classe “cliente” está importando a “Abstração” onde a mesma importa a classe “Extrair”.

#Desafio 5:
    #No script Extrair.py teria que criar uma classe chamada ERP3 com parâmetro ExtrairDados;
    # Uma função para se conecta ao MySQL no qual diferente do SQLite, ele não é um arquivo, mas um serviço que precisa de conexão;
    # As funções get_query, get_query_report e execute assim como está nesse código de exemplo, com isso pegaria os dados do banco de dados, e os dados necessários nas credências:
    # Nome do ERP
        # erp==>ERP3
    # Conexão do banco de dados
        # host='localhost'
        # database='cliente
        # user='root'
        # password='123'
    # Formato do relatório.
        # relatorio==>csv
    # Nome do arquivo: erp3.csv
        # relatorio_nome==>erp3
#------------------------------------------------------------------------------------------