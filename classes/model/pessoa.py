# Classe Pessoa que será usada para herança das outras classes
class Pessoa:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade
    
    # método para retornar nome
    def get_nome(self):
        return self.nome

    # método para retornar o cpf
    def get_cpf(self):
        return self.cpf
     
    # método para retornar idade
    def get_idade(self):
        return self.idade




