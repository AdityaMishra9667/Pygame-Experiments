import pygame, sys, math

pygame.init()

FPS = 10 # frames per second setting
fpsClock = pygame.time.Clock()

# set up the window
WIDTH = 700
WIN = pygame.display.set_mode((WIDTH, WIDTH), 0, 32)
pygame.display.set_caption('Cloth Physics')

GRAVITY = math.sqrt(400)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class Pendulum:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.selected = False

    def update(self):
        if self.selected == True:
            pos = pygame.mouse.get_pos()
            self.x = pos[0]
            self.y = pos[1]
        if mouse == False:
            self.selected = False

    def draw(self,surf,size,color):
        pygame.draw.circle(surf, color, (int(self.x), int(self.y)), size)

class Motion:
    def __init__(self,index0,index1):
        self.index0 = index0
        self.index1 = index1

    def move(self):
        self.x0 = pendulum[self.index0].x
        self.x1 = pendulum[self.index1].x
        self.y0 = pendulum[self.index0].y
        self.y1 = pendulum[self.index1].y
        self.dist = math.sqrt((self.x0 - self.x1)**2 + (self.y0 - self.y1)**2)
        self.sina = abs((self.y1-self.y0)/self.dist)
        self.cosa = abs((self.x1-self.x0)/self.dist)
        delta_x = self.x1-self.x0
        delta_y = self.y1-self.y0
        self.tension = 2*delta_y

        pendulum[self.index1].x -=  (delta_x * 0.2)
        pendulum[self.index1].y += GRAVITY - (self.tension * self.sina) * 0.2

    def draw(self, surf, size):
        x0 = pendulum[self.index0].x
        y0 = pendulum[self.index0].y
        x1 = pendulum[self.index1].x
        y1 = pendulum[self.index1].y
        pygame.draw.line(surf, WHITE, (int(x0), int(y0)), (int(x1), int(y1)), size)

def find_particle(pos):
    for i in range(len(pendulum)):
        dx = pendulum[i].x - pos[0]
        dy = pendulum[i].y - pos[1]
        if (dx*dx + dy*dy) < 400:
            pendulum[i].selected = True
            break

pendulum = []
motion = []
for i in range(10):
    c = Pendulum(100, 40+i*10)
    pendulum.append(c)

for i,_ in enumerate(pendulum):
    if i < len(pendulum)-1:
        m = Motion(i,i+1)
        motion.append(m)

run = True
mouse = False

while run:
    WIN.fill(BLACK)

    for mo in motion:
        mo.move()
    for p in pendulum:
        p.update()
        p.draw(WIN, 3, WHITE)

    for mo in motion:
        mo.draw(WIN, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = True
        if event.type == pygame.MOUSEBUTTONUP:
            mouse = False

    if mouse:
        pos = pygame.mouse.get_pos()
        find_particle(pos)

    pygame.display.update()
    fpsClock.tick(FPS)
