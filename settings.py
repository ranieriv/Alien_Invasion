class Settings:
    """A class to store all settings for Alien Invasion"""
    
    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Framerate
        self.framerate = 240
        
        # Ship settings
        self.ship_limit = 3
        
        # Bullet settings
        self.bullet_width = 3000 # Original = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3
        
        # Aliens settings
        self.fleet_drop_speed = 100 # original = 
        
        # How quick the game speeds up
        self.speedup_scale = 1.1
        
        # How quick the alien points value increase
        self.score_scale = 1.5
        
        # Base dynamic Settings
        self.base_ship_speed = 1.5
        self.base_bullet_speed = 3.0
        self.base_alien_speed = 1
        self.base_alien_points = 50
        self.level = 1
        
        
        self.initialize_dynamic_settings()

        
    def initialize_dynamic_settings(self):
        """ Initialize settings that change throughout the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        
        # Scoring
        self.alien_points = 50
        
    def level_up(self):
        self.level += 1
        print(f"Leval UP! Level: {self.level}")
        self.update_speed()

    def update_speed(self):
        """ Increase speed settings. """
        self.ship_speed = self.base_ship_speed * (self.speedup_scale ** self.level)
        self.bullet_speed = self.base_bullet_speed * (self.speedup_scale ** self.level)
        self.alien_speed = self.base_alien_speed * (self.speedup_scale ** self.level)
        self.alien_points = self.base_alien_points * (self.score_scale ** self.level)
        print(f"""
ship_speed   = {self.ship_speed}
bullet_speed = {self.bullet_speed}
alien_speed  = {self.alien_speed }
alien_points = {self.alien_points}
              """)

        
