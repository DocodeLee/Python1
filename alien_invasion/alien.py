import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A calss for Alien"""
    def __init__(self,ai_game):
        """initilaize alien and position setting"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        #Load the alien image and set rect
        self.image = pygame.image.load('images/alien-1295828_960_720.png')
        self.image = pygame.transform.scale(self.image,(30, 40))
        self.rect = self.image.get_rect()
        
        ## new alien starts on the top left side
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
    
    def check_edges(self):
        """Return True if alien is at edge of screen"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
        
        #store the alien's exact horizontal position
        self.x = float(self.rect.x)
    def update(self):
        """Move the alien to the right"""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
    