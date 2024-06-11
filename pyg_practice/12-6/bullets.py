import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets field from the ship"""
    def __init__(self,blue_game):
        """Create a bullet object at the ship's current position"""
        super().__init__()
        self.screen = blue_game.screen
        self.bullet_color = (60, 60, 60)
        
        # Create a bullet rect at (0,0) and then set correct position
        self.rect = pygame.Rect(0, 0, 15, 3)
        self.rect.midright = blue_game.ship.rect.midright
        
        self.x = float(self.rect.x)
    def update(self):
        self.x += 1
        self.rect.x = self.x
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)
        