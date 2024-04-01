import pygame.font

class Button:
    
    def __init__(self, ai_game, msg, type):
        """ Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        # Set the colors and properties of the button.
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # Get the divergent buttons
        # Build the buttons's dimensions, rect and position it
        if type == "play":
                self.width, self.height = 200, 50
                self.rect = pygame.Rect (0,0, self.width, self.height)
                self.rect.center = self.screen_rect.center
        if type == "plus":
                self.width, self.height = 50, 50
                self.rect = pygame.Rect (0,0, self.width, self.height)
                self.rect.midright = self.screen_rect.midright
                self.rect.centery = self.screen_rect.centery
        if type == "minus":
                self.width, self.height = 50, 50
                self.rect = pygame.Rect (0,0, self.width, self.height)
                self.rect.midleft = self.screen_rect.midleft
                self.rect.centery = self.screen_rect.centery

        
        # The button message needs to be prepped only once.
        self._prep_msg(msg)
        
    def _prep_msg(self, msg):
        """ Turn msg into a rendered image and cener text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
    