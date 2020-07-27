import pygame
import random

WIDTH = 1000
ROWS = 25
WIN = pygame.display.set_mode((WIDTH,WIDTH))
pygame.display.set_caption("Particle Physics")
clock = pygame.time.Clock()

RED = [255, 0, 0]
WHITE = [255,255,255]
BLUE = [0,0,255]

GRAVITY = 2
wid = 5
pwidth = 400
plength = 20

class Square:
    def __init__(self,x,y,width,color,vel_x,vel_y):
        self.x = x
        self.y = y
        self.width = width
        self.color = color
        self.velx = vel_x
        self.vely = vel_y
        self.colour_array = [0, 5, 5]

    def draw(self):
        pygame.draw.rect(WIN, self.colour, (self.x, self.y, self.width, self.width))

    def move(self):
        self.x += self.velx
        self.y += self.vely
        self.vely += GRAVITY
        if self.color != [255, 0, 0]:
            self.color = [self.colr - self.col_arr for self.colr, self.col_arr in zip(self.color, self.colour_array)]
        self.colour = tuple(self.color)

    def change_color(self):
        pass

class Platform:
    def __init__(self,x,y,width,length,color):
        self.x = x
        self.y = y
        self.width = width
        self.length = length
        self.color = tuple(color)

    def draw(self):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, self.width, self.length))


def particles(x,y):
    part = []
    a,b = x,y
    for i in range(50):
        c = random.randint(-10,10)
        d = random.randint(-30,0)
        part.append(Square(a,b,wid, WHITE, c, d))
    return part;

def draw_text():
    pass

def main():
    run = True
    part = False

    while run:
        if pygame.mouse.get_pressed()[0]: #if left mouse is pressed
            part = True
            pos = pygame.mouse.get_pos()
            a,b = pos
            particl = particles(a,b)
        WIN.fill((0,0,0))
        for event in pygame.event.get(): #event.get() checks for an event every frame
            if event.type == pygame.QUIT:
                run = False

        x,y = 500,500
        plat = Platform(x-pwidth//2,y,pwidth,plength,BLUE)
        plat.draw()

        if part:
            for square in particl:
                if square.x in range(plat.x, plat.x + pwidth) and square.y in range(plat.y, plat.y+plength):
                    square.vely -= abs(square.vely) + 5
                square.move()
                square.change_color()
                square.draw()

        pygame.display.update()
        pygame.time.delay(40)
        #clock.tick(60)

    pygame.quit()

main()
