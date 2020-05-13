import pygame

HEIGHT = 500
WIDTH = 500


class Visuals:
    def __init__(self, size_of_cell):
        self._display_text = True
        self._set_bg = True

        self._screen = pygame.display.set_mode([HEIGHT, WIDTH])
        self._size_of_cell = size_of_cell

        title_font = pygame.font.SysFont("dejavuserif", 72)
        msg_font = pygame.font.SysFont("dejavuserif", 32)
        controls_font = pygame.font.SysFont("dejavuserif", 24)

        self._title = title_font.render("Game of Life", True, (255, 255, 255))
        self._msg = msg_font.render("Press S to start", True, (255, 255, 255))
        self._controls = controls_font.render("press 0 to pause | press 1 to resume", True, (255, 255, 255))

    @property
    def display_text(self):
        return self._display_text

    @display_text.setter
    def display_text(self, val):
        self._display_text = val

    @property
    def set_bg(self):
        return self._set_bg

    @set_bg.setter
    def set_bg(self, val):
        self._set_bg = val

    def fill_screen(self):
        self._screen.fill((255, 255, 255))
        if self._set_bg:
            for i in range(10):
                for j in range(10):
                    pygame.draw.rect(self._screen, (i * 10, j * 10, 100), (i * 50, j * 50, 50, 50))

        if self._display_text:
            self._screen.blit(self._title, (250 - self._title.get_width() / 2, 200 - self._title.get_height() // 2))
            self._screen.blit(self._msg, (250 - self._msg.get_width() / 2, 260 - self._msg.get_height() // 2))
            self._screen.blit(self._controls, (160 - self._msg.get_width() / 2, 410 - self._msg.get_height() // 2))
            pygame.display.flip()

        self._screen.fill((255, 255, 255))

    def draw_cell(self, pos_x, pos_y, alive):
        color = (255, 255, 255)
        if alive:
            color = (0, 0, 0)
        pygame.draw.rect(self._screen, color, (pos_y, pos_x, self._size_of_cell, self._size_of_cell))
        pygame.display.update()
