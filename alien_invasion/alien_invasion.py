import sys
import pygame

class AlienInvasion:
    """Overall class to manage game assets and behavior"""
    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        
        # self.screen  = surface
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")
        
        # Set the background color
        self.bg_color = (159, 252, 181)
        
    def run_game(self):
        """Start the main loop for the game."""
        while True:
            # keyboard and mouse events
            for event in pygame.event.get():
                #event is action that player  perfoms while playing game
                # pygame.event.get() : returns a list of events that have taken place
                if event.type == pygame.QUIT:
                    #when player click close pygame.QUIT event is detected and call sys.exit()
                    sys.exit()
            #Redraw the screen
            self.screen.fill(self.bg_color)
            #Make the most recently drawn screen visible: continuously update the game info
            pygame.display.flip()
if __name == "__main__":
    #Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()