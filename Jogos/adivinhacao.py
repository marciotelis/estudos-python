print("**********************************")
print("Bem vindo ao jogo de adivinhação!")
print("**********************************")

numero_secreto = 42
numero_tentativas = 3
rodada = 1

while(rodada <= numero_tentativas):
    #print("rodada nº ", rodada, " do total de ", numero_tentativas)
    print("rodada nº {} do total de {}".format(
        rodada, numero_tentativas))  # formatando a string

    # O input sempre retorna uma variável str
    chute = input("Digite o seu número entre 1 e 100: ")
    chute = int(chute)

    print("Você digitou ", chute)
    print("")

    if((chute < 1) or (chute > 100)):
        print("Você deve digitar um número emtre 1 e 100!")
        print("")
        continue

    # Melhorando a legibilidade podemos já fazer algumas regras (porém não é obrigatório)
    acertou = chute == numero_secreto
    maior = chute > numero_secreto

    if (acertou):   # Atentar a sempre colocar os :
        print("Você acertou")
        break
    else:
        if(maior):
            print("Você errou, seu chute foi MAIOR que o número secreto")
        else:
            print("Você errou, seu chute foi MENOR que o número secreto")

        print("Você tem mais ", (numero_tentativas - rodada), " tentativas")
        rodada = rodada + 1
        print("")

print()
print("Fim do jogo")


# Teste do for--------------------------------------------------------------------------------
for variavel in range(1, 10):  # for conta de 1 a 9 (é enquanto for menor que 10)
    print(variavel)

print()
for variavel in range(1, 10, 2):  # for igual ao de cima porém incrementando de 2 em 2
    print(variavel)

# ----------------------------------------------------------------------------------------------


# Teste de mais formatações de strings----------------------------------------------------------------------

# indica que é float
print("R$ {:f}".format(4.5))

# diz que quer 2 casas decimais
print("R$ {:.2f}".format(4.5))

# diz que são um total de 5 dígitos e 2 são depois da vírgula. Completa o que falta com espaço em branco
print("R$ {:5.2f}".format(4.5))

# diz que são um total de 5 dígitos e 2 são depois da vírgula. Completa o que falta com 0
print("R$ {:05.2f}".format(4.5))

#------------------------------------------------------------------------------------------------------------
