def jogar():
    print("**********************************")
    print("   Bem vindo ao jogo da forca!")
    print("**********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip() #Se tiver espaço antes ou depois não considera

        index =  0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()): #usa o upper pra passar tudo pra maiúscula pra não ter diferença se o usuário digitar maiúsculo ou minúsculo
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)
                


   
    print("fim do jogo!")
   

# Se for executado direto este será o main e então executará, senão não executa (para não executar no import)
if(__name__ == "__main__"):
    jogar()