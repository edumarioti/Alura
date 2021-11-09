import forca
import adivinhacao

def escolha_jogo():
    print('**********************************')
    print('********* Escolha o Jogo *********')
    print('**********************************\n')

    print('1 - Adivinhação')
    print('2 - Forca')


    jogo = int(input('\nQual escolheu?'))

    if (jogo == 1):
        adivinhacao.play()
    elif (jogo == 2):
        forca.play()

if (__name__ == "__main__"):
    escolha_jogo()