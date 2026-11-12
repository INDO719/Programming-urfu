"""Игра «Змейка» на Pygame."""

from abc import abstractmethod
from random import randint

import pygame

# Константы для размеров поля и сетки:
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

# Направления движения:
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Цвет фона - черный:
BOARD_BACKGROUND_COLOR = (0, 0, 0)

# Цвет границы ячейки
BORDER_COLOR = (93, 216, 228)

# Цвет яблока
APPLE_COLOR = (255, 0, 0)

# Цвет змейки
SNAKE_COLOR = (0, 255, 0)

# Скорость движения змейки:
SPEED = 5

# Настройка игрового окна:
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

# Заголовок окна игрового поля:
pygame.display.set_caption('Змейка')

# Настройка времени:
clock = pygame.time.Clock()


class GameObject:
    """Базовый класс для игровых объектов."""

    def __init__(self) -> None:
        """Инициализирует объект с позицией и цветом."""
        self.position = None
        self.body_color = None

    @abstractmethod
    def draw(self) -> None:
        """Отрисовывает объект на экране."""


class Apple(GameObject):
    """Класс яблока, которое собирает змейка."""

    def __init__(self) -> None:
        """Создаёт яблоко в случайной позиции, кроме центра."""
        super().__init__()
        self.body_color = APPLE_COLOR

        self.randomize_position()
        while self.position == (GRID_WIDTH // 2 * GRID_SIZE,
                                GRID_HEIGHT // 2 * GRID_SIZE):
            self.randomize_position()

    def randomize_position(self) -> None:
        """Устанавливает случайную позицию яблока в пределах сетки."""
        x = randint(0, GRID_WIDTH - 1) * GRID_SIZE
        y = randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        self.position = (x, y)

    def draw(self) -> None:
        """Отрисовывает яблоко."""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)


class Snake(GameObject):
    """Класс змейки."""

    def __init__(self) -> None:
        """Инициализирует змейку в центре экрана."""
        super().__init__()
        self.direction = RIGHT
        self.body_color = SNAKE_COLOR

        self.position = (GRID_WIDTH // 2 * GRID_SIZE,
                         GRID_HEIGHT // 2 * GRID_SIZE)
        self.positions = [self.position]

        self.length = 1

        self.next_direction = None

        self.last = None

    def draw(self) -> None:
        """Отрисовывает змейку и затирает последний сегмент."""
        for position in self.positions[:-1]:
            rect = pygame.Rect(position, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

        # Отрисовка головы змейки
        head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)

        # Затирание последнего сегмента
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

    def update_direction(self) -> None:
        """Обновляет текущее направление движения змейки."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None

    def move(self) -> None:
        """Перемещает змейку на одну клетку в текущем направлении."""
        head_x_pos, head_y_pos = self.get_head_position()

        head_new_x_pos = head_x_pos + GRID_SIZE * self.direction[0]
        head_new_y_pos = head_y_pos + GRID_SIZE * self.direction[1]

        if head_new_x_pos == SCREEN_WIDTH:
            head_new_x_pos = 0
        if head_new_x_pos < 0:
            head_new_x_pos = SCREEN_WIDTH - GRID_SIZE

        if head_new_y_pos == SCREEN_HEIGHT:
            head_new_y_pos = 0
        if head_new_y_pos < 0:
            head_new_y_pos = SCREEN_HEIGHT - GRID_SIZE

        self.positions = [(head_new_x_pos, head_new_y_pos)] + self.positions

        self.last = self.positions.pop()

    def get_head_position(self) -> tuple[int, int]:
        """Возвращает позицию головы змейки."""
        return self.positions[0]

    def reset(self) -> None:
        """Сбрасывает змейку в начальное состояние."""
        for pos in self.positions:
            cell = pygame.Rect(pos, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, cell)

        self.position = (GRID_WIDTH // 2 * GRID_SIZE,
                         GRID_HEIGHT // 2 * GRID_SIZE)
        self.positions = [self.position]

        self.direction = RIGHT

        self.length = 1


def handle_keys(game_object: Snake) -> None:
    """Обрабатывает нажатия клавиш для управления змейкой."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game_object.direction != DOWN:
                game_object.next_direction = UP
            elif event.key == pygame.K_DOWN and game_object.direction != UP:
                game_object.next_direction = DOWN
            elif event.key == pygame.K_LEFT and game_object.direction != RIGHT:
                game_object.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and game_object.direction != LEFT:
                game_object.next_direction = RIGHT


def main() -> None:
    """Основной цикл игры."""
    
    # Инициализация PyGame:
    pygame.init()
    # Создаём экземпляры классов:
    apple = Apple()
    snake = Snake()

    while True:
        clock.tick(SPEED)

        handle_keys(snake)
        snake.update_direction()

        snake.move()

        if len(snake.positions) == GRID_WIDTH * GRID_HEIGHT:
            print("ПОБЕДА")
            pygame.quit()
            raise SystemExit

        if snake.get_head_position() == apple.position:
            apple.randomize_position()
            while apple.position in snake.positions:
                apple.randomize_position()
            snake.positions.append(snake.last)
            snake.length += 1

        if snake.positions.count(snake.get_head_position()) > 1:
            snake.reset()

        apple.draw()
        snake.draw()

        pygame.display.update()


if __name__ == '__main__':
    main()
