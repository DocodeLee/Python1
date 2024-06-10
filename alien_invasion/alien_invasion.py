import sys
import pygame
from settings import Settings   
from ships import Ship
from bullets import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.bullets = pygame.sprite.Group()
        
        # self.screen  is called as surface
        # self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        ## upline is for window-mode
        ## ---- FUll screen
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        ##define the ship
        self.ship = Ship(self)
        
        # Set the background color
        self.bg_color = (159, 252, 181)
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            
            
            
            
            
    def _check_events(self):
        """Respond to keypress and mouse"""
         # keyboard and mouse events
        for event in pygame.event.get():
                #event is action that player  perfoms while playing game
                # pygame.event.get() : returns a list of events that have taken place
            if event.type == pygame.QUIT:
                    #when player click close pygame.QUIT event is detected and call sys.exit()
                sys.exit()
            ##From here it gets the movement
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    def _check_keyup_events(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False
    
    def _fire_bullet(self):
        """create a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
        #pygame use add instead of append
    
    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets"""
        #Update bullet positions.
        self.bullets.update()
        ## Deleting the bullets that have disappeared
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)
        

    def _update_screen(self):
        """Update images on thes screen, and flip to the new screen"""
        #Redraw the screen  
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #Make the most recently drawn screen visible: 
        # continuously update the game info
        pygame.display.flip()
if __name__ == "__main__":
    #Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
    