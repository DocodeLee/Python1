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
        self.image = pygame.transform.rotate(self.image,270)
        self.rect = self.image.get_rect()
        
        #start each new ship at  center
        new_x = self.screen_rect.left + self.rect.width / 2
        self.rect.center = (new_x,self.screen_rect.center[1])
        
        
        self.moving_up = False
        self.moving_down = False
    
    def center_ship(self):
        """Center the ship on the screen"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        
    def update(self):
        """Update the ship's position"""
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= 2
        if self.moving_down and self.rect.bottom < self.screen.get_rect().bottom:
            self.rect.y += 2
        
    def blitme(self):
        """Draw the ship at its current position"""
        self.screen.blit(self.image,self.rect)