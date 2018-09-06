import sys

import pygame

def run_game():
        pygame.init()
        screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

        #Set the background colour.
        bg_colour = (230, 230, 230)

        # Start the main loop for the game.
        while True:
            #Watch for keyboard and mouse events
            screen.fill(bg_colour)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()

run_game()