import random



def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palavra_secreta):
            mostra_letra_certa(chute, palavra_secreta, letras_acertadas)
        else:
            erros += 1

        enforcou = erros == 6   # Aqui ta testando se erros é igual a 6, a resposta da TRUE ou FALSE, e é gravada em enforcou
        acertou = "_" not in letras_acertadas # Se _ não tiver mais em letras_acertadas retorna TRUE

        print(letras_acertadas)

    if(acertou):
        print("Você ganhou!\n")
    else:
        print("Você perdeu!\n")

    print("fim do jogo!\n")


def imprime_mensagem_abertura():
    print("**********************************")
    print("   Bem vindo ao jogo da forca!")
    print("**********************************")


def carrega_palavra_secreta():
    # MANIPULANDO UM ARQUIVO
    arquivo = open("palavras.txt", "r")  # abrindo o arquivo como leitura
    palavras = []
    for linha in arquivo:
        linha = linha.strip()   # retira os caracteres especiais das palavras (\n, espaços...)
        palavras.append(linha)  #add cada linha (palavra neste caso) do arquivo na lista palavras
    arquivo.close()  # fecha o arquivo (sempre é interessante fechar para não deixar o sistema operacional com este arquivo aberto, consumindo memória, processamento, etc)

    numero = random.randrange(0, len(palavras)) # gera um número randômico entre 0 e o tamanho da lista palavras (quantas palavras tem)
    palavra_secreta = palavras[numero].upper()  # seleciona a palavra deste número (o índice) colocando todas as letras em maiúscula

    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()   # Se tiver espaço antes ou depois não considera e todas letras são maiúsculas
    return chute


def mostra_letra_certa(chute, palavra_secreta, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra): # usa o upper pra passar tudo pra maiúscula pra não ter diferença se o usuário digitar maiúsculo ou minúsculo
            letras_acertadas[index] = letra
        index += 1


# Se for executado direto este será o main e então executará, senão não executa (para não executar no import)
if(__name__ == "__main__"):
    jogar()
