import pygame

class button:
    def __init__(self, sprite, xPos, yPos, xScale, yScale, action, is_visible ):
        self.sprite = sprite
        self.xPos = xPos
        self.yPos = yPos
        self.xScale = xScale
        self.yScale = yScale
        self.action = action
        self.is_visible = is_visible

        # Configuration of the button sprite for when the mouse is not hovering over it
        normal_width = int(self.sprite.get_width() * self.xScale)
        normal_height = int(self.sprite.get_height() * self.yScale)
        
        self.normal_sprite = pygame.transform.scale(self.sprite, (normal_width, normal_height))

        self.rect = self.normal_sprite.get_rect(topleft = (xPos, yPos))

        # Configuration of the button sprite for when the mouse is hovering over it. Slightly bigger, keeps rect size but centers it so it grows evenly.
        hovered_width = int(normal_width*1.1)
        hovered_height = int(normal_height*1.1)

        self.hovered_sprite = pygame.transform.scale(self.sprite, (hovered_width, hovered_height))

        self.centered_rect = self.hovered_sprite.get_rect(center = self.rect.center)

    def draw(self, surface):
        if self.is_visible:
            if self.is_hovered:
                surface.blit(self.hovered_sprite, self.centered_rect)
            else:
                surface.blit(self.normal_sprite, self.rect) 

    def handle_event(self):
        mouse_pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(mouse_pos):
            self.is_hovered = True
        else:
            self.is_hovered = False