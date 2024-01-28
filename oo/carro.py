"""
Classe (Carro) com atributos de outras classes(Motor, Direção)
motor:
1 atributo - velocidade
2 método - acelerar
3 método - frear

direção:
1 valor direção - norte, sul, leste, oeste
2 método - girar esquerda
3 método - girar direita

"""
class Motor:
    def __init__(self):
        self.velocidade=0

    def acelerar(self):
        self.velocidade += 1
