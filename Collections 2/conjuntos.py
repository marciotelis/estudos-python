'''
#--------------------------------------------------- DIFERENÇA ENTRE LISTA E CONJUNTOS ------------------------------------------------------------------

usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13,23,56,42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(assistiram)   # irá conter os elementos das listas, porém irá repetir se tiverem elementos iguais nas listas

print(set(assistiram))     #criando um conjunto, dessa forma não duplica e apenas agrupa


#   CRIANDO DIRETAMENTE O CONJUNTO
assistiram2 = {15, 23, 43, 56, 13, 23, 56, 42}  # no caso de conjuntos a ordem não importa, não consegue acessar idexado, não existe posição específica
print(assistiram2)

#--------------------------------------------------------------------------------------------------------------------------------------------------------
'''

'''
#----------------------------------- ITERANDO O CONJUNTO ------------------------------------
for usuario in assistiram2:     # pode iterar, acessar, etc. Mas não tem posição específica
    print(usuario)
#--------------------------------------------------------------------------------------------
'''

#   OPERAÇÕES DE CONJUNTOS
usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13,23,56,42}

print(usuarios_data_science | usuarios_machine_learning)        # em conjuntos um OU (OR) outro mostra o conteúdo dos dois
print(usuarios_data_science & usuarios_machine_learning)        # & (E - AND) mostra quem está nos dois conjuntos
print(usuarios_data_science - usuarios_machine_learning)        # mostra quem está no conjunto data_science mas não está no conjunto machine learning
print(usuarios_data_science ^ usuarios_machine_learning)        # OU EXCLUSIVO (XOR) fez um ou outro mas não fez os dois

#   FUNÇÕES DE CONJUNTOS
print()
usuarios = {1, 5, 76, 34, 52, 13, 17}
print(len(usuarios))
usuarios.add(13)        # aceita a adição porém como já tem no conjunto não modifica nada
print(len(usuarios))
usuarios.add(765)       # agora sim, como não tinha no conjunto é adicionado
print(len(usuarios))

#   CRIANDO UM CONJUNTO IMUTÁVEL
usuarios = frozenset(usuarios)
print(type(usuarios))
print(usuarios)

# usuarios.add(123)     - dá erro porque não pode adicionar nada no conjunto imutável

#   EXEMPLO SEPARANDO UMA STRING EM PALAVRAS E COLOCANDO EM UM CONJUNTO
texto = "Olá meu nome é Márcio e eu estou fazendo o curso do Alura de Collections para Python. Eu estou gostando do curso."
print(texto.split())        # split separar por padrão por espaço (" "), se quiser separar por outra coisa é só colocar dentro do split
print(set(texto.split()))
