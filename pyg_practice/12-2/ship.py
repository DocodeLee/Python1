import pygame

class Ship:
    """Class to manage the ship"""
    def __init__(self, blue_game):
        """Initialize the ship and set its starting position"""
        self.screen = blue_game.screen
        self.screen_rect = blue_game.screen.get_rect()
        
        ##Load the ship image
        self.image = pygame.image.load('images/air-force-2026819_960_720.png')
        self.image = pygame.transform.scale(self.image,(100,150))
        self.rect = self.image.get_rect()
        
        #start each new ship at  center
        self.rect.center = self.screen_rect.center
        
    def blitme(self):
        """Draw the ship at its current position"""
        self.screen.blit(self.image,self.rect)