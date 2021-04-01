from rh.classes.Departamento import Departamento
from datetime import date, timedelta


class TestDepartamento:
    def test_class_declared(self):
        objeto = Departamento('Departamento XYZ')
        assert isinstance(objeto, Departamento)

    def test_instanciar(self):
        objeto = Departamento('Departamento XYZ')
        assert objeto.nome == 'Departamento XYZ'
        # assert objeto.responsavel is None

    def test_str_repr(self):
        objeto = Departamento('Departamento XYZ')
        assert str(objeto) == 'Departamento XYZ'
        assert repr(objeto) == 'Departamento = Departamento XYZ'

    def test_setters(self):
        objeto = Departamento('Curadoria')
        assert objeto.nome == 'Curadoria'
        objeto.nome = 'ETL'
        assert objeto.nome == 'ETL'

    def test_properties(self):
        objeto = Departamento('Departamento XYZ')
        assert objeto.nome == 'Departamento XYZ'

    def test_responsavel(self):
        departamento = Departamento('Departamento XYZ')
        assert departamento.responsavel is False
        departamento.add_colaborador('José da Silva', True, 1, 1, 1990)
        assert departamento.responsavel == True

    def test_responsavel_substituido(self):
        departamento = Departamento('Departamento XYZ')
        assert departamento.responsavel is False
        departamento.add_colaborador('José da Silva', True, 1, 1, 1990)
        assert departamento.responsavel == True
        departamento.add_colaborador('João Oliveira', True, 1, 1, 1990)
        assert departamento.responsavel == True

    def test_add_colaborador(self):
        departamento = Departamento('Departamento XYZ')
        departamento.add_colaborador('José da Silva', True, 1, 1, 1990)
        departamento.add_colaborador('João Oliveira', False, 28, 3, 1992)
        departamento.add_colaborador('Pedro Mendonça', False, 28, 4, 1993)
        assert len(departamento.colaboradores) == 3

    def test_verificar_aniversariantes(self):
        dt1 = date.today()
        hoje = date.today()
        retorno = [('José da Silva', '1990-03-28', 'Departamento XYZ', 'Reponsavel Pelo Setor'),
                   ('Luis Fernando', '2000-03-28', 'Departamento XYZ')]
        dt1 = date.today() - timedelta(days=4)
        hoje = date.today()
        depto = Departamento('Departamento XYZ')
        depto.add_colaborador('José da Silva', True, hoje.day, hoje.month, 1990)
        depto.add_colaborador('João Oliveira', False, dt1.day, dt1.month, 1992)
        depto.add_colaborador('Pedro Mendonça', False, dt1.day, dt1.month, 1993)
        depto.add_colaborador('Luis Fernando', False, hoje.day, hoje.month, 2000)
        depto.add_colaborador('Maurício Souza', False, dt1.day, dt1.month, 1085)
        aniversariantes = depto.verificar_aniversariantes()
        assert aniversariantes == retorno
        assert len(aniversariantes) == 2
        if depto.responsavel == True:
            assert len(aniversariantes[0]) == 4
        else:
            assert len(aniversariantes[0]) == 3
        assert type(aniversariantes[0]) == tuple
        assert type(aniversariantes) == 