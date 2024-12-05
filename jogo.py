import pygame
import os
from mapa import *
import time 
import math

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

        # Cores
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
        self.conjuntos = pygame.image.load(os.path.join('assets', 'pergunta1.png'))
        self.logica = pygame.image.load(os.path.join('assets', 'pergunta2.png'))
        self.pergunta3 = pygame.image.load(os.path.join('assets', 'pergunta3.png'))
        self.pergunta4 = pygame.image.load(os.path.join('assets', 'pergunta4.png'))
        self.perseguidor2_img = pygame.image.load(os.path.join('assets', 'perseguidor2.png'))
        self.perseguidor1_img = pygame.image.load(os.path.join('assets', 'perseguidor1.png'))
        self.perseguidor1_img = pygame.transform.scale(self.perseguidor1_img, (50, 50)) 
        self.perseguidor2_img = pygame.transform.scale(self.perseguidor2_img, (50, 50)) 


    def perseguir_calouro(self, perseguidores, calouro_pos, velocidade):
        """
        Faz os perseguidores perseguirem o calouro.
        :param perseguidores: Lista de dicionários com posição {'x': valor, 'y': valor}.
        :param calouro_pos: Dicionário com a posição atual do calouro {'x': valor, 'y': valor}.
        :param velocidade: Velocidade dos perseguidores.
        :param gameover: Função a ser chamada caso um perseguidor alcance o calouro.
        """

        for perseguidor in perseguidores:
            # Calcula a diferença de posição entre perseguidor e calouro
            dx = calouro_pos['x'] - perseguidor['x']
            dy = calouro_pos['y'] - perseguidor['y']

            # Calcula a distância atual entre eles
            distancia = math.sqrt(dx**2 + dy**2)

            # Verifica se o perseguidor alcançou o calouro
            if distancia < 30:  # Tamanho do raio de colisão
                Maps = Mapa(self.gameDisplay)
                Maps.gameover()  # Chama a função gameover
                self.current_map = 3
                perseguidores = [{'x': 100, 'y': 100}, {'x': 700, 'y': 500}]

                
                return

            # Atualiza a posição do perseguidor para se aproximar do calouro
            perseguidor['x'] += velocidade * (dx / distancia)
            perseguidor['y'] += velocidade * (dy / distancia)

    '''
    def mostrar_coordenadas(self, display, x, y):
        """Exibe as coordenadas do personagem na tela."""
        """Utilizado durante a construção do jogo para ver as coordenadas das portas do jogo, por exemplo"""
        font = pygame.font.Font(None, 36)
        text = font.render(f"X: {x}, Y: {y}", True, self.black)
        display.blit(text, (10, 10))
    '''
    def text_objects(self, text, font):
        """Função auxiliar para renderizar texto."""
        textSurface = font.render(text, True, self.black)
        return textSurface, textSurface.get_rect()

    def message_display(self, text, x=400, y=300, font=20):  # Valores padrão do texto
        """Funcao para mostrar um texto na tela"""
        largeText = pygame.font.Font('freesansbold.ttf', font)
        TextSurf, TextRect = self.text_objects(text, largeText)
        TextRect.center = (x, y)  # Usa os parâmetros passados ou valores padrão
        self.gameDisplay.blit(TextSurf, TextRect)
        
    def message_display_white(self, text, x=400, y=300, font=20):  # Valores padrão do texto
        """Funcao para mostrar um texto na tela em branco"""
        largeText = pygame.font.Font('freesansbold.ttf', font)
        TextSurf, TextRect = self.text_objects_white(text, largeText)
        TextRect.center = (x, y)  # Usa os parâmetros passados ou valores padrão
        self.gameDisplay.blit(TextSurf, TextRect)
        #pygame.display.update()
    def text_objects_white(self, text, font):
        """Função auxiliar para renderizar texto."""
        textSurface = font.render(text, True, self.white)
        return textSurface, textSurface.get_rect()

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
        map3_start_time = None  # Inicializa a variável para controlar o tempo do mapa 3
        map5_start_time = None  # Inicializa a variável para controlar o tempo do mapa 5
        map6_start_time = None  # Inicializa a variável para controlar o tempo do mapa 6
        map7_start_time = None  # Inicializa a variável para controlar o tempo do mapa 7
        perseguidores = [{'x': 100, 'y': 100}, {'x': 700, 'y': 500}] #posição inicial dos perseguidores
            
        while not GameExit:

            # Calcula o tempo total decorrido
            self.elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000

            ##############################################
            # Renderiza o mapa atual
            if self.current_map == 1:
                if self.elapsed_time < 5:
                    self.gameDisplay.blit(self.intro1, (0, 0))  # Exibir primeira imagem
                elif self.elapsed_time < 10:
                    self.gameDisplay.blit(self.intro2, (0, 0))  # Exibir segunda imagem
                else:
                    Maps.mapa1()  # Exibe o mapa 1 após a introdução
                    calouroImg = self.calouroImg_frente

            ##############################################
            elif self.current_map == 2:
                if map2_start_time is None:

                    map2_start_time = pygame.time.get_ticks()  # Define o início do mapa 2
                Maps.mapa2()

                map2_elapsed_time = (pygame.time.get_ticks() - map2_start_time) / 1000 # Calcula o tempo decorrido no mapa 2

                self.message_display('ninguém chegou ainda... acho que vou descansar... ZZzzzz', 450, 50)
                calouroImg = self.calouroImg_costas

                if map2_elapsed_time > 5:
                    self.current_map = 3
            ##############################################
            elif self.current_map == 3:
                if map3_start_time is None:
                    map3_start_time = pygame.time.get_ticks()
                map3_elapsed_time = (pygame.time.get_ticks() - map3_start_time) / 1000

                if map3_elapsed_time < 5:
                    # Exibe a imagem no mapa 3
                    self.gameDisplay.blit(self.conjuntos, (0, 0))
                    x = 1000
                    y = 1000
                elif map3_elapsed_time >= 5 and map3_elapsed_time < 5.1:
                # Chama o método do mapa 3 após 8 segundos
                    Maps.mapa3_conjuntos()
                    x = 400 
                    y = 500
                    
                else:
                    #posições das portas e suas respostas em cada
                    Maps.mapa3_conjuntos()
                    calouroImg = self.calouroImg_frente
                    self.message_display('Se um conjunto A possui 1024 subconjuntos,', 400, 50)
                    self.message_display('então o tamanho de A é igual a:', 400, 70)
                    self.message_display('6', 155, 185)
                    self.message_display('7', 280, 185)
                    self.message_display('10', 505, 185)
                    self.message_display('9', 630, 185)
            ##############################################
            # Processa eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    GameExit = True
                if self.current_map != 2 and self.current_map != 7:
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

            ##############################################
            # Verifica transições de mapa
            if self.current_map == 1:
                if 345 <= x <= 400 and 555 <= y <= 600:
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
            ##############################################
            elif self.current_map == 3:
                if 74 <= y < 185:
                    if ( 106 <= x <= 166 ):
                        Maps.gameover()
                        pygame.display.update()  # Atualiza a tela para exibir o game over
                        pygame.time.wait(3000)  # Aguarda 3 segundos para o jogador ver o estado
                        # Reinicia no mapa "conjuntos"
                        self.current_map = 3
                        x, y = 400, 500  # Define as coordenadas iniciais para o mapa "conjuntos"
                        x_change, y_change = 0, 0
                    elif ( 232 <= x <= 300 ):
                        Maps.gameover()
                        pygame.display.update()  # Atualiza a tela para exibir o game over
                        pygame.time.wait(3000)  # Aguarda 3 segundos para o jogador ver o estado
                        # Reinicia no mapa "conjuntos"
                        self.current_map = 3
                        x, y = 400, 500  # Define as coordenadas iniciais para o mapa "conjuntos"
                        x_change, y_change = 0, 0
                    elif (454 <= x <= 514 ):
                        # Exibe a imagem
                        self.gameDisplay.blit(self.logica, (0, 0))
                        pygame.display.update()  # Atualiza a tela para mostrar a imagem
                        pygame.time.wait(5000)  # Aguarda 5 segundos (5000 milissegundos)
                        # Continua com as alterações do jogo
                        self.current_map = 4  # Atribui o mapa 4
                        x, y = 400, 500  # Define novas coordenadas iniciais para o mapa 4
                        x_change, y_change = 0, 0

                    elif (580 <= x <= 634 ):
                        Maps.gameover()
                        pygame.display.update()  # Atualiza a tela para exibir o game over
                        pygame.time.wait(3000)  # Aguarda 3 segundos para o jogador ver o estado
                        # Reinicia no mapa "conjuntos"
                        self.current_map = 3
                        x, y = 400, 500  # Define as coordenadas iniciais para o mapa "conjuntos"
                        x_change, y_change = 0, 0
                
                if x < 0:
                    x = 0
                elif x > self.display_width - self.calouro_width:
                    x = self.display_width - self.calouro_width
                elif y < 0:
                    y = 0
                elif y > self.display_height - self.calouro_height:
                    y = self.display_height - self.calouro_height
            ##############################################
            elif self.current_map == 4:
                Maps.mapa4_sequencias()
                    
                if 73 <= x <= 109 and 239 <= y <= 311:
                    self.message_display('A Colega diz:', 400, 50) #ao se aproximar da colega, mostrar esse texto
                    self.message_display('Tome cuidado com os veteranos frustrados e professores ruins', 400, 80)                 
                else:
                    calouroImg = self.calouroImg_frente
                    self.message_display('Qual é a negação correta da proposição p→q?', 400, 50)
                    self.message_display('p or ¬q', 175, 200)
                    self.message_display('¬p or q', 300, 200)
                    self.message_display('¬p and q', 525, 200)
                    self.message_display('p and ¬q', 650, 200)
 
                if (116 <= y <= 220):
                    if ( 139 <= x <= 193 ):
                        Maps.gameover()
                        pygame.display.update() #Atualiza a tela para exibir o game over
                        pygame.time.wait(3000)  #Aguarda 3 segundos para o jogador ver o estado
                        # Reinicia no mapa "conjuntos"
                        self.current_map = 3
                        x, y = 400, 500  # Define as coordenadas iniciais para o mapa "conjuntos"
                        x_change, y_change = 0, 0
                    elif ( 253 <= x <= 325 ):
                        Maps.gameover()
                        pygame.display.update() # Atualiza a tela para exibir o game over
                        pygame.time.wait(3000)  # Aguarda 3 segundos para o jogador ver o estado
                        # Reinicia no mapa "conjuntos"
                        self.current_map = 3
                        x, y = 400, 500  # Define as coordenadas iniciais para o mapa "conjuntos"
                        x_change, y_change = 0, 0
                    elif (478 <= x <= 544 ):
                        Maps.gameover()
                        pygame.display.update()  # Atualiza a tela para exibir o game over
                        pygame.time.wait(3000)  # Aguarda 3 segundos para o jogador ver o estado
                        # Reinicia no mapa "conjuntos"
                        self.current_map = 3
                        x, y = 400, 500  # Define as coordenadas iniciais para o mapa "conjuntos"
                        x_change, y_change = 0, 0
                    elif (607 <= x <= 673 ):
                        Maps.mapa5_logica()
                        pygame.display.update()
                        self.current_map = 5  # Atribui o mapa 5
                        x, y = 400, 500  # Define novas coordenadas iniciais para o mapa 5
                        x_change, y_change = 0, 0
                if x < 0:
                    x = 0
                elif x > self.display_width - self.calouro_width:
                    x = self.display_width - self.calouro_width
                elif y < 0:
                    y = 0
                elif y > self.display_height - self.calouro_height:
                    y = self.display_height - self.calouro_height
            ##############################################
            elif self.current_map == 5:
                Maps.mapa5_logica()
                if map5_start_time is None:
                    map5_start_time = pygame.time.get_ticks()
                map5_elapsed_time = (pygame.time.get_ticks() - map5_start_time) / 1000
                if map5_elapsed_time < 5:
                    self.gameDisplay.blit(self.pergunta3, (0, 0))
                    x = 1000
                    y = 1000
                elif map5_elapsed_time >= 5 and map5_elapsed_time < 5.1:
                # Chama o método do mapa 5 após 5 segundos
                    Maps.mapa5_logica()
                    x = 400 
                    y = 500
                    
                else:
                    #respostas nas portas e chama as funções dos perseguidores
                    Maps.mapa5_logica()
                    calouroImg = self.calouroImg_frente
                    calouro_pos = {'x': x, 'y': y}
                    self.message_display('Existe algum y tal que para todo x(x^2>y)', 400, 50)
                    self.message_display('Reais e inteiros', 185, 200, 10)
                    self.message_display('Reais positivos', 305, 200, 10)
                    self.message_display('Inteiros negativos', 535, 200, 10)
                    self.message_display('Inteiros positivos', 660, 200, 10)
                    self.perseguir_calouro(perseguidores, calouro_pos, 2)
                    for perseguidor in perseguidores:
                        self.gameDisplay.blit(self.perseguidor1_img, (perseguidor['x'], perseguidor['y']))


                if (113 <= y <= 224):
                    if ( 136 <= x <= 193 ):
                        Maps.mapa6_inducao()
                        pygame.display.update()
                        self.current_map = 6  # Atribui o mapa 6
                        x, y = 400, 500  # Define novas coordenadas iniciais para o mapa 6
                        x_change, y_change = 0, 0
                        
                    elif ( 244 <= x <= 313 ):
                        Maps.gameover()
                        pygame.display.update()  # Atualiza a tela para exibir o game over
                        pygame.time.wait(3000)   # Aguarda 3 segundos para o jogador ver o estado
                        # Reinicia no mapa "conjuntos"
                        self.current_map = 3
                        x, y = 400, 500  # Define as coordenadas iniciais para o mapa "conjuntos"
                        x_change, y_change = 0, 0
                    elif (472 <= x <= 532 ):
                        Maps.gameover()
                        pygame.display.update()  # Atualiza a tela para exibir o game over
                        pygame.time.wait(3000)   # Aguarda 3 segundos para o jogador ver o estado
                        # Reinicia no mapa "conjuntos"
                        self.current_map = 3
                        x, y = 400, 500  # Define as coordenadas iniciais para o mapa "conjuntos"
                        x_change, y_change = 0, 0
                    elif (598 <= x <= 664 ):
                        Maps.gameover()
                        pygame.display.update()  # Atualiza a tela para exibir o game over
                        pygame.time.wait(3000)   # Aguarda 3 segundos para o jogador ver o estado
                        # Reinicia no mapa "conjuntos"
                        self.current_map = 3
                        x, y = 400, 500  # Define as coordenadas iniciais para o mapa "conjuntos"
                        x_change, y_change = 0, 0
                        
                if x < 0:
                    x = 0
                elif x > self.display_width - self.calouro_width:
                    x = self.display_width - self.calouro_width
                elif y < 0:
                    y = 0
                elif y > self.display_height - self.calouro_height:
                    y = self.display_height - self.calouro_height
            ##############################################
            elif self.current_map == 6:
                Maps.mapa6_inducao()
                if map6_start_time is None:
                    map6_start_time = pygame.time.get_ticks()
                map6_elapsed_time = (pygame.time.get_ticks() - map6_start_time) / 1000
                if map6_elapsed_time < 5:
                    self.gameDisplay.blit(self.pergunta4, (0, 0))
                    x = 1000
                    y = 1000
                elif map6_elapsed_time >= 5 and map6_elapsed_time < 5.1:
                # Chama o método do mapa 6 após 8 segundos
                    Maps.mapa6_inducao()
                    x = 400 
                    y = 500
                    
                else:
                    Maps.mapa5_logica()
                    calouroImg = self.calouroImg_frente
                    self.message_display('Para m um inteiro positivo, 4m+2 é múltiplo de', 400, 70)
                    self.message_display('6', 175, 200)
                    self.message_display('2', 300, 200)
                    self.message_display('3', 525, 200)
                    self.message_display('5', 650, 200)
                    
                if (113 <= y <= 224):
                    if ( 136 <= x <= 193 ):
                        Maps.gameover()
                        pygame.display.update()  # Atualiza a tela para exibir o game over
                        pygame.time.wait(3000)   # Aguarda 3 segundos para o jogador ver o estado
                        # Reinicia no mapa "conjuntos"
                        self.current_map = 3
                        x, y = 400, 500  # Define as coordenadas iniciais para o mapa "conjuntos"
                        x_change, y_change = 0, 0
                        
                    elif ( 244 <= x <= 313 ):
                        
                        Maps.mapa2()
                        pygame.display.update()
                        self.current_map = 7  # Atribui o mapa 7
                        x, y = 400, 500  # Define novas coordenadas iniciais para o mapa 4
                        x_change, y_change = 0, 0
                    elif (472 <= x <= 532 ):
                        Maps.gameover()
                        pygame.display.update()  # Atualiza a tela para exibir o game over
                        pygame.time.wait(3000)   # Aguarda 3 segundos para o jogador ver o estado
                        # Reinicia no mapa "conjuntos"
                        self.current_map = 3
                        x, y = 400, 500  # Define as coordenadas iniciais para o mapa "conjuntos"
                        x_change, y_change = 0, 0
                    elif (598 <= x <= 664 ):
                        Maps.gameover()
                        pygame.display.update()  # Atualiza a tela para exibir o game over
                        pygame.time.wait(3000)   # Aguarda 3 segundos para o jogador ver o estado
                        # Reinicia no mapa "conjuntos"
                        self.current_map = 3
                        x, y = 400, 500  # Define as coordenadas iniciais para o mapa "conjuntos"
                        x_change, y_change = 0, 0
                if x < 0:
                    x = 0
                elif x > self.display_width - self.calouro_width:
                    x = self.display_width - self.calouro_width
                elif y < 0:
                    y = 0
                elif y > self.display_height - self.calouro_height:
                    y = self.display_height - self.calouro_height
            ##############################################
            elif self.current_map == 7:
                if map7_start_time is None:
                    map7_start_time = pygame.time.get_ticks()
                map7_elapsed_time = (pygame.time.get_ticks() - map7_start_time) / 1000

                if map7_elapsed_time > 5:
                    # Exibe a imagem no mapa 7
                    self.gameDisplay.fill((0, 0, 0))  # Preenche a tela com a cor preta
                    self.message_display_white('Obrigada por jogar!', 400, 300)
                    self.message_display_white('FIM', 400, 350)
                    x, y = 1000, 10000 

                else:
                    Maps.mapa2()
                    calouroImg = self.calouroImg_costas
                    self.message_display('EU GANHEI O QUIZ! Mas todo mundo já foi embora...', 450, 50)
                    self.message_display('ainda perdi o chocolate por dormir demais... espero que eu vá bem amanhã...', 400, 70)
                
            if self.elapsed_time >= 10:  
                calouro(x, y, calouroImg)
            # Atualiza o display e controla o FPS
            pygame.display.update()
            self.clock.tick(60)
        pygame.quit()
        quit()
