import pygame
from ui_elements import button, background
from assets import images
from main_menu import MainMenu

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

menu = MainMenu(screen)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    menu.load_main_menu()

    pygame.display.flip()

    clock.tick(60)

pygame.quit()