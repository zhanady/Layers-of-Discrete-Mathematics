import pygame
import os
from mapa import *

class Jogo:
    def __init__(self):
        pygame.init()
        self.start_time = pygame.time.get_ticks()
        self.clock = pygame.time.Clock()



        # Configurações da tela
        self.display_width = 800
        self.display_height = 600
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('Layers of Discrete Mathematics')

        # Cores e fontes
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

        # Configurações do personagem
        self.calouro_width = 40
        self.calouro_height = 40

        # Imagens
        self.calouroImg_frente = pygame.image.load(os.path.join('assets', 'calouro_frente.png'))
        self.calouroImg_frente = pygame.transform.scale(self.calouroImg_frente, (40, 40))
        self.calouroImg_costas = pygame.image.load(os.path.join('assets', 'calouro_costas.png'))
        self.calouroImg_costas = pygame.transform.scale(self.calouroImg_costas, (200, 250))
        self.intro1 = pygame.image.load(os.path.join('assets', 'intro1.png'))
        self.intro2 = pygame.image.load(os.path.join('assets', 'intro2.png'))
        self.aulasono = pygame.image.load(os.path.join('assets', 'aulasono.png'))
        self.conjuntos = pygame.image.load(os.path.join('assets', 'pergunta1.png'))

    def mostrar_coordenadas(self, display, x, y):
        """Exibe as coordenadas do personagem na tela."""
        font = pygame.font.Font(None, 36)
        text = font.render(f"X: {x}, Y: {y}", True, self.black)
        display.blit(text, (10, 10))

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

        def calouro(x, y, image):
            self.gameDisplay.blit(image, (x, y))

        x, y = 0, 0
        x_change, y_change = 0, 0

        self.current_map = 1  # Começa no mapa 1
        Maps = Mapa(self.gameDisplay)

        map2_start_time = None  # Inicializa a variável para controlar o tempo do mapa 2
        map3_start_time = None
        while not GameExit:
            # Calcula o tempo total decorrido
            self.elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000

            # Renderiza o mapa atual
            if self.current_map == 1:
                if self.elapsed_time < 5:
                    self.gameDisplay.blit(self.intro1, (0, 0))  # Exibir primeira imagem
                elif self.elapsed_time < 10:
                    self.gameDisplay.blit(self.intro2, (0, 0))  # Exibir segunda imagem
                else:
                    Maps.mapa1()  # Exibe o mapa 1 após a introdução
                    calouroImg = self.calouroImg_frente

            elif self.current_map == 2:
                if map2_start_time is None:
                    map2_start_time = pygame.time.get_ticks()  # Define o início do mapa 2

                # Calcula o tempo decorrido no mapa 2
                map2_elapsed_time = (pygame.time.get_ticks() - map2_start_time) / 1000

                if map2_elapsed_time < 5:
                    # Exibe a imagem por 8 segundos no mapa 2
                    Maps.mapa2()
                    self.gameDisplay.blit(self.aulasono, (250, 0))
                    self.aulasono = pygame.transform.scale(self.aulasono, (300, 100))

                    calouroImg = self.calouroImg_costas
                else:
                    self.current_map = 3
            elif self.current_map == 3:
                if map3_start_time is None:
                    map3_start_time = pygame.time.get_ticks()
                map3_elapsed_time = (pygame.time.get_ticks() - map3_start_time) / 1000

                if map3_elapsed_time < 5:
                    # Exibe a imagem no mapa 3
                    self.gameDisplay.blit(self.conjuntos, (0, 0))
                    x = 1000
                    y = 1000
                elif map3_elapsed_time >= 5 and map3_elapsed_time <= 6:
                # Chama o método do mapa 3 após 8 segundos
                    Maps.mapa3_conjuntos()
                    x = 400 
                    y = 500
                    calouroImg = self.calouroImg_frente
                else:
                    Maps.mapa3_conjuntos()





            # Processa eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GameExit = True
                if self.current_map != 2 or (map2_start_time and map2_elapsed_time >= 8):
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
                    x, y = 327, 453  # Reinicia a posição
                    x_change = 0
                    y_change = 0
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

            if self.elapsed_time >= 10:  
                calouro(x, y, calouroImg)
                self.mostrar_coordenadas(self.gameDisplay, x, y)
            # Atualiza o display e controla o FPS
            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()
        quit()
