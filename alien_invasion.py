import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    """ Overall class to manage game assets and behaviour"""
    def __init__(self):

        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)

    def run_game(self):
        while True:     # start the loop for the Game
            for event in pygame.event.get():  #watch for keyboard and mouse event
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.bg_color)#redraw the screen during each pass through the loop
            self.ship.blitme()
            pygame.display.flip()# Make the most recent drawn screen visible


if __name__ == '__main__':
    ai = AlienInvasion()        # Make a game instance and run the Game.
    ai.run_game()
