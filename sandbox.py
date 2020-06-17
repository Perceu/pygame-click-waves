import pygame
import time
import math
import random

pygame.init()

windown_size = width, height = 800, 400
screen = pygame.display.set_mode(windown_size)
ingame = True

class Wave():
    def __init__(self, position):
        self.position_initial = position
        self.size_out = 5
        self.size_in = 0
        self.running = True
        self.white = (255,255,255)
        self.black = (0,0,0)

    def update(self):
        self.size_in +=5
        self.size_out +=5

    def draw_circle(self):
        pygame.draw.circle(screen, self.white, self.position_initial, self.size_out)
        pygame.draw.circle(screen, self.black, self.position_initial, self.size_in)
        self.update()

    def draw(self):
        self.draw_circle()

waves = []
while ingame:
    screen.fill((0,0,0))
    time.sleep(0.03)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ingame = False 
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            waves.append(Wave(pos))

    for wave in waves:
        wave.draw()

    for key, wave in enumerate(waves):
        if wave.size_out > width:
            del(waves[key])
    print(len(waves))
    pygame.display.update()