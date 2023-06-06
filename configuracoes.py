import time
import os 
import sys

def limparTela():
    os.system("cls")

def restartGame():
    python = sys.executable
    os.execl(python, python, * sys.argv)

def desenha_forca(erros):
    print("  ____     ")
    print(" |/  |    ")
    if(erros == 1):
        print("      ",cabeca)

    if(erros == 2):
        print("      ",tronco)

    if(erros == 3):
        print("      ",braco_esquerdo)

    if(erros == 4):
        print("      ",braco_direito)

    if(erros == 5):
        print("      ",perna_esquerda)
       
    if(erros == 6):
        print("      ",perna_direita)
    else:
        print("você perdeu!!")    
        
        
    print(" |            ")
    print("_|___         ")
    print()

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

chances = [vazio, cabeca, tronco, braco_esquerdo, braco_direito, perna_esquerda, perna_direita]


