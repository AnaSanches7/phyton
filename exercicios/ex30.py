import random


computador = random.randint(0, 5)


print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
jogador = int(input("Em que número eu pensei? "))


if jogador == computador:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print("Eu ganhei! pensei no número {} e não no {}!".format(computador, jogador))
