from rh.classes.Colaborador import Colaborador


class Departamento:
    def __init__(self, nome_setor):
        self._nome_setor = nome_setor
        self._responsavel = False
        self._colaboradores = []

    @property
    def nome(self):
        return self._nome_setor

    @nome.setter
    def nome(self, value):
        self._nome_setor = value

    @property
    def responsavel(self):
        if self._responsavel is False:
            return False
        else:
            return True
        return str(self._responsavel)

    @property
    def colaboradores(self):
        return self._colaboradores

    # def informar_responsavel(self, nome, dia, mes, ano):
    #     self._responsavel = Colaborador(nome, dia, mes, ano)

    def add_colaborador(self, nome, responsavel, dia, mes, ano):
        self._colaboradores.append(Colaborador(nome, responsavel, dia, mes, ano))
        if responsavel == True:
            self._responsavel = Colaborador(nome, responsavel, dia, mes, ano)

    def verificar_aniversariantes(self):
        lista = []
        for colaborador in self.colaboradores:
            if colaborador.aniversario_hoje():
                if colaborador.responsavel == True:
                    lista.append((colaborador.nome, colaborador.aniversario, self._nome_setor, 'Reponsavel Pelo Setor'))
                else:
                    lista.append((colaborador.nome, colaborador.aniversario, self._nome_setor))
                
        return lista

    def __str__(self):
        return self._nome_setor

    def __repr__(self):
        return 'Departamento = ' + self._nome_setor