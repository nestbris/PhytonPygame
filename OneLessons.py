# -*- coding: utf-8 -*-
# Pygame шаблон - скелет для нового проекта Pygame
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
# Создаем игру и окно
pygame.init()  # это команда, которая запускает pygame
pygame.mixer.init() # это для звука
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # создание окна программы
pygame.display.set_caption("My Game")
clock = pygame.time.Clock() # таймер для работы с заданной частотой кадров
# Цикл игры
running = True
while running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

pygame.quit()