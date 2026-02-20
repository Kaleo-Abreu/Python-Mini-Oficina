import random

class PersonagemDoJogo:
    def __init__(self, nome, poder):
        self._nome = nome
        self.inventario = []
        self.vida = 100
        self.nivel = 1
        self.força = 10
        
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

    def atacar(self, alvo):
        dano = self.força + self.nivel
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")
        alvo.receber_dano(dano)

    def subir_de_nivel(self):
        self.nivel += 1
        self.força += 5
        self.vida += 25
        print(f"{self.nome} subiu para o nível {self.nivel}!")

    def usar_item(self, item):
        if item in self.inventario:

            if item == "Poção da Vida":
                self.vida += 30
                print(f"{self.nome} tomou a Poção da Vida e ganhou +30 de vida!")

            elif item == "Elixir de Força":
                self.força += 15
                print(f"{self.nome} tomou o Elixir de Força e ganhou +15 de força!")

            self.inventario.remove(item)

        else:
            print("Item não encontrado no inventário.")

print("\n⚔️ BATALHA COMEÇOU ⚔️\n")

heroi = PersonagemDoJogo("Superman")
vilao = PersonagemDoJogo("Lex Luthor")

# Adicionando itens
heroi.inventario.append("Poção da Vida")
heroi.inventario.append("Elixir de Força")

vilao.inventario.append("Poção da Vida")

# Loop da batalha
while heroi.vida > 0 and vilao.vida > 0:

    print("\n--- Novo Turno ---\n")

    heroi.atacar(vilao)

    if vilao.vida <= 0:
        break

    vilao.atacar(heroi)

print("\n🏆 BATALHA TERMINOU 🏆")

if heroi.vida > 0:
    print(f"🎉 {heroi.nome} venceu a batalha!")
else:
    print(f"💀 {vilao.nome} venceu a batalha!")