import pygame

class Space(pygame.Rect):
    def __init__(self, col, row, width, height):
        super().__init__((col + 1) * width, (row + 1) * height, width, height)
        self.size = (width, height)
        self.col = col
        self.row = row
        self.is_empty = True

    def get_size(self):
        return self.size