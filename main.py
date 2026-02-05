import pygame
from ui_elements import button

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

fung = pygame.image.load("Screenshot 2025-07-14 215351.png")
fungButton = button(fung, 600, 360, 0.5, 0.5, None, True)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")
    fungButton.handle_event()
    fungButton.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()