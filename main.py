import pygame
import random

pygame.init()  # Инициализация всех импортированных модулей pygame

SCREEN_WIDTH = 800  # Ширина экрана
SCREEN_HEIGHT = 600  # Высота экрана
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))  # Создание окна игры

pygame.display.set_caption("Игра Тир")  # Установка названия окна
icon = pygame.image.load("img/40883.jpg")  # Загрузка иконки приложения
pygame.display.set_icon(icon)  # Установка иконки окна

target_img = pygame.image.load("img/target.png")  # Загрузка изображения мишени
target_width = 80  # Ширина мишени
target_height = 80  # Высота мишени

# Начальная позиция мишени, случайно выбирается в пределах границ экрана
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)

# Случайный цвет фона
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

running = True
while running:  # Главный цикл игры
    screen.fill(color)  # Заливка экрана случайным цветом

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Событие закрытия окна
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:  # Событие нажатия на кнопку мыши
            mouse_x, mouse_y = pygame.mouse.get_pos()  # Получение координат мыши
            # Проверка попадания по мишени
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                # Если попали по мишени, перемещаем её
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)

    screen.blit(target_img, (target_x, target_y))  # Отрисовка мишени на новом месте
    pygame.display.update()  # Обновление содержимого всего экрана

pygame.quit()  # Закрытие и выход из pygame



