from rh.classes.Departamento import Departamento

from datetime import date, timedelta
dt1 = date.today() - timedelta(days=4)
hoje = date.today()

departamento = Departamento('Departamento XYZ')
departamento.add_colaborador('José da Silva', True, hoje.day, hoje.month, 1990)
departamento.add_colaborador('João Oliveira', False, hoje.day, hoje.month, 1992)
departamento.add_colaborador('Pedro Mendonça', False, dt1.day, dt1.month, 1993)
departamento.add_colaborador('Luis Fernando', False, hoje.day, hoje.month, 2000)
departamento.add_colaborador('Maurício Souza', False, dt1.day, dt1.month, 1985)

aniversariantes = departamento.verificar_aniversariantes()

for aniversariante in aniversariantes:
    print(aniversariante)