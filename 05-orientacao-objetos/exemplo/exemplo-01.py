class Pessoa:
    def __init__(self, nome, prontuario, idade):
        self.__nome = nome
        self.__prontuario = prontuario
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome


    @nome.setter
    def nome(self, nome):
        self.__nome = nome
    @property
    def prontuario(self):
        return self.__prontuario

    @property
    def idade(self):
        return self.__idade
    

    @prontuario.setter
    def prontuario(self, prontuario):
        self.__prontuario = prontuario

    @idade.setter
    def idade(self, idade):
        self.__idade = idade
