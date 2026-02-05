import pygame

pygame.display.set_mode((1, 1), pygame.HIDDEN)

images = {
    "fung" : pygame.image.load("Screenshot 2025-07-14 215351.png").convert_alpha(),
    "main_menu_background" : pygame.image.load("Screenshot 2026-02-05 092914.png").convert_alpha(),
    "play_button" : pygame.image.load("playButton.png").convert_alpha(),
}