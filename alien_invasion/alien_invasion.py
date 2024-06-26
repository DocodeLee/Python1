import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ships import Ship
from bullets import Bullet
from alien import Alien
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        
        # self.screen  is called as surface
        # self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        ## upline is for window-mode
        ## ---- FUll screen
        self.screen = pygame.display.set_mode((800, 600))
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        #create an instance to store game statistics and scoreboard
        # create an instance to store game statistics.
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        
        ##define the ship
        self.ship = Ship(self)
        self._create_fleet()
        
        # Set the background color
        self.bg_color = (159, 252, 181)
        
        #Make the play button
        self.play_button = Button(self, "Play")
        
    def _create_fleet(self):
        """Create the fleet of the aliens"""
        # Create an alien and find the number of aliens
        # Spacing between each alien is equal to one alien width
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        
        #Determine the number of rows of alien that fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (2 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        # Create the first row of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
            #Create an alien and place it in the row
                self._create_alien(alien_number, row_number)
            
    def _create_alien(self,alien_number,row_number):
        alien = Alien(self)
        alien_width, alien_height= alien.rect.size
        
        alien.x = alien_width + 2 * alien_number * alien_width
        alien.rect.x = alien.x
        alien.rect.y =alien.rect.height + 2 * row_number * alien_width
        self.aliens.add(alien)
    
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1
            
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
        
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
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                
    def _check_play_button(self,mouse_pos):
        """Start a new game when the player click"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            #Reset the game settings
            self.settings.initialize_dynamic_settings()
            #Reset the game stats
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            ## get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()
            
            #Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            #Hide the cursor
            pygame.mouse.set_visible(False)
            
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
        
        self._check_bullet_alien_collision()
        
    def _check_bullet_alien_collision(self):
        #check for any bullets that have hit aliens
        # if so get rid of the bullet and alien.
        collisons = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        
        if collisons:
            for aliens in collisons.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
            
        if not self.aliens:
            #Destroy exisiting bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            
            #Increase level
            self.stats.level += 1
            self.sb.prep_level()
        
            
    def _ship_hit(self):
        """Respond to the ship being hit by an alien"""
        if self.stats.ships_left > 0:
            #Decrement ships left
            self.stats.ships_left -= 1
            self.sb.prep_ships()
        
            # Gid rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()
        
            #Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
        
            #Pause
            sleep(0.5)
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)
        
    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                #Treat this the same as if the ship got hit
                self._ship_hit()
                break
            
            
    def _update_aliens(self):
        """check edge and set the position"""
        self._check_fleet_edges()
        self.aliens.update()
        
        # Look for alien-ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
           self._ship_hit()
           
        #Look for aliens hitting the bottom
        self._check_aliens_bottom()
        

    def _update_screen(self):
        """Update images on thes screen, and flip to the new screen"""
        #Redraw the screen  
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        
        #Draw the score information
        self.sb.show_score()
        #Make the most recently drawn screen visible: 
        # continuously update the game info
        
        
        #Draw the play button if the game is inactive.
        if not self.stats.game_active:
            self.play_button.draw_button()
        pygame.display.flip()
        
    
            
if __name__ == "__main__":
    #Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
    