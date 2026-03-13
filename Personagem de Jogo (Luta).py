%%writefile personagem.py
import random

class PersonagemDoJogo:
    def __init__(self, nome, poder):
        self._nome = nome
        self.inventario = []
        self.vida = 100
        self.nivel = 1
        self.força = 10


        self.inimigo = {
            "nome": "Goblin",
            "vida": random.randint(50,150),
            "nivel": 1,
            "força": 10
        }

    @property
    def nome(self):
        return self._nome

    def receber_dano(self, dano):
        chance_defesa = random.randint(1, 100)

        if chance_defesa <= 30:
            dano = dano // 2
            print(f"{self.nome} conseguiu defender! Dano reduzido para {dano}.")

        self.vida -= dano
        print(f"{self.nome} recebeu {dano} de dano!")

        if self.inventario:
            item_perdido = self.inventario.pop()
            print(f"{self.nome} perdeu o item {item_perdido}")
        else:
            print("Sofreu apenas dano!")

        if self.vida <= 0:
            print(f"{self.nome} foi derrotado!")

    def atacar(self):

        if self.inimigo["força"] > self.força:
            print(f"{self.nome} percebeu que {self.inimigo['nome']} é muito forte!")
            print("Você não conseguirá derrotá-lo agora.")
            print("Tente usar um Elixir de Força!")
            return

        dano = self.força + self.nivel
        print(f"{self.nome} atacou {self.inimigo['nome']} causando {dano} de dano!")

        self.inimigo["vida"] -= dano
        print(f"{self.inimigo['nome']} recebeu {dano} de dano!")

        if self.inimigo["vida"] <= 0:
            print(f"{self.inimigo['nome']} foi derrotado!")

    def inimigo_atacar(self):
        dano = self.inimigo["força"] + self.inimigo["nivel"]
        print(f"{self.inimigo['nome']} atacou {self.nome} causando {dano} de dano!")
        self.receber_dano(dano)

    def subir_de_nivel(self):
        self.nivel += 1
        self.força += 5
        self.vida += 25
        self.inimigo["nivel"]
