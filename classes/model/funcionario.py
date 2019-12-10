from .pessoa import Pessoa
from .equipes import Equipes
from .linguagem import Linguagem

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, idade, salario, carga_horaria, cargo, linguagem_id:int, equipe_id:int, id=None):
        super().__init__(nome, cpf, idade)
        self.salario = salario
        self.carga_horaria = carga_horaria
        self.cargo = cargo
        self.linguagem_id = linguagem_id
        self.equipe_id = equipe_id
        self.id = id


    
    # método para retornar salario:
    def get_salario(self):
        return self.salario

    # método para retornar a carga horaria:
    def get_carga_horaria(self):
        return self.carga_horaria
        
    # método para retornar cargo:
    def get_cargo(self):
        return self.cargo

    # método para retornar linguagem:
    def get_linguagem(self):
        return self.linguagem_id
    # método para retornar equipe:
    def get_equipe(self):
        return self.equipe_id

    # método para retornar id:
    def get_id(self):
        return self.id


