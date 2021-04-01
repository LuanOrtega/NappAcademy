from datetime import date


class Colaborador:
    def __init__(self, nome, responsavel, dia=None, mes=None, ano=None):
        self._nome = nome
        try:
            self._aniversario = date(ano, mes, dia)
        except TypeError:
            raise TypeError('Informe dia, mês e ano')
        self._responsavel = responsavel


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, value):
        self._nome = value

    @property
    def aniversario(self):
        return self._aniversario.isoformat()

    def aniversario_hoje(self):
        hoje = date.today()
        if self._aniversario.day == hoje.day:
            if self._aniversario.month == hoje.month:
                return True
        return False

    @property
    def responsavel(self):
        return self._responsavel
    
    @responsavel.setter
    def responsavel(self, value):
        if self._responsavel == True:
            value = True
        else:
            value = False

    def __str__(self):
        return self._nome

    def __repr__(self):
        return 'Colaborador: ' + self._nome