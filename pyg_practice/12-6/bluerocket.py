import sys
import pygame
from ship import Ship
from bullets import Bullet

class Bluesky:
    """Overall class to manage game assets and behavior"""
    
    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        ##Setting the background color
        self.bg_color = (130, 218, 245)
        
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Blue Sky")
        
        ## part of ship
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #Watch for keyboard and mouse events:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self._update_bullets()
            
    
    def _update_bullets(self):
        self.bullets.update()
            
            #get rid of the bullets
        for bullet in self.bullets.copy():
            if bullet.rect.right > self.screen.get_rect().right:
                self.bullets.remove(bullet)
                       
            
            
    def _check_events(self):
        """Respond to the keypress and mouse"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                if event.key == pygame.K_UP:
                    self.ship.moving_up = True
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = True
                elif event.key == pygame.K_SPACE:
                    self._fire_bullet() 
            
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
                if event.key == pygame.K_UP:
                    self.ship.moving_up = False
                if event.key == pygame.K_DOWN:
                    self.ship.moving_down = False 
            
    def _fire_bullet(self):
        if len(self.bullets)< 3:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_screen(self):
        #Redraw the screen during loop
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #Make the most recently drawn screen
        pygame.display.flip()

if __name__ == "__main__":
    #Make a game instance and run
    blue = Bluesky()
    blue.run_game()
