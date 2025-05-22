from random import choice, randint
import pygame
from abc import ABC, abstractmethod
from typing import List, Tuple, Optional

# Константы
SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

BOARD_BACKGROUND_COLOR = (0, 0, 0)
BORDER_COLOR = (93, 216, 228)
APPLE_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)
SPEED = 10

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
pygame.display.set_caption('Змейка')
clock = pygame.time.Clock()

class GameObject(ABC):
    """Базовый класс для всех игровых объектов."""
    
    def __init__(self, position: Tuple[int, int], body_color: Tuple[int, int, int]):
        """
        Инициализация игрового объекта.
        
        :param position: Начальная позиция (x, y) в пикселях
        :param body_color: Цвет объекта в формате RGB
        """
        self.position = position
        self.body_color = body_color
    
    @abstractmethod
    def draw(self) -> None:
        """Абстрактный метод для отрисовки объекта."""
        pass

class Apple(GameObject):
    """Класс, представляющий яблоко на игровом поле."""
    
    def __init__(self):
        """Инициализирует яблоко со случайной позицией."""
        super().__init__((0, 0), APPLE_COLOR)
        self.randomize_position()
    
    def randomize_position(self) -> None:
        """Устанавливает случайную позицию в пределах сетки."""
        x = randint(0, GRID_WIDTH - 1) * GRID_SIZE
        y = randint(0, GRID_HEIGHT - 1) * GRID_SIZE
        self.position = (x, y)
    
    def draw(self) -> None:
        """Отрисовывает яблоко с границей."""
        rect = pygame.Rect(self.position, (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, rect)
        pygame.draw.rect(screen, BORDER_COLOR, rect, 1)

class Snake(GameObject):
    """Класс, управляющий змейкой."""
    
    def __init__(self):
        """Инициализирует змейку в центре экрана."""
        start_pos = (SCREEN_WIDTH//2, SCREEN_HEIGHT//2)
        super().__init__(start_pos, SNAKE_COLOR)
        self.positions: List[Tuple[int, int]] = [start_pos]
        self.direction: Tuple[int, int] = RIGHT
        self.next_direction: Optional[Tuple[int, int]] = None
        self.last: Optional[Tuple[int, int]] = None
    
    def update_direction(self) -> None:
        """Обновляет направление движения."""
        if self.next_direction:
            self.direction = self.next_direction
            self.next_direction = None
    
    def move(self) -> None:
        """Обновляет позиции сегментов змейки."""
        self.last = self.positions[-1] if len(self.positions) > 1 else None
        head_x, head_y = self.positions[0]
        dx, dy = self.direction
        
        # Телепортация через границы
        new_head = (
            (head_x + dx * GRID_SIZE) % SCREEN_WIDTH,
            (head_y + dy * GRID_SIZE) % SCREEN_HEIGHT
        )
        
        self.positions.insert(0, new_head)
        self.positions.pop() if self.last else None
    
    def grow(self) -> None:
        """Увеличивает длину змейки."""
        self.positions.append(self.last)
    
    def reset(self) -> None:
        """Сбрасывает змейку в начальное состояние."""
        self.positions = [self.position]
        self.direction = RIGHT
        self.next_direction = None
    
    def check_collision(self) -> bool:
        """Проверяет столкновение головы с телом."""
        return self.positions[0] in self.positions[1:]
    
    def draw(self) -> None:
        """Отрисовывает змейку с границами и затирает след."""
        # Отрисовка тела
        for pos in self.positions[:-1]:
            rect = pygame.Rect(pos, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, self.body_color, rect)
            pygame.draw.rect(screen, BORDER_COLOR, rect, 1)
        
        # Отрисовка головы
        head_rect = pygame.Rect(self.positions[0], (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(screen, self.body_color, head_rect)
        pygame.draw.rect(screen, BORDER_COLOR, head_rect, 1)
        
        # Затирание последнего сегмента
        if self.last:
            last_rect = pygame.Rect(self.last, (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(screen, BOARD_BACKGROUND_COLOR, last_rect)

def handle_keys(snake: Snake) -> None:
    """Обрабатывает нажатия клавиш для управления змейкой."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.direction != DOWN:
                snake.next_direction = UP
            elif event.key == pygame.K_DOWN and snake.direction != UP:
                snake.next_direction = DOWN
            elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                snake.next_direction = LEFT
            elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                snake.next_direction = RIGHT

def main():
    """Основная функция игры."""
    pygame.init()
    snake = Snake()
    apple = Apple()
    
    while True:
        clock.tick(SPEED)
        handle_keys(snake)
        snake.update_direction()
        snake.move()
        
        # Проверка съедения яблока
        if snake.positions[0] == apple.position:
            snake.grow()
            apple.randomize_position()
        
        # Проверка столкновений
        if snake.check_collision():
            snake.reset()
        
        # Отрисовка
        screen.fill(BOARD_BACKGROUND_COLOR)
        apple.draw()
        snake.draw()
        pygame.display.update()

if __name__ == '__main__':
    main()