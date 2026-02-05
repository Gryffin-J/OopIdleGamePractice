from ui_elements import button, background
from assets import images
import pygame

class MainMenu:
    def __init__(self, draw_location):

        self.draw_location = draw_location
    
        self.fungButton = button(images["fung"], 600, 360, 0.5, 0.5, None, True)
        self.mainBackground = background(images["main_menu_background"], 50, 30, 1.5, 1.5, True)
        
    def load_main_menu(self):
        self.mainBackground.draw(self.draw_location)

        self.fungButton.handle_event()
        self.fungButton.draw(self.draw_location)
