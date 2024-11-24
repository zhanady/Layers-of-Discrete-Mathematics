import pygame
import os
import jogo

class Menu(jogo.Jogo):  # Menu herda de Jogo
    
    def game_intro(self):
        pygame.init()
        intro = True

        clock = pygame.time.Clock()  # Inicializa o clock para controlar FPS

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:  # Permitir sair do menu pressionando uma tecla
                    if event.key == pygame.K_RETURN:  # Pressione Enter para começar o jogo
                        intro = False
                    elif event.key == pygame.K_q:  # Pressione Q para sair
                        pygame.quit()
                        quit()

            self.gameDisplay.fill(self.white)

            # Texto do menu
            largeText = pygame.font.Font('freesansbold.ttf', 40)
            TextSurf, TextRect = self.text_objects("Layers of Discrete Mathematics", largeText)
            TextRect.center = ((self.display_width / 2), (self.display_height / 2 - 50))
            self.gameDisplay.blit(TextSurf, TextRect)

            # Texto de instruções
            smallText = pygame.font.Font('freesansbold.ttf', 20)
            TextSurf, TextRect = self.text_objects("Press ENTER to Start or Q to Quit", smallText)
            TextRect.center = ((self.display_width / 2), (self.display_height / 2 + 50))
            self.gameDisplay.blit(TextSurf, TextRect)

            

            pygame.display.update()
            clock.tick(15)

        # Quando sair do menu, começa o jogo
        self.openGame()
