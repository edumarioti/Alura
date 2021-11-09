from random import randrange

def play():
    print('**********************************')
    print('*******Jogo de adivinhação********')
    print('**********************************')

    numero_secreto = randrange(1,101)
    total_de_tentativas = 33
    pontos = 1000

    print('Escolha a dificulde:')
    print('    1 - Fácil')
    print('    2 - Médio')
    print('    3 - Difícil')
    dificuldade = int(input('Defina a dificulade:'))

    if (dificuldade == 1):
        total_de_tentativas = 20
    elif (dificuldade == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5
        
    for rodada in range (1, total_de_tentativas + 1):
        print(f'Tentativa {rodada} de {total_de_tentativas}.')
        chute = int(input('Digite um número entre 1 e 100:'))

        if (chute < 1 or chute > 100):
            print('Digite um número entre 1 e 100!')
            continue

        acertou = numero_secreto == chute
        menor = numero_secreto < chute 
        maior = numero_secreto > chute 
        if (acertou):
            print(f'Você acertou e fez {pontos} pontos')
            break
        else:
            if (menor):
                print('Que pena, você errou, o número secreto é menor')
            elif(maior):
                print('Que pena, você errou, o número secreto é maior')
            pontos_perdidos = abs(numero_secreto - chute)
            pontos -= pontos_perdidos
    print('fim de jogo...')

if (__name__ == "__main__"):
    play()