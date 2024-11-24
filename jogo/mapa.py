import pygame
import os

class Mapa:
    def __init__(self, gameDisplay):
        """Recebe a superfície principal onde os elementos serão desenhados."""
        self.gameDisplay = gameDisplay
        self.background = pygame.image.load(os.path.join('assets', 'background_inicio.png'))
    def mapa1(self):
        pygame.init()
				
        self.background = pygame.image.load(os.path.join('assets', 'background_inicio.png'))
        self.gameDisplay.blit(self.background, (0, 0))  # Posiciona o fundo no canto superior esquerdo
        pygame.display.update()  
    def mapa2(self):
        pygame.init()
				
        self.background = pygame.image.load(os.path.join('assets', 'background_inicio.png'))
        self.gameDisplay.blit(self.background, (0, 0))  # Posiciona o fundo no canto superior esquerdo
        #pygame.display.update()  