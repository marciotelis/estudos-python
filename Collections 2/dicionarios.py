#   Utilizando  dicionário (mapas, etc)
#    ter chave e valor {chave : valor}

aparicoes = {
    "Guilherme" : 1,
    "cachorro" : 2,
    "nome" : 2,
    "vindo" : 1
}

'''
print(type(aparicoes))      # tipo dict

print(aparicoes["Guilherme"])
print(aparicoes["cachorro"])

print(aparicoes.get("dasfas", 0))      # dessa forma se não tiver o que se procura neste dicionário retorna 0 e não dá erro. Se tentar diretamente dará erro na compilação
print(aparicoes.get("cachorro", 0))

#      CRIANDO PELO COSTRUTOR       - é menos comum utilizar desta forma, que nem list não se utiliza o construtor e sim diretamente
aparicoes2 = dict(Guilherme = 2, cachorro = 2, nome = 2, vindo = 1)
print(aparicoes)
print(aparicoes2)
'''

#       MODIFICANDO O DICIONÁRIO
aparicoes["Carlos"] = 1     # adicionando
print(aparicoes)
aparicoes["Carlos"] = 2     # modificando
print(aparicoes)
del aparicoes["Carlos"]     # deletando
print(aparicoes)

#       ITERANDO EM DICIONÁRIOS
print("Carlos" in aparicoes)        

for elemento in aparicoes:          # desta irá retornar apenas as chaves e não os valores
    print(elemento)

for elemento in aparicoes.keys():   # também retorna as chaves
    print(elemento)

for elemento in aparicoes.values(): # retorna os valores
    print(elemento)

for elemento in aparicoes.items():  # retorna os dois
    print(elemento)

print([f"palavra {chave}" for chave in aparicoes.keys()])       # adicionando uma palavra a cada elemento