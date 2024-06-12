class GameStats:
    """Track situation for alien invasion"""
    
    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()
        #start alien invasion in active state
        self.game_active = True
        
        #Start game in an inactive state.abs
        self.game_active = False
        
        #High score never reset
        self.high_score = 0
        self.level = 1
    
    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0