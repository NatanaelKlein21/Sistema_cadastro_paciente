from abc import ABC, abstractmethod

# Criação da classe Pessoa
class Pessoa(ABC):
    def __init__(self, nome, idade, genero):
        self.nome = nome
        self.idade = idade
        self.genero = genero

# Alteração da classe Paciente
class Paciente(Pessoa):
    def __init__(self, nome, idade, genero):
        super().__init__(nome, idade, genero)
        self.registros = []

    def adicionar_registro(self, registro):
        self.registros.append(registro)

    def listar_registros(self):
        for registro in self.registros:
            print(registro)

# classe RegistroMedico se manteve
class RegistroMedico:
    def __init__(self, data, sintomas, diagnostico, prescricao):
        self.data = data
        self.sintomas = sintomas
        self.diagnostico = diagnostico
        self.prescricao = prescricao

    def __str__(self):
        return f"Data: {self.data}\nSintomas: {self.sintomas}\nDiagnóstico: {self.diagnostico}\nPrescrição: {self.prescricao}"

# Classe PessoaFactory criada 
class PessoaFactory(ABC):
    def criar_pessoa(self):
        pass

# Classe PacienteFactory criada
class PacienteFactory(PessoaFactory):
    def criar_pessoa(self, nome, idade, genero):
        return Paciente(nome, idade, genero)

# Classe RegistroMedicoFactory
class RegistroMedicoFactory:
    def criar_registro_medico(self, data, sintomas, diagnostico, prescricao):
        return RegistroMedico(data, sintomas, diagnostico, prescricao)


def menu_principal():
    print("----- Sistema Médico -----")
    print("1. Cadastrar Paciente")
    print("2. Adicionar Registro Médico")
    print("3. Listar Registros de um Paciente")
    print("0. Sair")
    print("---------------------------")

# Cadastrar novos pacientes
def cadastrar_paciente():
    nome = input("Nome do Paciente: ")
    idade = input("Idade: ")
    genero = input("Gênero: ")
    paciente = Paciente(nome, idade, genero)
    pacientes.append(paciente)
    print("Paciente cadastrado com sucesso!")

# Adicionar novos registros medicos 
def adicionar_registro_medico():
    nome = input("Nome do Paciente: ")
    encontrado = False
    for paciente in pacientes:
        if paciente.nome == nome:
            data = input("Data do Registro Médico: ")
            sintomas = input("Sintomas: ")
            diagnostico = input("Diagnóstico: ")
            prescricao = input("Prescrição: ")
            registro = RegistroMedico(data, sintomas, diagnostico, prescricao)
            paciente.adicionar_registro(registro)
            encontrado = True
            print("Registro Médico adicionado com sucesso!")
            break
    if not encontrado:
        print("Paciente não encontrado.")

# Listar os registros médicos
def listar_registros_medicos():
    nome = input("Nome do Paciente: ")
    encontrado = False
    for paciente in pacientes:
        if paciente.nome == nome:
            print(f"----- Registros Médicos de {paciente.nome} -----")
            paciente.listar_registros()
            print("-----------------------------------------------")
            encontrado = True
            break
    if not encontrado:
        print("Paciente não encontrado.")

# Alteração nos parametros com base nas novas classes criadas
pacientes = []
pessoa_factory = PacienteFactory()
registro_factory = RegistroMedicoFactory()

# Escolha de entrada
while True:
    menu_principal()
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        cadastrar_paciente(pessoa_factory)
    elif opcao == "2":
        adicionar_registro_medico(registro_factory)
    elif opcao == "3":
        listar_registros_medicos()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")
