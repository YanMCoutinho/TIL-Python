import random

def jogar():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************", end="\n\n")

    numero_secreto = random.randint(1, 100)
    total_tentativas = 0
    pontos = 100
    rodada = 1

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o Nível: "))

    if (nivel==1):
        total_tentativas = 20
    elif (nivel==2):
        total_tentativas = 10
    elif (nivel==3):
        total_tentativas = 5
    else:
        print("Era preciso um número válido")

    for rodada in range(1, total_tentativas + 1):
        print("\nTentativa {} de {}".format(rodada, total_tentativas))
        chute = int(input('Digite um número entre 1 em 100: '))
        print("Você digitou o número {}".format(chute), end="\n\n")

        if (chute < 0 or chute > 100):
            print("ERRO! Você deve digitar um número entre 1 e 100", end="\n\n")
            continue

        acertou = (chute == numero_secreto)
        maior = (chute > numero_secreto)
        menor = (chute < numero_secreto)

        if (acertou):
            print("Você acertou e fez {} pontos".format(pontos), end="\n\n")
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto", end="\n\n\n")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto", end="\n\n\n")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            if (rodada == total_tentativas or pontos <= 0):
                print("Você perdeu! O número secreto era {}. Você fez {} pontos".format(numero_secreto, pontos))
                break
    print("Fim do jogo!")

if (__name__ == "__main__"):
    jogar()