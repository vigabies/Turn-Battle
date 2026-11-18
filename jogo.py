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


heroi = Heroi(nome="Arthur", vida=100, nivel=5, habilidade="Espada")
inimigo = Inimigo(nome="Goblin", vida=50, nivel=2, tipo="Monstro")

print("Informações do Herói:")
heroi.exibir_informacoes()
print("\nInformações do Inimigo:")
inimigo.exibir_informacoes()