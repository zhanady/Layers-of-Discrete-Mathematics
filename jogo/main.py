import os, sys
dirpath = os.getcwd()
sys.path.append(dirpath)
if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)
from jogo import *
from menu import Menu  

def main():
    menu = Menu()  # Cria uma instância da classe Menu
    menu.game_intro()  # Exibe o menu e, depois, inicia o jogo
    #jogo = Jogo()  
    #jogo.openGame()  

if __name__ == "__main__":
    main() 
    
'''
- bugs: nao aparece a pergunta no mapa 2
- implementar inimigos
'''