meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

'''
aparicoes = {}

for palavra in meu_texto.split():
    ate_agora = aparicoes.get(palavra, 0)
    aparicoes[palavra] = ate_agora + 1
    print(aparicoes)
'''

#       UTILIZANDO DEFAULT DICT - PARA NÃO PRECISAR USAR O GET E INDICAR QUE SE NÃO TIVER AINDA ADICIONAR COM O VALOR
from collections import defaultdict

aparicoes = defaultdict(int)        # int é uma função que retorna zero se não for colocado nenhum valor (que é o que se quer)

for palavra in meu_texto.split():
    aparicoes[palavra] += 1         # simplificando, se não tem vai atribuir zero, se tem atribui o valor e sempre vai somar um
    print(aparicoes)
