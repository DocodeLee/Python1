class Settings:
    """ A class to store all settings for Alien Invasion"""
    
    def __init__(self):
        """Initialize the games's settings"""
        #Screen settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (159, 252, 181)
        
        #Ships settings
        
        self.ship_limit = 3
        
        # Bullet settings
        
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        #Alien settings
        
        self.fleet_drop_speed = 6
        
        # How quickly the game speed up
        self.speedup_scale = 1.1
        
        #point value up
        self.score_scale = 1.5
        
        self.initialize_dynamic_settings()
        
    def initialize_dynamic_settings(self):
        """ Initialize settings that change throughout the game"""
        self.ship_speed = 1.3
        self.bullet_speed = 1.0
        self.alien_speed = 0.51
        # direction 1 is right -1 is left
        self.fleet_direction = 1
        
        #Scoring
        self.alien_points = 10
        
    def increase_speed(self):
        """Increase speed"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        