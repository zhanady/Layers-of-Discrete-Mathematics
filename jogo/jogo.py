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

    def warninglimitMapa1(self):
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
    
        self.current_map = 1  # Inicializa no mapa 1
        Maps = Mapa(self.gameDisplay)
        
        while not GameExit:
            # Preenche a tela com branco
            #self.gameDisplay.fill(self.white)
            
            # Renderiza o mapa atual
            if self.current_map == 1:
                Maps.mapa1()
            elif self.current_map == 2:
                Maps.mapa2()
    
            # Desenha o calouro
            
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
    
            # Verifica transições de mapa
            if self.current_map == 1:
                if 350 <= x <= 400 and 555 <= y <= 600:
                        self.current_map = 2  # Troca para o mapa 2
                        x, y = 0, 0  # Reinicia a posição
                elif 670 <= x <= 720 and 60 <= y <= 140:
                    self.warningru()
                elif x < 0:
                    x = 0
                    self.warninglimitMapa1()
                elif x > self.display_width - self.calouro_width:
                    x = self.display_width - self.calouro_width
                    self.warninglimitMapa1()
                elif y < 0:
                    y = 0
                    self.warninglimitMapa1()
                elif y > self.display_height - self.calouro_height:
                    y = self.display_height - self.calouro_height
                    self.warninglimitMapa1()
    
                    
    
            elif self.current_map == 2:
                # Adicione condições específicas para o mapa 2, se necessário
                pass
            
            calouro(x, y)
            # Atualiza o display e controla o FPS
            pygame.display.update()
            self.clock.tick(60)
    
        pygame.quit()
        quit()