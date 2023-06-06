#Alunos: Vitor Quadros / Abner Panazollo RA: 1134821 / 1134868
def mostra_dicas(dicas):
    if(dicas == 1):
        print(dica1)
    if(dicas == 2):
        print(dica2)
    if(dicas == 3):
        print(dica3)
    if(dicas > 3):
        print("voce não tem mais dicas")
    return dicas 


forca = """
____
    |
    
"""

vazio = ""

cabeca = """
    O
    """
tronco = """
    O
    |
    """
braco_esquerdo = """
     O
    /|
    """
braco_direito = """
     O
    /|\\
    """ 
perna_esquerda = """
     O
    /|\\
    /
"""
perna_direita = """
     O
    /|\\
    / \\
"""
acertos = 0
erros = ''
chances = [vazio, cabeca, tronco, braco_esquerdo, braco_direito, perna_esquerda, perna_direita,erros]

from configuracoes import limparTela, desenha_forca,restartGame
jogar = True
while jogar ==True:
    print("----------------------")
    print(" JOGO DA FORCA (x_x)  ")
    print("----------------------")
    desafiante = input("Desafiante: ")
    competidor = input("Competidor: ")
    limparTela()

    palavra = input("Digite a palavra para começar o jogo: ").upper()
    print("O desafiante deve informar 3 dicas para o competidor")
    dica1 = input("Primeira dica: ")
    dica2 = input("Segunda dica: ")
    dica3 = input("Terceira dica: ")
    limparTela()
    letras = [palavra]
    for item in letras:
        item = list(item)

    print("A palavra do jogo contém: ", len(item) , "letras!!!" )
    try:
        comecar = int(input("Deseja obter a primeira dica? (1) para sim (0) para começar o jogo: "))
    except:
        print("valor invalido...")
    limparTela()

    acertos = 0
    erros = 0

    letras_acertadas = ''
    letras_erradas = ''

    dicas = 1
    listadicas = [dica1,dica2,dica3]
    while comecar == 1:
        mostra_dicas(dicas)
        dicas = dicas+1
        comecar = int(input("Deseja obter mais dicas? (1) para sim (0) para começar o jogo: "))
    if comecar == 0:
        while acertos != len(palavra) or erros != 7: 
            mensagem = ''
            for letra in palavra:
                if letra in letras_acertadas:
                    print(letra)
                    mensagem += letra
                else:
                    print('_ ')
            print(forca+chances[erros])

            print("Letras acertadas: " + letras_acertadas)
            print("Letras Erradas: " + letras_erradas)
            letra = input("Digite a letra: ").upper()

            if letra in palavra:
                acertos += 1
                letras_acertadas += letra
                if acertos == len(palavra):
                    print("Parabéns!! Você ganhou o jogo!!")
                    print("A palavra era: ", palavra)
                    print("Você acertou as letras: " + letras_acertadas)
                    print("Você errou as letras: " + letras_erradas)
                    vencedor = competidor
                    perdedor = desafiante
                    jogarNovamente = int(input("deseja jogar novamente(1)-sim  (0)-não: "))
                    if jogarNovamente == 1:
                        limparTela()
                        break
                    if jogarNovamente == 0:
                        print("obrigado por ter jogado!! ")
                        jogar = False
                        break

                elif erros >6:
                    print("Você perdeu")
                    print("A palavra era: ", palavra)
                    print("Você acertou as letras: " + letras_acertadas)
                    print("Você errou as letras: " + letras_erradas)
                    vencedor = desafiante
                    perdedor = competidor
                    jogarNovamente = int(input("deseja jogar novamente(1)-sim  (0)-não: "))
                    if jogarNovamente == 1:
                       limparTela()
                       break
                    if jogarNovamente == 0:
                        print("obrigado por ter jogado!! ")
                        jogar = False
                        break
            else:
                print("Você errou a letra")
                desenha_forca(erros)
                erros += + 1
                letras_erradas += letra
        
    arquivo = open("resultado_partidas.txt","a")
    arquivo.write("Vencedor: "+vencedor+" Perdedor: "+perdedor+ " Palavra: "+palavra+"\n")
    arquivo.close()