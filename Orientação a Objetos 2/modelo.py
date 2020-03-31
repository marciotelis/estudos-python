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

    def __str__(self):  # método especial (representação textual do objeto)
        return f"Nome: {self._nome} - Ano: {self.ano} - Likes: {self._likes}"


class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) #super extende a classe Filme a classe mãe (Programa) enviando os valores (nome, ano) e utilizando os métodos e atributos
        self.duracao = duracao
    
    def __str__(self):  #quando chamar programa.imprime() na verdade vai chamar este específico
        return f"Nome: {self._nome} - Ano: {self.ano} - Duração: {self.duracao} min - Likes: {self._likes}"


class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas
    
    def __str__(self):  #quando chamar programa.imprime() na verdade vai chamar este específico
        return f"Nome: {self._nome} - Ano: {self.ano} - Temporadas: {self.temporadas} - Likes: {self._likes}"


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    
    def __getitem__(self, item):
        return self._programas[item]

    # @property
    # def listagem(self):
    #     return self._programas

    def __len__(self):
        return len(self._programas)
    

vingadores = Filme("vingadores", 2018, 160)
atlanta = Serie("Atlanta", 2018, 2)
tmep = Filme("todo mundo em pânico",1999, 100)
demolidor = Serie("demolidor", 2016, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()


filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist("fim de semana", filmes_e_series)


print(f"tamanho da minha playlist: {len(playlist_fim_de_semana)}")

for programa in playlist_fim_de_semana: # for com um iterável, virou iterável pelo método __getitem__
    print(programa) # Assim chama a representação textual da classe (__str__)

print(f"Tá ou não tá? {demolidor in playlist_fim_de_semana}")   # Jeito de utilizar uma comparação, o in percorre a lista dentro da playlist e ve se tem demolidor (com o __getitem__ da pra iterear)
