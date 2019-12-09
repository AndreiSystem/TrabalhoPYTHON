from pessoa import Pessoa

class Funcionario(Pessoa):
    
    # método para setar o salario:
    def set_salario(self, salario):
        self.salario = salario
    
    # método para retornar salario:
    def get_salario(self):
        return self.salario

    # método para setar a carga_horaria:
    def set_carga_horaria(self, carga_horaria):
        self.carga_horaria = carga_horaria

    # método para retornar a carga horaria:
    def get_carga_horaria(self):
        return self.carga_horaria

    # método para setar o cargo:
    def set_idade(self, cargo):
        self.cargo = cargo
        
    # método para retornar cargo:
    def get_cargo(self):
        return self.cargo