import pygame

pygame.init()
screen = pygame.display.set_mode([1200, 1200])


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def draw(self):
        button_rect = pygame.rect.Rect((self.x, self.y), (400, 400))

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        pygame.draw.rect(screen, 'white', (395,0, 10, 1200))
        pygame.draw.rect(screen, 'white', (795, 0, 10, 1200))
        pygame.draw.rect(screen, 'white', (0, 395, 1200, 10))
        pygame.draw.rect(screen, 'white', (0, 795, 1200, 10))
    pygame.display.flip()
pygame.quit()
