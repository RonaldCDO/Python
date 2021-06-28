class Produto:

    def __init__(self, nome='0', preco=0.00):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    def get_nome(self):
        print(self.nome)
        return self.nome

    def set_nome(self, valor):
        self.nome = valor
        return self.nome

    def get_preco(self):
        print(f'O produto custa R${self.preco}')
        return self.preco

    def set_preco(self, valor):
        self.preco = valor


