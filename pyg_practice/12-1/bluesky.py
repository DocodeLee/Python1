import sys
import pygame

class Bluesky:
    """Overall class to manage game assets and behavior"""
    
    def __init__(self):
        """Initialize the game and create game resources"""
        pygame.init()
        ##Setting the background color
        self.bg_color = (130, 218, 245)
        
        self. screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Blue Sky")
        
    def run_game(self):
        """Start the main loop for the game"""
        while True:
            #Watch for keyboard and mouse events:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            #Redraw the screen during loop
            self.screen.fill(self.bg_color)
            #Make the most recently drawn screen
            pygame.display.flip()

if __name__ == "__main__":
    #Make a game instance and run
    blue = Bluesky()
    blue.run_game()
