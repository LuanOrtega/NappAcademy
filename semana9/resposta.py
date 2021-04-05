from exercicio import juros_simples, soma_numeros, criar_json, situacao_escolar, vacina_ja, data_por_extenso, n_medias, calculo_media
import json
import pytest


class TestExercicio:

# Exercício 1
    def test_class_jurus_simples(self):
        with pytest.raises(TypeError) as error:
            juros_simples(0)
        assert error.value == 'Capital precisa ser maior que zero.'

    def test_class_jurus_simples2(self):
        with pytest.raises(TypeError) as error:
            juros_simples(1000, -0.1)
        assert error.value == 'Taxa precisa estar entre 0 e 1.'

    def test_class_jurus_simples3(self):
        with pytest.raises(TypeError) as error:
            juros_simples(1000, 1.1)
        assert error.value == 'Taxa precisa estar entre 0 e 1.'

    def test_class_jurus_simples4(self):
        with pytest.raises(TypeError) as error:
            juros_simples(1000, 0.1, 0)
        assert error.value == 'Período precisa ser maior que zero.'

    def test_class_jurus_simples5(self):
        objeto = juros_simples(1000, 0.1, 2)
        assert objeto == 1200

# Exercício 2
    def test_class_soma_numeros1(self):
        with pytest.raises(TypeError) as error:
            soma_numeros('string')
        assert str(error.value) == 'Incompatibilidade de tipos. Verificar parâmetros'

    def test_class_soma_numeros2(self):
        objeto = soma_numeros(10)
        assert objeto == 10

# Exercício 3
    def test_class_criar_json(self, **kwargs):
        objeto = criar_json()
        assert objeto == json.dumps(kwargs)

# Exercício 4
    def test_class_situacao_escolar1(self):
        with pytest.raises(TypeError) as error:
            situacao_escolar(10, -1)
        assert str(error.value) == 'Ausências entre 0 e 80'

    def test_class_situacao_escolar2(self):
        with pytest.raises(TypeError) as error:
            situacao_escolar(10, 81)
        assert str(error.value) == 'Ausências entre 0 e 80'

    def test_class_situacao_escolar3(self):
        with pytest.raises(TypeError) as error:
            situacao_escolar(-1, 50)
        assert str(error.value) == 'Nota Final entre 0 e 10'

    def test_class_situacao_escolar4(self):
        with pytest.raises(TypeError) as error:
            situacao_escolar(11, 50)
        assert str(error.value) == 'Nota Final entre 0 e 10'

    def test_class_situacao_escolar5(self):
        objeto = situacao_escolar(10, 50)
        assert objeto == 'Reprovado por falta'

    def test_class_situacao_escolar6(self):
        objeto = situacao_escolar(4, 10)
        assert objeto == 'Reprovado por nota'

    def test_class_situacao_escolar7(self):
        objeto = situacao_escolar(6, 10)
        assert objeto == 'Reprovado, em regime de recuperação'

    def test_class_situacao_escolar8(self):
        objeto = situacao_escolar(10, 10)
        assert objeto == 'Aprovado'

# Exercício 5
    def test_class_vacina_ja1(self, **kwargs):
        objeto = vacina_ja(70, kwargs='medico')
        assert objeto == 'Autorizado Vacinação'

    def test_class_vacina_ja2(self, **kwargs):
        objeto = vacina_ja(70, kwargs='professor')
        assert objeto == 'Autorizado Vacinação'

    def test_class_vacina_ja3(self, **kwargs):
        objeto = vacina_ja(30)
        assert objeto == 'Não autorizado por enquanto'

# Exercício 6
    def test_class_data_extenso(self, **kwargs):
        objeto = data_por_extenso('10/12/2021')
        assert objeto == '10 de dezembro de 2021'

    def test_class_data_extenso2(self):
        with pytest.raises(TypeError) as error:
            data_por_extenso('10/13/2012')
        assert str(error.value) == 'Mês inválido'

# Exercício 7
    def test_class_n_medias1(*notas, **kwnotas):
        notas = [10, 9, 8]
        objeto = n_medias(*notas)
        assert objeto == 9

    def test_class_n_medias2(*notas, **kwnotas):
        kwnotas = {'nota1':10, 'nota2':9, 'nota3':8}
        objeto = n_medias(**kwnotas)
        assert objeto == 9

# Exercício 8

    def test_class_calculo_media(self):
        objeto = calculo_media(10, 10, 10)

        assert objeto == 10

# Justificativa: Por estar sendo passado parametro na função, fica
# mais facil de aplicar os testes automáticos, assim como o return é importante
# para o assert