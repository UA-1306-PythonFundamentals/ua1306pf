import pygame

# Constants
FPS = 60
WIDTH_DISPLAY = 500
HEIGHT_DISPLAY = 500
DELTA_STEP = 5

BLACK_COLOR = (0, 0, 0)
RED_COLOR = (250, 0, 0)

class Game:
    def __init__(self):
        # Initialize Pygame and game variables
        pygame.init()
        self.gameDisplay = pygame.display.set_mode((WIDTH_DISPLAY, HEIGHT_DISPLAY), pygame.RESIZABLE)
        pygame.display.set_caption("My first game")

        self.COORD_X = 50
        self.COORD_Y = 50
        self.WIDTH_RECTANGLE = 40
        self.HEIGHT_RECTANGLE = 60
        self.run = True
        self.clock = pygame.time.Clock()

    def handle_events(self):
        """Handle events like quitting and key presses."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

    def move_rectangle(self):
        """Handle movement of the rectangle within screen bounds."""
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and self.COORD_X - DELTA_STEP >= 0:
            self.COORD_X -= DELTA_STEP
        if keys[pygame.K_RIGHT] and self.COORD_X + self.WIDTH_RECTANGLE + DELTA_STEP <= WIDTH_DISPLAY:
            self.COORD_X += DELTA_STEP
        if keys[pygame.K_UP] and self.COORD_Y - DELTA_STEP >= 0:
            self.COORD_Y -= DELTA_STEP
        if keys[pygame.K_DOWN] and self.COORD_Y + self.HEIGHT_RECTANGLE + DELTA_STEP <= HEIGHT_DISPLAY:
            self.COORD_Y += DELTA_STEP

    def draw(self):
        """Draw everything on the screen."""
        self.gameDisplay.fill(BLACK_COLOR)
        pygame.draw.rect(self.gameDisplay, RED_COLOR, [self.COORD_X, self.COORD_Y, self.WIDTH_RECTANGLE, self.HEIGHT_RECTANGLE])
        pygame.display.update()

    def run_game(self):
        """Main game loop."""
        while self.run:
            self.handle_events()
            self.move_rectangle()
            self.draw()
            self.clock.tick(FPS)

        pygame.quit()

if __name__ == "__main__":
    game = Game()
    game.run_game()
