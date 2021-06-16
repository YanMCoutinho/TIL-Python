import forca
import adivinhacao

def escolher_jogo():
    print("*********************************")
    print("        Escolha seu jogo!        ")
    print("*********************************", end="\n\n")

    print("(1) Forca (2) Adivinhação")
    jogo = int(input("Qual jogo você quer jogar? "))

    if (jogo == 1):
        print("\nJogando forca\n")
        forca.jogar()
    elif (jogo == 2):
        print("\nJogando adivinhação\n")
        adivinhacao.jogar()
if (__name__ == "__main__"):
    escolher_jogo()
