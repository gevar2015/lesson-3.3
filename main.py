import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/40883.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target.png")
target_width = 80
target_height = 80

# Начальная позиция мишени
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Случайная скорость перемещения мишени по осям x и y
speed_x = random.randint(-5, 5)
speed_y = random.randint(-5, 5)

color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:
    screen.fill(color)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обновление позиции мишени
    target_x += speed_x
    target_y += speed_y

    # Проверка выхода мишени за пределы экрана и изменение направления при необходимости
    if target_x <= 0 or target_x + target_width >= SCREEN_WIDTH:
        speed_x = -speed_x
    if target_y <= 0 or target_y + target_height >= SCREEN_HEIGHT:
        speed_y = -speed_y

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()
