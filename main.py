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

# Инициализация счетчиков выстрелов и попаданий
shots = 0
hits = 0

font = pygame.font.Font(None, 36)  # Создание шрифта для отображения текста

running = True
while running:
    screen.fill(color)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            shots += 1
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                hits += 1
                # Если попали по мишени, перемещаем её
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    # Обновление позиции мишени
    target_x += speed_x
    target_y += speed_y

    # Проверка выхода мишени за пределы экрана и изменение направления при необходимости
    if target_x <= 0 or target_x + target_width >= SCREEN_WIDTH:
        speed_x = -speed_x
    if target_y <= 0 or target_y + target_height >= SCREEN_HEIGHT:
        speed_y = -speed_y

    screen.blit(target_img, (target_x, target_y))

    # Отображение счетчиков в центре экрана
    text = font.render(f"Выстрелы: {shots}  Попадания: {hits}", True, (255, 255, 255))
    text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(text, text_rect)

    pygame.display.update()

pygame.quit()
