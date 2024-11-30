import pygame
import os

class Mapa:
    def __init__(self, gameDisplay):
        """Recebe a superfície principal onde os elementos serão desenhados."""
        self.gameDisplay = gameDisplay
        self.background = None

    def mapa1(self):
        """Desenha apenas o fundo do mapa 1."""
        self.background = pygame.image.load(os.path.join('assets', 'background_inicio.png'))
        self.gameDisplay.blit(self.background, (0, 0))

    def mapa2(self):
        """Desenha apenas o fundo do mapa 2."""
        self.background = pygame.image.load(os.path.join('assets', 'saladeaula.png'))
        self.gameDisplay.blit(self.background, (0, 0))
    def mapa3_conjuntos(self):
        """Desenha apenas o fundo do mapa 2."""
        self.background = pygame.image.load(os.path.join('assets', 'conjuntosright.png'))
        self.gameDisplay.blit(self.background, (0, 0))
    def mapa4_sequencias(self):
        """Desenha apenas o fundo do mapa 2."""
        self.background = pygame.image.load(os.path.join('assets', 'sequencias.png'))
        self.gameDisplay.blit(self.background, (0, 0))
    def mapa5_logica(self):
        """Desenha apenas o fundo do mapa 2."""
        self.background = pygame.image.load(os.path.join('assets', 'logica.png'))
        self.gameDisplay.blit(self.background, (0, 0))
    def mapa6_inducao(self):
        """Desenha apenas o fundo do mapa 2."""
        self.background = pygame.image.load(os.path.join('assets', 'inducao.png'))
        self.gameDisplay.blit(self.background, (0, 0))
    def gameover(self):
        """Desenha apenas o fundo do mapa 2."""
        self.background = pygame.image.load(os.path.join('assets', 'gameoverset.png'))
        self.gameDisplay.blit(self.background, (0, 0))
    def intro(self):
        """Desenha apenas o fundo do mapa 2."""

        
        self.gameDisplay.blit(self.background, (0, 0))

'''
    def textoSalaInicio(self):
        """Desenha apenas o fundo do mapa 2."""

        self.background = pygame.image.load(os.path.join('assets', 'gameoverset.png'))
        self.gameDisplay.blit(self.background, (0, 0))

    def textoSalaFim(self):
        """Desenha apenas o fundo do mapa 2."""

        self.background = pygame.image.load(os.path.join('assets', 'gameoverset.png'))
        self.gameDisplay.blit(self.background, (0, 0))
        
    def Pergunta1(self):
        """Desenha apenas o fundo do mapa 2."""
        
        self.background = pygame.image.load(os.path.join('assets', 'gameoverset.png'))
        self.gameDisplay.blit(self.background, (0, 0))
    def Pergunta2(self):
        self.background = pygame.image.load(os.path.join('assets', 'gameoverset.png'))
        self.gameDisplay.blit(self.background, (0, 0))
    def Pergunta3(self):
        self.background = pygame.image.load(os.path.join('assets', 'gameoverset.png'))
        self.gameDisplay.blit(self.background, (0, 0))
    def Pergunta4(self):
        self.background = pygame.image.load(os.path.join('assets', 'gameoverset.png'))
        self.gameDisplay.blit(self.background, (0, 0))
'''