import pygame
import sys
import cells
import random

pygame.init()

SIZE = WIDTH, HEIGHT = 1000, 1000
SCREEN = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Langton's Ant")

FPS = 120
FPS_CLOCK = pygame.time.Clock()

cell_arr = []
fill = []
x = 0
y = 0
w = 10
h = 10
for i in range(int(WIDTH/w)):
    for j in range(int(HEIGHT/h)):
        cell_arr.append(cells.Cell(SCREEN, x, y, w, h))
        x += w
    y += h
    x = 0

for cell in cell_arr:
    cell.draw(1)

ant = cells.Ant(SCREEN, 700, 350, 0)
ant2 = cells.Ant(SCREEN, 600, 500, 1)
ant.draw()

it = 0


while True:

    SCREEN.fill((0, 0, 0))
    if ant.r > 3:
        ant.r = 0
    if ant.r < 0:
        ant.r = 3
    if ant2.r > 3:
        ant2.r = 0
    if ant2.r < 0:
        ant2.r = 3

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    for cell in cell_arr:
        if cell.this.collidepoint(ant.this.x, ant.this.y):
            if cell.f == 1:
                if ant.r == 0:
                    cell.f = 0
                    ant.r += 1
                    ant.x += 10
                elif ant.r == 1:
                    cell.f = 0
                    ant.r += 1
                    ant.y += 10
                elif ant.r == 2:
                    cell.f = 0
                    ant.r += 1
                    ant.x -= 10
                elif ant.r == 3:
                    cell.f = 0
                    ant.r += 1
                    ant.y -= 10
            elif cell.f == 0:
                if ant.r == 0:
                    cell.f = 1
                    ant.r -= 1
                    ant.x -= 10
                elif ant.r == 1:
                    cell.f = 1
                    ant.y -= 10
                    ant.r -= 1
                elif ant.r == 2:
                    cell.f = 1
                    ant.r -= 1
                    ant.x += 10
                elif ant.r == 3:
                    cell.f = 1
                    ant.r -= 1
                    ant.y += 10
        cell.draw(cell.f)
                
    ant.update(ant.x, ant.y, ant.r)
    ant.draw()
    it += 1
    print(it)
                    

    pygame.display.flip()
    FPS_CLOCK.tick(FPS)
