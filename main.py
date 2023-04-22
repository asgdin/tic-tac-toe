import pygame

pygame.init()
screen = pygame.display.set_mode([1200, 1200])
#rects
square1ch = True
square2ch = True
square3ch = True
square4ch = True
square5ch = True
square6ch = True
square7ch = True
square8ch = True
square9ch = True

x_or_o = 0
def click_square():
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()[0]
    #rects

    square1 = pygame.Rect(0, 0, 400, 400)
    square2 = pygame.Rect(400, 0, 400, 400)
    square3 = pygame.Rect(800, 0, 400, 400)
    square4 = pygame.Rect(0, 400, 400, 400)
    square5 = pygame.Rect(400, 400, 400, 400)
    square6 = pygame.Rect(800, 400, 400, 400)
    square7 = pygame.Rect(0, 800, 400, 400)
    square8 = pygame.Rect(400, 800, 400, 400)
    square9 = pygame.Rect(800, 800, 400, 400)
    global square1ch

    if click:
        if square1.collidepoint(mouse_pos) and square1ch:
            X_or_o(0, 0)
            square1ch = False

def X_or_o(x, y):
    global x_or_o
    if x_or_o % 2 == 0:
        pygame.draw.line(screen,'white', [x + 100, y + 100], [x + 200, y + 200], 10)
        pygame.draw.line(screen, 'white', [x + 200, y + 100], [x + 100, y + 200], 10)
        x_or_o += 1
    else:
        pygame.draw.circle(screen, 'white', [x + 200, y + 200], 100, 10)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        # lines
        click_square()
        pygame.draw.rect(screen, 'white', (395,0, 10, 1200))
        pygame.draw.rect(screen, 'white', (795, 0, 10, 1200))
        pygame.draw.rect(screen, 'white', (0, 395, 1200, 10))
        pygame.draw.rect(screen, 'white', (0, 795, 1200, 10))




    pygame.display.flip()
pygame.quit()
