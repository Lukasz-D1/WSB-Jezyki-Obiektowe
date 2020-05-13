import pygame
from models import Cell, Board, StaticRules
from views import Visuals
from itertools import chain
from random import randint

NUM_ROWS = 50
NUM_COLS = 50
SIZE_OF_CELL = 10


class Controller:
    def __init__(self):
        pygame.init()
        self._running = True
        self._run_game = False
        self._gen = 0
        self.vis = Visuals(SIZE_OF_CELL)
        self.board = Board(NUM_ROWS, NUM_COLS)
        self.rules = StaticRules()

    def app(self):
        while self._running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        self.vis.display_text = False
                        self.vis.set_bg = False
                        self.vis.game_running = True
                        self._run_game = True
                        self.board.matrix[0][0].is_alive = True
                        self.board.matrix[1][1].is_alive = True
                        self.board.matrix[1][2].is_alive = True
                        self.board.matrix[2][0].is_alive = True
                        self.board.matrix[2][1].is_alive = True
                    if event.key == pygame.K_0:
                        self._run_game = False
                    if event.key == pygame.K_1:
                        self._run_game = True
            self.game_of_life()
            if not self._run_game:
                self.vis.fill_screen()

        pygame.quit()

    def game_of_life(self):

        if self._run_game:

            print("Generation: {}".format(self._gen))
            self._gen += 1
            for i in range(NUM_ROWS):
                for j in range(NUM_COLS):
                    #print(self.board.matrix[i][j].x, self.board.matrix[i][j].y, self.board.matrix[i][j].is_alive, self.board.matrix[i][j].cnt)
                    self.rules.check_neighbourhood(self.board, self.board.matrix[i][j].x, self.board.matrix[i][j].y)
                    if self.board.matrix[i][j].is_alive:
                        self.vis.draw_cell(i * SIZE_OF_CELL, j * SIZE_OF_CELL, 1)
                    else:
                        self.vis.draw_cell(i * SIZE_OF_CELL, j * SIZE_OF_CELL, 0)
            for i in range(NUM_ROWS):
                for j in range(NUM_COLS):
                    self.rules.decide(self.board, i, j)


if __name__ == '__main__':
    ctr = Controller()
    ctr.app()
