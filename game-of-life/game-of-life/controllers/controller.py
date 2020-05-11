import pygame
from models import Cell, Board
from views import Visuals
from itertools import chain

NUM_ROWS = 10
NUM_COLS = 10


class Controller:
    def __init__(self):
        pygame.init()
        self._running = True
        self._run_game = False
        self._gen = 0
        self.vis = Visuals()
        self.board = Board(NUM_ROWS, NUM_COLS)

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
                    if event.key == pygame.K_0:
                        self._run_game = False

                        # self.vis.draw_cell(0, 50, 1)
                        # self.vis.draw_cell(0, 100, 1)
                        # self.vis.draw_cell(0, 0, 1)
            self.game_of_life()
            if not self._run_game:
                self.vis.fill_screen()

        pygame.quit()

    def game_of_life(self):
        if self._run_game:
            self.board.matrix[int(100 / 50)][int(50 / 50)].is_alive = True
            self.board.matrix[int(100 / 50)][int(100 / 50)].is_alive = True
            self.board.matrix[int(150 / 50)][int(0 / 50)].is_alive = True

            print("Generation: {}".format(self._gen))
            self._gen += 1
            for i in range(NUM_ROWS):
                for j in range(NUM_COLS):
                    self.board.matrix[i][j].rules.check_neighbourhood()

                    if self.board.matrix[i][j].is_alive:
                        print('here {} {}'.format(i * 50, j * 50))
                        self.vis.draw_cell(i * 50, j * 50, 1)
                    else:
                        self.vis.draw_cell(i * 50, j * 50, 0)
                    # print('Cell {} {} alive - {}'.format(self.board.matrix[i][j].x,
                    #                                     self.board.matrix[i][j].y,
                    #                                     self.board.matrix[i][j].is_alive))
                    # if i == 1 and j == 1:
                    #     self.board.matrix[i][j].rules.check_neighbourhood()
                    pygame.time.wait(10)


if __name__ == '__main__':
    ctr = Controller()
    ctr.app()
