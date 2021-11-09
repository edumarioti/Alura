from random import randrange

def play():

    mensagem_cabeçalho()
    palavra_secreta = carrega_palavra_secreta()
    letras_corretas = inicializa_letras_acertadas(palavra_secreta)
    imprime_letras_corretas(letras_corretas)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):

        chute = pede_chute()
     
        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_corretas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = not '_' in letras_corretas
        imprime_letras_corretas(letras_corretas)

    if (acertou):
       imprime_mensagem_vencedor()
    else:
       imprime_mensagem_perdedor(palavra_secreta)

def mensagem_cabeçalho():
    print('*********************************')
    print('**********Jogo da Forca**********')
    print('*********************************')

def carrega_palavra_secreta():
    arquivo = open('palavras.txt', 'r')
    palavras = []
    
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()

    numero = randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]

def pede_chute():
    chute = input('Qual a letra?').strip().upper()
    return chute

def marca_chute_correto(chute, letras_corretas, palavra_secreta):
    index = 0 
    for letra in palavra_secreta:
        if (chute == letra):
            letras_corretas[index] = letra
        index += 1

def imprime_mensagem_vencedor():
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

def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
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

def imprime_letras_corretas(letras_corretas):
    print('Adivinhe a palavra:', end='')
    for letra in letras_corretas:
        print(letra, end=' ')
    print()

if (__name__ == "__main__"):
    play()