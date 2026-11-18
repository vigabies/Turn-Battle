# Personagem: classe mae 
# Heroi: controlado pelo usuario 
# Inimigo: adversario do usuario

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
        print(f'Nome: {self.__nome}')
        print(f'Vida: {self.__vida}')
        print(f'Nivel: {self.__nivel}')


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f'Habilidade: {self.get_habilidade()}')


class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f'Tipo: {self.get_tipo()}')


class Jogo:
    """Classe orquestradora do jogo, responsável por gerenciar os personagens e a lógica do combate."""
    def __init__(self) -> None:
        self.heroi = Heroi(nome="Herói", vida=100, nivel=5, habilidade="Super Força")
        self.inimigo = Inimigo(nome="Morcego", vida=50, nivel=3, tipo="Voador")

    def iniciar_batalha(self):
        """"Inicia a batalha entre o herói e o inimigo, exibindo suas informações e iniciando o combate."""
        print("Batalha iniciada!")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nInformações dos Personagens:")
            print(self.heroi.exibir_informacoes())
            print(self.inimigo.exibir_informacoes())

            input("Pressione Enter para o herói atacar...")
            escolha = input("Escolha a ação do herói (1 - Atacar, 2 - Ataque Especial): ")

# Criar instância do jogo e iniciar a batalha
jogo = Jogo()
jogo.iniciar_batalha()