import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    """A class to manage ship"""
    
    def __init__(self,ai_game):
        """ Initialize the ship and set its starting"""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        ## treat game elements like rectangle
        
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/air-force-2026819_960_720.png')
        self.image = pygame.transform.scale(self.image,(25,50))
        self.rect = self.image.get_rect()
        ## give a image rectangule to place
        
        #Start each New ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        #Store a demical value for the ship's horizontal position
        self.x = float(self.rect.x)
        
        #Movement flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """Update the ship's position based on the movement"""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
             self.x -= self.settings.ship_speed
        #Update rect from self.x
        self.rect.x = self.x
    def blitme(self):
        """Draw the ship at its current position"""
        self.screen.blit(self.image,self.rect)
        
    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)