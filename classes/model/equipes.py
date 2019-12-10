class Equipes:

    # método para setar o projeto
    def set_projeto(self, projeto):
        self.projeto = projeto

    # método para retornar o projeto
    def get_projeto(self):
        return self.projeto
    
    def set_squad(self, squad):
        self.squad = squad
    
    def get_squad(self):
        return self.set_squad

equipe = Equipes()
equipe.set_squad(4)
