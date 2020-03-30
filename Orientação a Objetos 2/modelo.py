class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()   #apenas um _ faz com que não esteja realmente privado (protegido), podendo ser acessado por outra classe, porém por convenção se diz que não se deve modificar os valores de atributos com _ diretamente e sim pelos getters e setters
        self.ano = ano
        self._likes = 0

    @property
    def nome(self):
        return self._nome

    @property
    def likes(self):
        return self._likes

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def dar_like(self):
        self._likes += 1


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) #super extende a classe Filme a classe mãe (Programa) enviando os valores (nome, ano) e utilizando os métodos e atributos
        self.duracao = duracao


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
        


vingadores = Filme("vingadores", 2018, 160)
vingadores.dar_like()
print(f"Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} - Likes: {vingadores.likes}")

atlanta = Serie("Atlanta", 2018, 2)

atlanta.dar_like()
atlanta.dar_like()
print(f"Nome: {atlanta.nome} - Ano: {atlanta.ano} - Temporadas: {atlanta.temporadas} - Likes: {atlanta.likes}")


filmes_e_series = [vingadores, atlanta]

for programa in filmes_e_series:
    detalhes = programa.duracao if hasattr(programa, "duracao") else programa.temporadas    # Verifica se tem o atributo duracao, se nao tiver usa o temporadas
    print(f"Nome: {programa.nome} - Ano: {programa.ano} - Duração: {detalhes} - Likes: {programa.likes}")