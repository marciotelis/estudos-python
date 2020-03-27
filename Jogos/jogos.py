import forca
import adivinhacao

print("**********************************")
print("         Lista de jogos")
print("**********************************")

print()
print("(1) Jogo da adivinhação")
print("(2) Jogo da forca")
print()

jogo_selecionado = int(input("Escolha o seu jogo: "))

if(jogo_selecionado == 1):
    # seleciona o jogo da adivinhação
    adivinhacao.jogar()
elif(jogo_selecionado == 2):
    # seleciona o jogo da forca
    forca.jogar()