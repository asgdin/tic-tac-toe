import pygame

pygame.init()
screen = pygame.display.set_mode([1200, 1200])

font = pygame.font.Font('freesansbold.ttf', 70)
x = []
o = []
x_or_o = 0
#if winner = false x wins
winner = False
sq1ch = True
sq2ch = True
sq3ch = True
sq4ch = True
sq5ch = True
sq6ch = True
sq7ch = True
sq8ch = True
sq9ch = True
class Button(pygame.sprite.Sprite):
    def __init__(self, text, x, y, button_size):
        super().__init__()
        self.text = text
        self.x = x
        self.y = y
        self.button_size = button_size
        if self.button_size == 1:
            self.button_size = (200, 100)
        self.draw()

    def draw(self):

        button_text = font.render(self.text, True, 'Black')
        buttonrect = pygame.rect.Rect((self.x, self.y), self.button_size)
        pygame.draw.rect(screen, 'gray', buttonrect, 0, 5)
        pygame.draw.rect(screen, 'black', buttonrect, 2, 5)
        screen.blit(button_text, (self.x + 10, self.y + 10))

    def click(self):
        mouse_pos = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()[0]
        buttonrect = pygame.rect.Rect((self.x, self.y), (self.button_size))
        if click and buttonrect.collidepoint(mouse_pos):
            return True

        else:
            return False
def win_screen():
    screen.fill('black')
    global x_or_o
    global x
    global o
    global winner
    global sq1ch
    global sq2ch
    global sq3ch
    global sq4ch
    global sq5ch
    global sq6ch
    global sq7ch
    global sq8ch
    global sq9ch
    global sq1
    global sq2
    global sq3
    global sq4
    global sq5
    global sq6
    global sq7
    global sq8
    global sq9
    winner = False
    sq1ch = True
    sq2ch = True
    sq3ch = True
    sq4ch = True
    sq5ch = True
    sq6ch = True
    sq7ch = True
    sq8ch = True
    sq9ch = True
    x = []
    o = []
    x_or_o = 0
    while True:



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            play_button = Button('Play Again', 600, 400, (400,100))
            quit_button = Button('quit', 600, 600, (400, 100))
            if play_button.click():
                Game()
            if quit_button.click():
                pygame.quit()
        pygame.display.flip()

def Game():
    screen.fill('black')


    # avaivability checks


    sq1 = pygame.Rect(0, 0, 400, 400)
    sq2 = pygame.Rect(400, 0, 400, 400)
    sq3 = pygame.Rect(800, 0, 400, 400)
    sq4 = pygame.Rect(0, 400, 400, 400)
    sq5 = pygame.Rect(400, 400, 400, 400)
    sq6 = pygame.Rect(800, 400, 400, 400)
    sq7 = pygame.Rect(0, 800, 400, 400)
    sq8 = pygame.Rect(400, 800, 400, 400)
    sq9 = pygame.Rect(800, 800, 400, 400)
    x_or_o = 0


    while True:
        def win():
            global  winner
            global sq1ch
            global sq2ch
            global sq3ch
            global sq4ch
            global sq5ch
            global sq6ch
            global sq7ch
            global sq8ch
            global sq9ch
            global sq1
            global sq2
            global sq3
            global sq4
            global sq5
            global sq6
            global sq7
            global sq8
            global sq9
            c1 = [1, 2, 3]
            if set(c1).issubset(o):
                winner = True
                win_screen()
            if set(c1).issubset(x):
                print(' x won')
            c2 =[4, 5, 6]
            if set(c2).issubset(o):
                winner = True
                win_screen()
            if set(c2).issubset(x):
                winner = False
                win_screen()
            c3 = [7, 8, 9]
            if set(c3).issubset(o):
                winner = True
                win_screen()
            if set(c3).issubset(x):
                winner = False
                win_screen()
            c5 = [1, 5, 9]
            if set(c5).issubset(o):
                winner = True
                win_screen()
            if set(c5).issubset(x):
                winner = False
                win_screen()
            c6 = [3, 5, 7]
            if set(c6).issubset(o):
                winner = True
                win_screen()
            if set(c6).issubset(x):
                winner = False
                win_screen()
            c7 = [1, 4, 7]
            if set(c7).issubset(o):
                winner = True
                win_screen()
            if set(c7).issubset(x):
                winner = False
                win_screen()
            c8 = [2, 5, 8]
            if set(c8).issubset(x):
                winner = True
                win_screen()
            if set(c8).issubset(x):
                winner = False
                win_screen()
            c9 = [3, 6, 9]
            if set(c9).issubset(o):
                winner = True
                win_screen()
            if set(c9).issubset(x):
                winner = False
                win_screen()
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
                    if x_or_o % 2 == 0:
                        o.append(1)
                    else:
                        x.append(1)

                if sq2.collidepoint(mouse_pos) and sq2ch:
                    X_or_o(400, 0)
                    sq2ch = False
                    if x_or_o % 2 == 0:
                        o.append(2)
                    else:
                        x.append(2)
                if sq3.collidepoint(mouse_pos) and sq3ch:
                    X_or_o(800, 0)
                    sq3ch = False
                    if x_or_o % 2 == 0:
                        o.append(3)
                    else:
                        x.append(3)
                if sq4.collidepoint(mouse_pos) and sq4ch:
                    X_or_o(0, 400)
                    sq4ch = False
                    if x_or_o % 2 == 0:
                        o.append(4)
                    else:
                        x.append(4)
                if sq5.collidepoint(mouse_pos) and sq5ch:
                    X_or_o(400, 400)
                    sq5ch = False
                    if x_or_o % 2 == 0:
                        o.append(5)
                    else:
                        x.append(5)
                if sq6.collidepoint(mouse_pos) and sq6ch:
                    X_or_o(800, 400)
                    sq6ch = False
                    if x_or_o % 2 == 0:
                        o.append(6)
                    else:
                        x.append(6)
                if sq7.collidepoint(mouse_pos) and sq7ch:
                    X_or_o(0, 800)
                    sq7ch = False
                    if x_or_o % 2 == 0:
                        o.append(7)
                    else:
                        x.append(7)
                if sq8.collidepoint(mouse_pos) and sq8ch:
                    X_or_o(400, 800)
                    sq8ch = False
                    if x_or_o % 2 == 0:
                        o.append(8)
                    else:
                        x.append(8)
                if sq9.collidepoint(mouse_pos) and sq9ch:
                    X_or_o(800, 800)
                    sq9ch = False
                    if x_or_o % 2 == 0:
                        o.append(9)
                    else:
                        x.append(9)
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

                win()
                click_square()

                #lines
                pygame.draw.rect(screen, 'white', (395,0, 10, 1200))
                pygame.draw.rect(screen, 'white', (795, 0, 10, 1200))
                pygame.draw.rect(screen, 'white', (0, 395, 1200, 10))
                pygame.draw.rect(screen, 'white', (0, 795, 1200, 10))




            pygame.display.flip()
Game()
pygame.quit()
