def jogar():
    print("**********************************")
    print("   Bem vindo ao jogo da forca!")
    print("**********************************")

    palavra_secreta = "abacate".upper()
    letras_acertadas = []

    for letra in palavra_secreta:
        letras_acertadas.append("_")

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper() #Se tiver espaço antes ou depois não considera e todas letras são maiúsculas

        if(chute in palavra_secreta):
            index =  0
            for letra in palavra_secreta:
                if(chute == letra): #usa o upper pra passar tudo pra maiúscula pra não ter diferença se o usuário digitar maiúsculo ou minúsculo
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
        
        enforcou = erros == 6  #Aqui ta testando se erros é igual a 6, a resposta da TRUE ou FALSE, e é gravada em enforcou
        acertou = "_" not in letras_acertadas #Se _ não tiver mais em letras_acertadas retorna TRUE

        print(letras_acertadas)
                

    if(acertou):
        print("Você ganhou!")
        print()
    else:
        print("Você perdeu!")
        print()
   
    print("fim do jogo!")
   

# Se for executado direto este será o main e então executará, senão não executa (para não executar no import)
if(__name__ == "__main__"):
    jogar()