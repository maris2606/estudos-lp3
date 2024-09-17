# POO em python segue as mesmas ideias
# "paradigma de programação que usa objetos - instancias de classe - pra modelar dados e comportamento"

class Cachorro:
    def __init__(self, nome, idade): # self é tipo o this
        # init é construtor
        self.nome = nome
        self.idade = idade

    def latir(self):
        print(f'{self.nome} está latindo - AUAU')

# modificadores de acesso
# getter e setter - ter acesso as coisas dos privados - esse nome é boa prática 
# get tem retorno e set tem parametro - no mínimo

# prefixos __ (dois underline private) 
 
  
# heranca sempre vem de alguem

class Pomeranian (Cachorro):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca

    def latir(self):
        print(f'{self.nome} está latindo - auau')
# polimorfismo
