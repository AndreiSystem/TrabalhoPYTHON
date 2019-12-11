# Classe equipes para receber os dados da equipe (squad, projeto):
class Equipes:

    #--- Método para setar o projeto
    def __init__(self, squad, projeto):
        self.squad = squad
        self.projeto = projeto

    #--- Método para retornar o projeto
    def get_projeto(self):
        return self.projeto
 
    #--- Método para retornar o squad
    def get_squad(self):
        return self.squad
