import pygame

# Define some constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BLOCK_SIZE = 20

# Define the snake class
class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = "right"

    def move(self):
        # Get the head of the snake
        head = self.body[0]

        # Move the head in the current direction
        if self.direction == "right":
            head = (head[0] + BLOCK_SIZE, head[1])
        elif self.direction == "left":
            head = (head[0] - BLOCK_SIZE, head[1])
        elif self.direction == "up":
            head = (head[0], head[1] - BLOCK_SIZE)
        elif self.direction == "down":
            head = (head[0], head[1] + BLOCK_SIZE)

        # Add the new head to the body of the snake
        self.body.insert(0, head)

        # Remove the tail of the snake
        self.body.pop()

    def draw(self, screen):
        for block in self.body:
            pygame.draw.rect(screen, (0, 0, 255), (block[0], block[1], BLOCK_SIZE, BLOCK_SIZE))

# Define the food class
class Food:
    def __init__(self):
        # Randomly place the food on the screen
        self.x = random.randint(0, SCREEN_WIDTH - BLOCK_SIZE)
        self.y = random.randint(0, SCREEN_HEIGHT - BLOCK_SIZE)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))

# Initialize Pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create the snake
snake = Snake()

# Create the food
food = Food()

# Start the game loop
while True:

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.direction = "up"
            elif event.key == pygame.K_DOWN:
                snake.direction = "down"
            elif event.key == pygame.K_LEFT:
                snake.direction = "left"
            elif event.key == pygame.K_RIGHT:
                snake.direction = "right"

    # Move the snake
    snake.move()

    # Check if the snake has collided with the food
    if snake.body[0] == (food.x, food.y):
        # Create a new food
        food = Food()

        # Grow the snake
        snake.body.append((snake.body[-1][0] + BLOCK_SIZE, snake.body[-1][1]))

    # Check if the snake has collided with itself
    for block in snake.body[1:]:
        if snake.body[0] == block:
            # Game over
            break

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Draw the snake
    snake.draw(screen)

    # Draw the food
    food.draw(screen)

    # Update the screen
    pygame.display.flip()