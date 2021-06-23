import os
import glob

def palavra_no_arquivo(palavra, arquivo, case_sensitive):
    with open(arquivo, 'r') as f:
        for line in f:
            if case_sensitive:
                return palavra in line
            else:
                return palavra.lower() in line.lower()
    return False

def todos_arquivos(extensao):
    # looking_for = '**/*.txt'
    looking_for = os.path.dirname(__file__) + '\\**/*.' + extensao
    matched = glob.glob(looking_for, recursive=True)
    return matched

def encontrar_palavra(palavra, case_sensitive, extensao):
    encontrado_em = []
    arquivos = todos_arquivos(extensao)
    for arquivo in arquivos:
        if palavra_no_arquivo(palavra, arquivo, case_sensitive):
            encontrado_em.append(arquivo)
    return encontrado_em


# Busca em arquivo TXT--------------------------------------------------
busca_napp1 = encontrar_palavra(palavra='napp', case_sensitive=True, extensao='txt') # Com case sensitive
print('\nBusca em arquivo TXT')
if len(busca_napp1) > 0:
    print(f'Foram encontrados: {len(busca_napp1)} registros.\nOcorrência encontrada nos arquivos:')
    for arquivo in busca_napp1:
        print(arquivo)
    print('\n')
else:
    print('Nenhuma ocorrência encontrada.\n')


busca_napp2 = encontrar_palavra(palavra='napp', case_sensitive=False, extensao='txt')# Sem case sensitive
if len(busca_napp2) > 0:
    print(f'Foram encontrados: {len(busca_napp2)} registros.\nOcorrência encontrada nos arquivos:')
    for arquivo in busca_napp2:
        print(arquivo)
    print('\n')
else:
    print('Nenhuma ocorrência encontrada.\n')

print('=-' * 60)


# Busca em arquivo CSV--------------------------------------------------
busca_napp4 = encontrar_palavra(palavra='napp', case_sensitive=True, extensao='csv') # Com case sensitive
print('\nBusca em arquivo CSV')
if len(busca_napp4) > 0:
    print(f'Foram encontrados: {len(busca_napp4)} registros.\nOcorrência encontrada nos arquivos:')
    for arquivo in busca_napp4:
        print(arquivo)
    print('\n')
else:
    print('Nenhuma ocorrência encontrada.\n')


busca_napp4 = encontrar_palavra(palavra='napp', case_sensitive=False, extensao='csv')# Sem case sensitive
if len(busca_napp4) > 0:
    print(f'Foram encontrados: {len(busca_napp4)} registros.\nOcorrência encontrada nos arquivos:')
    for arquivo in busca_napp4:
        print(arquivo)
else:
    print('Nenhuma ocorrência encontrada.')

print('=-' * 60)

