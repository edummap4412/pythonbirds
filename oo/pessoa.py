class Pessoa:
    def __init__(self, nome=None,idade=35):
        self.idade = idade
        self.nome = nome
    def cumprimentar(self):
        return f'Olá'


if __name__ == '__main__':
    p = Pessoa('Eduardo')
    print(p.cumprimentar())
    print(p.nome)
    p.nome ='Renzo'
    print(p.nome)
    print(p.cumprimentar())
    print(p.nome)
    print(p.idade)

