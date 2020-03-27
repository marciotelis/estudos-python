print("**********************************")
print("Bem vindo ao jogo de adivinhação!")
print("**********************************")

numero_secreto = 42
numero_tentativas = 3
rodada = 1

while(rodada <= numero_tentativas):
    print("rodada nº ", rodada, " do total de ", numero_tentativas)

    # O input sempre retorna uma variável str
    chute = input("Digite o seu número: ")
    chute = int(chute)

    print("Você digitou ", chute)
    print("")

    # Melhorando a legibilidade podemos já fazer algumas regras (porém não é obrigatório)
    acertou = chute == numero_secreto
    maior = chute > numero_secreto

    if (acertou):   # Atentar a sempre colocar os :
        print("Você acertou")
        rodada = 4
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
