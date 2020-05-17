import pygame
from models import Board
from views import PyGameVisuals
from .abstract_controller import AbstractController

NUM_ROWS = 50       # 10 | 25 | 50
NUM_COLS = 50       # 10 | 25 | 50
SIZE_OF_CELL = 10   # 50 | 20 | 10


class Controller(AbstractController):
    def __init__(self):
        super().__init__()
        pygame.init()
        self._running = True
        self.vis = PyGameVisuals(SIZE_OF_CELL)
        self.board = Board(NUM_ROWS, NUM_COLS, self.vis)

    def app(self, entry_point):
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.vis.display_text = False
                        self.vis.set_bg = False
                        self.vis.game_running = True
                        self.board.run_game = True
                        self.board.entry_point(entry_point)
                    if event.key == pygame.K_0:
                        self.board.run_game = False
                    if event.key == pygame.K_1:
                        self.board.run_game = True
            self.board.game_of_life()
            if not self.board.run_game:
                self.vis.fill_screen()

        pygame.quit()


if __name__ == '__main__':
    ctr = Controller()
    ctr.app('glider')
