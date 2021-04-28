print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************", end="\n\n")

numero_secreto = 42
total_tentativas = 3
rodada = 1

for rodada in range(1, total_tentativas +1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute = int(input('Digite o seu número: '))
    print("Você digitou o número {}".format(chute), end="\n\n")

    acertou = (chute == numero_secreto)
    maior = (chute > numero_secreto)
    menor = (chute < numero_secreto)

    if (acertou):
        print("Você acertou", end="\n\n")
        rodada = total_tentativas
    elif (maior):
        print("Você errou! O seu chute foi maior que o número secreto", end="\n\n\n")
    elif (menor):
        print("Você errou! O seu chute foi menor que o número secreto", end="\n\n\n")

print("Fim do jogo!")
