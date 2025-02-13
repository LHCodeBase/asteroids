import pygame
from constants import SCREEN_WIDTH


class Score():
    def __init__(self) -> None:
        self.score = 0
        self.multiplier = 1
        # Set font to default
        pygame.font.init()
        self.FONT = pygame.font.Font(None, 24)
        pass

    def highscore(self, score: int) -> int:
        return max(score, self.score)

    def __str__(self) -> str:
        return str(self.score).rjust(6, '0')

    def get_score(self) -> int:
        return self.score

    def render_score(self, screen: pygame.Surface) -> None:
        pygame.display.set_caption("Score")
        pygame.font.init()
        score_text = self.FONT.render(str(self), True, 'white') 
        screen.blit(score_text, (SCREEN_WIDTH - 80, 10))
        pass

    def increase(self, amount: int) -> None:
        self.score += amount
        pass

    def reset(self) -> None:
        self.score = 0
        pass

    def add_perm_multiplier(self, amount: int) -> None:
        # For future use
        pass

    def add_temp_multiplier(self, amount: int, time: int) -> None:
        # For future use
        pass

