import pygame

pygame.init()
screen = pygame.display.set_mode([1200, 1200])

#avaivability checks
sq1ch = True
sq2ch = True
sq3ch = True
sq4ch = True
sq5ch = True
sq6ch = True
sq7ch = True
sq8ch = True
sq9ch = True

x_or_o = 0
def click_square():
    mouse_pos = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()[0]
    #rects
    sq1 = pygame.Rect(0, 0, 400, 400)
    sq2 = pygame.Rect(400, 0, 400, 400)
    sq3 = pygame.Rect(800, 0, 400, 400)
    sq4 = pygame.Rect(0, 400, 400, 400)
    sq5 = pygame.Rect(400, 400, 400, 400)
    sq6 = pygame.Rect(800, 400, 400, 400)
    sq7  =pygame.Rect(0, 800, 400, 400)
    sq8 = pygame.Rect(400, 800, 400, 400)
    sq9 = pygame.Rect(800, 800, 400, 400)
    global sq1ch
    global sq2ch
    global sq3ch
    global sq4ch
    global sq5ch
    global sq6ch
    global sq7ch
    global sq8ch
    global sq9ch

    if click:
        if sq1.collidepoint(mouse_pos) and sq1ch:
            X_or_o(0, 0)
            sq1ch = False
        if sq2.collidepoint(mouse_pos) and sq2ch:
            X_or_o(400, 0)
            sq2ch = False
        if sq3.collidepoint(mouse_pos) and sq3ch:
            X_or_o(800, 0)
            sq3ch = False
        if sq4.collidepoint(mouse_pos) and sq4ch:
            X_or_o(0, 400)
            sq4ch = False
        if sq5.collidepoint(mouse_pos) and sq5ch:
            X_or_o(400, 400)
            sq5ch = False
        if sq6.collidepoint(mouse_pos) and sq6ch:
            X_or_o(800, 400)
            sq6ch = False
        if sq7.collidepoint(mouse_pos) and sq7ch:
            X_or_o(0, 800)
            sq7ch = False
        if sq8.collidepoint(mouse_pos) and sq8ch:
            X_or_o(400, 800)
            sq8ch = False
        if sq9.collidepoint(mouse_pos) and sq9ch:
            X_or_o(800, 800)
            sq9ch = False
def X_or_o(x, y):
    global x_or_o
    if x_or_o % 2 == 0:
        pygame.draw.line(screen,'white', [x + 100, y + 100], [x + 200, y + 200], 10)
        pygame.draw.line(screen, 'white', [x + 200, y + 100], [x + 100, y + 200], 10)
        x_or_o += 1
    else:
        pygame.draw.circle(screen, 'white', [x + 200, y + 200], 100, 10)
        x_or_o += 1
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
