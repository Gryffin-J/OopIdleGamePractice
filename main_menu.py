from ui_elements import button, background
from assets import images

class MainMenu:
    def __init__(self, draw_location):

        self.draw_location = draw_location
    
        self.fungButton = button(images["fung"], 600, 360, 0.5, 0.5, None, True)
        self.mainBackground = background(images["main_menu_background"], 50, 30, 1.5, 1.5, True)
        self.playButton = button(images["play_button"], 300, 200, 0.3, 0.3, None, True)
        
    def load_main_menu(self):
        self.mainBackground.draw(self.draw_location)

        self.fungButton.handle_event()
        self.fungButton.draw(self.draw_location)

        self.playButton.handle_event()
        self.playButton.draw(self.draw_location)

