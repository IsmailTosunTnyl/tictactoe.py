import game

class GUI:
    import pygame, sys
    import time, game


    def __init__(self, game):
        self.pygame.init()
        self.WIDTH = 600
        self.HEIGHT = 600
        self.background_color = "#27aae1"
        self.icon = self.pygame.image.load("icon.png")

        self.screen = self.pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.pygame.display.set_icon(self.icon)
        self.pygame.display.set_caption("TIC TAC TOE")
        self.screen.fill(self.background_color)
        self.g = game
        self.gameStatus = True
        self.font = self.pygame.font.Font('orange juice 2.0.ttf', 40)


    def drawLines(self):
        a = self.HEIGHT / 3
        l = list()
        for i in range(1, 3):
            l.append((a * i))

        for i in l:
            self.pygame.draw.line(self.screen, "#FFFFFF", (0, i), (600, i), 8)
            self.pygame.draw.line(self.screen, "#FFFFFF", (i, 0), (i, 600), 8)

    def drawFigures(self, x, y):

        # draw X
        if self.g.player == "O":
            self.pygame.draw.line(self.screen, "#FFFFFF", (y * 200 + 20, x * 200 + 20), (y * 200 + 180, x * 200 + 180), 6)
            self.pygame.draw.line(self.screen, "#FFFFFF", (y * 200 + 180, x * 200 + 20), (y * 200 + 20, x * 200 + 180), 6)

       #draw O
        else:
             self.pygame.draw.circle(self.screen, "#FFFFFF", (y * 200 + 100, x * 200 + 100), 80, 6)

    def endGame(self,content):
        self.gameStatus = False
        print("endGame")
        self.pygame.init()
        self.screen = self.pygame.display.set_mode((600, 200))
        color = "#FFFFFF"
        self.screen.fill(color)


        # create a text surface object,
        # on which text is drawn on it.

        text = self.font.render(content, True, self.background_color)

        # create a rectangular object for the
        # text surface object
        textRect = text.get_rect()

        # set the center of the rectangular object.
        textRect.center = (600 // 2, 200 // 2)
        self.screen.blit(text, textRect)
        self.pygame.display.update()


    def startGUI(self):
        self.drawLines()
        while True:
            self.time.sleep(0.15)
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    self.sys.exit()

                if event.type == self.pygame.MOUSEBUTTONDOWN:
                    mouseX = event.pos[0]
                    mouseY = event.pos[1]
                    if self.gameStatus:
                        status = self.g.play(int(mouseY / 200), int(mouseX / 200))
                        if status == "win":
                            self.drawFigures(int(mouseY / 200), int(mouseX / 200))
                            print("Win")
                            self.endGame(f'{self.g.player} Win')

                        elif status == "draw":
                            self.drawFigures(int(mouseY / 200), int(mouseX / 200))
                            self.endGame(' Draw')
                            print("Draw")

                        else:
                            self.drawFigures(int(mouseY / 200), int(mouseX / 200))
                    else:

                        self.WIDTH = 600
                        self.HEIGHT = 600
                        self.background_color = "#27aae1"
                        self.icon = self.pygame.image.load("icon.png")

                        self.screen = self.pygame.display.set_mode((self.WIDTH, self.HEIGHT))
                        self.pygame.display.set_icon(self.icon)
                        self.pygame.display.set_caption("TIC TAC TOE")
                        self.screen.fill(self.background_color)
                        self.gameStatus = True
                        self.drawLines()
                        self.g.restart()


            self.pygame.display.update()
