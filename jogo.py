# Personagem: classe mae
# Heroi: controlado pelo usuario
# Inimigo: adversario do usuario
import random

class Personagem:
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome

    def get_vida(self):
        return self.__vida

    def get_nivel(self):
        return self.__nivel

    def exibir_informacoes(self):
        return f"Nome: {self.get_nome()}, Vida: {self.get_vida()}, Nível: {self.get_nivel()}"

    def receber_dano(self, dano):
        """Diminui a vida do personagem, sem deixar ficar negativa."""
        self.__vida = max(0, self.__vida - dano)

    def atacar(self, alvo):
        """Ataque normal: dano aleatório baseado no nível."""
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 10)
        alvo.receber_dano(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} causando {dano} de dano!")


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade

    def exibir_informacoes(self):
        return f"{super().exibir_informacoes()}, Habilidade: {self.get_habilidade()}"

    def ataque_especial(self, alvo):
        """Ataque especial: dano aleatório maior que o ataque normal."""
        dano = random.randint(self.get_nivel() * 8, self.get_nivel() * 15)
        alvo.receber_dano(dano)
        print(f"{self.get_nome()} usou {self.get_habilidade()} em {alvo.get_nome()} causando {dano} de dano!")


class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def exibir_informacoes(self):
        return f"{super().exibir_informacoes()}, Tipo: {self.get_tipo()}"


class Jogo:
    """Classe orquestradora do jogo, responsável por gerenciar os personagens e a lógica do combate."""
    def __init__(self) -> None:
        self.heroi = Heroi(nome="Herói", vida=100, nivel=5, habilidade="Super Força")
        self.inimigo = Inimigo(nome="Morcego", vida=50, nivel=3, tipo="Voador")

    def iniciar_batalha(self):
        """Inicia a batalha entre o herói e o inimigo."""
        print("Batalha iniciada!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nInformações dos Personagens:")
            print(self.heroi.exibir_informacoes())
            print(self.inimigo.exibir_informacoes())

            escolha = input("\nEscolha a ação do herói (1 - Atacar, 2 - Ataque Especial): ")

            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha inválida. Escolha novamente.")
                continue  # volta ao início sem o inimigo atacar

            # Turno do inimigo (só se ainda estiver vivo)
            if self.inimigo.get_vida() > 0:
                self.inimigo.atacar(self.heroi)

        print("\nFim da batalha!")
        if self.heroi.get_vida() > 0:
            print(f"{self.heroi.get_nome()} venceu!")
        else:
            print(f"{self.inimigo.get_nome()} venceu!")


# Criar instância do jogo e iniciar a batalha
jogo = Jogo()
jogo.iniciar_batalha()