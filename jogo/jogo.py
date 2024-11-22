import pygame
import os
from mapa import *

class Jogo:
    def __init__(self):
        pygame.init()

        # Configurações da tela
        self.display_width = 800
        self.display_height = 600
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Layers of Discrete Mathematics')

        # Carrega os recursos
        self.background = pygame.image.load(os.path.join('assets', 'background_inicio.png'))
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.red = (255, 0, 0)
        self.blue = (0, 0, 255)

        self.calouro_width = 40
        self.calouro_height = 40
        self.clock = pygame.time.Clock()

        self.calouroImg = pygame.image.load(os.path.join('assets', 'calouro.png'))
        self.calouroImg = pygame.transform.scale(self.calouroImg, (40, 40))

    def text_objects(self, text, font):
        """Função auxiliar para renderizar texto."""
        textSurface = font.render(text, True, self.black)
        return textSurface, textSurface.get_rect()

    def message_display(self, text):
        """Exibe uma mensagem temporária na tela."""
        largeText = pygame.font.Font('freesansbold.ttf', 25)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = (self.display_width / 2, self.display_height / 2)
        self.gameDisplay.blit(TextSurf, TextRect)
        pygame.display.update()
        pygame.time.wait(2000)

    def warninglimit(self):
        self.message_display('Esse não é o caminho para o CTC')

    def warningru(self):
        self.message_display('RU fechado para manutenção')

    def openGame(self):
        GameExit = False

        def calouro(x, y):
            self.gameDisplay.blit(self.calouroImg, (x, y))

        x = 0
        y = 0
        x_change = 0
        y_change = 0
        font = pygame.font.SysFont("Arial", 25)

        while not GameExit:
            # Preenche a tela com o fundo branco
            self.gameDisplay.fill(self.white)

            # Renderiza o texto de coordenadas
            coords_text = font.render(f"Coordenadas: ({x}, {y})", True, self.red)
            self.gameDisplay.blit(coords_text, (10, 10))

            # Processa eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -3
                    elif event.key == pygame.K_RIGHT:
                        x_change = 3
                    elif event.key == pygame.K_UP:
                        y_change = -3
                    elif event.key == pygame.K_DOWN:
                        y_change = 3
                if event.type == pygame.KEYUP:
                    if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                        x_change = 0
                    elif event.key in [pygame.K_UP, pygame.K_DOWN]:
                        y_change = 0

            # Atualiza as coordenadas
            x += x_change
            y += y_change

            # Desenha o mapa
            Maps = Mapa()
            Maps.mapa1()

            # Desenha o calouro
            calouro(x, y)

            # Verifica limites da tela
            if x < 0:
                x = 0
                self.warninglimit()
            if x > self.display_width - self.calouro_width:
                x = self.display_width - self.calouro_width
                self.warninglimit()
            if y < 0:
                y = 0
                self.warninglimit()
            if y > self.display_height - self.calouro_height:
                y = self.display_height - self.calouro_height
                self.warninglimit()

            # Verifica coordenadas específicas
            if 680 <= x <= 700 and 140 <= y <= 160:
                self.warningru()

            # Atualiza o display e controla o FPS
            pygame.display.update()
            self.clock.tick(60)

        pygame.quit()
        quit()