import random

def jogar():

    imprimir_abertura()
    palavra_secreta = carregar_palavra_secreta()
    letras_acertadas = inicializar_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):

        chute = pedir_chute(erros, letras_acertadas)

        if(chute in palavra_secreta):
            letras_acertadas = marcar_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            desenhar_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas

    imprimir_resultado(acertou, palavra_secreta)
    print("Fim do jogo!")


def imprimir_abertura():
    print("*********************************")
    print("Bem vindo ao jogo de Forca!")
    print("*********************************", end="\n\n")


def carregar_palavra_secreta():
    palavras = []

    with open("palavras.txt") as arquivo:
        for linha in arquivo:
            palavras.append(linha.strip())

    numero = random.randrange(0, len(palavras), 1)

    palavra_secreta = palavras[numero].lower()
    return palavra_secreta


def inicializar_letras_acertadas(palavra):
    return ["_" for letra in palavra]


def pedir_chute(erros, letras_acertadas):
    print("{}{}".format("\n", letras_acertadas))
    print("{} erros de 6".format(erros))
    chute = input("Qual letra? ")
    chute = chute.strip().lower()
    return chute


def marcar_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1
    return letras_acertadas


def desenhar_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def imprimir_resultado(acertou, palavra_secreta):
    if(acertou):
        print("Parabéns, você ganhou!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")
    else:
        print("Puxa, você foi enforcado!")
        print("A palavra era {}".format(palavra_secreta))
        print("    _______________        ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\   ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/    ")
        print(" |   XXX       XXX   |     ")
        print(" |                   |     ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |       ")
        print("   | I I I I I I I |       ")
        print("   |  I I I I I I  |       ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")


if (__name__ == "__main__"):
    jogar()