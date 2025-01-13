import pygame
import random


class GuessTheNumberGame:
    def __init__(self):
        pygame.init()
        # Screen dimensions
        self.WIDTH, self.HEIGHT = 640, 480
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Guess the Secret Number")

        # Colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)

        # Font
        self.FONT = pygame.font.Font(None, 36)

        # Initialize game variables
        self.reset_game()

        # Game state
        self.running = True

    def reset_game(self):
        """Resets the game variables to their initial state."""
        self.secret_number = random.randint(1, 100)
        self.attempts_left = 10
        self.user_input = ""
        self.message = ""
        self.game_over = False

    def draw_text(self, text, color, center):
        """Helper function to render and draw text at a given position."""
        rendered_text = self.FONT.render(text, True, color)
        text_rect = rendered_text.get_rect(center=center)
        self.screen.blit(rendered_text, text_rect)

    def handle_events(self):
        """Handles all user input and events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.running = False
                elif not self.game_over:
                    self.handle_game_input(event)
                elif event.key == pygame.K_RETURN:
                    self.reset_game()

    def handle_game_input(self, event):
        """Handles game-related input during active gameplay."""
        if event.key == pygame.K_RETURN:  # Enter key
            if self.user_input.isdigit():
                self.process_guess(int(self.user_input))
            else:
                self.message = "Enter a valid number!"
            self.user_input = ""  # Clear input
        elif event.key == pygame.K_BACKSPACE:  # Backspace key
            self.user_input = self.user_input[:-1]
        elif event.unicode.isdigit():  # Add numeric input
            self.user_input += event.unicode

    def process_guess(self, guess):
        """Processes the user's guess and updates the game state."""
        self.attempts_left -= 1
        if guess == self.secret_number:
            self.message = f"Congratulations! You guessed it: {self.secret_number}"
            self.game_over = True
        elif guess < self.secret_number:
            self.message = "Too low!"
        else:
            self.message = "Too high!"

        if self.attempts_left == 0 and not self.game_over:
            self.message = f"Out of attempts! The number was {self.secret_number}"
            self.game_over = True

    def draw_game(self):
        """Draws all game elements on the screen."""
        self.screen.fill(self.WHITE)
        self.draw_text("Guess the number (1-100)", self.BLACK, (self.WIDTH // 2, 50))
        self.draw_text(f"Attempts left: {self.attempts_left}", self.BLACK, (self.WIDTH // 2, 100))
        self.draw_text(f"Your guess: {self.user_input}", self.BLACK, (self.WIDTH // 2, 150))
        self.draw_text(self.message, self.GREEN if "Congratulations" in self.message else self.RED, (self.WIDTH // 2, 250))

        if self.game_over:
            self.draw_text("Press Enter to play again or Q to quit", self.BLACK, (self.WIDTH // 2, 350))
        else:
            self.draw_text("Press Q to quit", self.BLACK, (self.WIDTH // 2, 350))

        pygame.display.flip()

    def run(self):
        """Runs the main game loop."""
        while self.running:
            self.handle_events()
            self.draw_game()

        pygame.quit()


# Run the game
if __name__ == "__main__":
    game = GuessTheNumberGame()
    game.run()
