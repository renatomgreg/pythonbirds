class Pessoa:
    def __init__(self, *filhos, nome, idade):
        self.idade=idade
        self.nome=nome
        self.filhos=list(filhos)

if __name__ == '__main__':
    riquelme=Pessoa(nome='Riquelme',idade=10)
    renato=Pessoa(riquelme,nome='Renato', idade= 35)

    print(renato.nome)
    print(renato.idade)
    for filho in renato.filhos:
        print(filho.nome)
