import pygame
import os
import jogo

class Menu(jogo.Jogo):  # Menu herda de Jogo
    
    def game_intro(self):
        pygame.init()
        intro = True

        # Cores
        red = (200, 0, 0)
        green = (0, 200, 0)
        bright_red = (255, 0, 0)
        bright_green = (0, 255, 0)

        clock = pygame.time.Clock()

        # Carrega a imagem de fundo uma vez
        self.background = pygame.image.load(os.path.join('assets', 'background_cinza.png'))
        game_title = "Layers of Discrete Mathematics"
        title_font = pygame.font.Font("freesansbold.ttf", 40)

        def button(msg, x, y, w, h, inacColor, actColor, action=None):
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()

            # Verifica se o mouse está sobre o botão
            if x + w > mouse[0] > x and y + h > mouse[1] > y:
                pygame.draw.rect(self.gameDisplay, actColor, (x, y, w, h))
                # Verifica clique
                if click[0] == 1 and action is not None:
                    action()
            else:
                pygame.draw.rect(self.gameDisplay, inacColor, (x, y, w, h))
            
            # Renderiza o texto do botão
            smallText = pygame.font.Font("freesansbold.ttf", 20)
            textSurf, textRect = self.text_objects(msg, smallText)
            textRect.center = ((x + (w / 2)), (y + (h / 2)))
            self.gameDisplay.blit(textSurf, textRect)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:  # Pressione Enter para começar
                        intro = False
                    elif event.key == pygame.K_q:  # Pressione Q para sair
                        pygame.quit()
                        quit()

            # Desenha o fundo
            self.gameDisplay.blit(self.background, (0, 0))

            # Renderiza o título do jogo no centro da tela
            title_surface = title_font.render(game_title, True, (0, 0, 0))
            title_rect = title_surface.get_rect(center=(self.gameDisplay.get_width() / 2, (self.gameDisplay.get_height() / 3)+20))
            self.gameDisplay.blit(title_surface, title_rect)

            # Adiciona botões
            button("Start", 150, 450, 100, 50, green, bright_green, self.openGame)
            button("Quit", 550, 450, 100, 50, red, bright_red, pygame.quit)

            pygame.display.update()
            clock.tick(15)

    def text_objects(self, text, font):
        """Helper para renderizar texto"""
        textSurface = font.render(text, True, (0, 0, 0))
        return textSurface, textSurface.get_rect()
