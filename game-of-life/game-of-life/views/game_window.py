import pygame


class Visuals:

    def __init__(self):
        self._display_text = True
        self._set_bg = True
        self._screen = pygame.display.set_mode([500, 500])
        self._title_font = pygame.font.SysFont("dejavuserif", 72)
        self._msg_font = pygame.font.SysFont("dejavuserif", 32)
        self._title = self._title_font.render("Game of Life", True, (255, 255, 255))
        self._msg = self._msg_font.render("Press S to start", True, (255, 255, 255))

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
                    pygame.draw.rect(self._screen, (i * 10, j * 10, 255), (i * 50, j * 50, 50, 50))

        if self._display_text:
            self._screen.blit(self._title, (250 - self._title.get_width() // 2, 250 - self._title.get_height() // 2))
            self._screen.blit(self._msg, (250 - self._msg.get_width() // 2, 310 - self._msg.get_height() // 2))
            pygame.display.flip()

        self._screen.fill((255, 255, 255))

    def draw_cell(self, pos_x, pos_y, alive):
        color = (255, 255, 255)
        if alive:
            color = (0, 0, 0)
        pygame.draw.rect(self._screen, color, (pos_y, pos_x, 50, 50))
        pygame.display.update()



