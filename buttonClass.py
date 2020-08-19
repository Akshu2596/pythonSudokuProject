import pygame


class Button:
    def __init__(self, x, y, width, height, color=(255, 135, 133), text=None, highlighted_color=(255, 203, 66),
                 functions=None, params=None
                 ):
        self.image = pygame.Surface((width, height))
        self.pos = (x, y)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.color = color
        self.text = text
        self.highlighted_color = highlighted_color
        self.functions = functions
        self.params = params
        self.highlighted = False

    def update(self, mouse):
        if self.rect.collidepoint(mouse):
            self.highlighted = True
        else:
            self.highlighted = False

    def draw(self, window):
        self.image.fill(self.highlighted_color if self.highlighted else self.color)
        window.blit(self.image, self.pos)
