class Equipes:

    # método para setar o projeto
    def __init__(self, squad, projeto):
        self.squad = squad
        self.projeto = projeto

    # método para retornar o projeto
    def get_projeto(self):
        return self.projeto
 
    def get_squad(self):
        return self.squad
