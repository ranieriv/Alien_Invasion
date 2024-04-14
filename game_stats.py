class GameStats:
    """ Tracks statistics for Alien Invasion."""
    
    def __init__(self, ai_game):
        """ Initialize Statistics."""
        self.settings = ai_game.settings
        self.reset_stats()
        
        #Start Alien invasion in an inactive state.
        self.game_active = False
        
        # High score shoiuld never be reset.
        self.high_score = 0
        with open("highscore.txt", "r") as file: 
            content = file.read()
            try:
                self.high_score = float(content)
            except ValueError:
                print("Falha em resgatar o high score")
                
            
        
    def reset_stats(self):
        """ Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1