import pygame
from space import Space
from piece import Piece

WHITE = (255,255,255)
BLACK = (0,0,0)

class Board:
    def __init__(self, window_size):
        self.board_size = window_size * 0.8
        self.board_start = (window_size * 0.1, window_size * 0.1)
        self.board_end = (window_size * 0.9, window_size * 0.9)
        self.rect = pygame.Rect(self.board_start[0], self.board_start[1], self.board_size, self.board_size)
        self.border = pygame.Rect(window_size*0.09, window_size*0.09, window_size*0.8225, window_size*0.8225)
        self.spaces = []
        num_board_spaces = 8
        space_size = window_size * 0.1
        for row in range(num_board_spaces):
            row_spaces = []
            for col in range(num_board_spaces):
                row_spaces.append(Space(col, row, space_size, space_size))
            self.spaces.append(row_spaces)
        
        self.pieces = pygame.sprite.Group()
        for row in range(int(round(num_board_spaces / 2))):
            if row > 1:
                row += 4
            for col in range(num_board_spaces):
                self.pieces.add(Piece(self.board_size, col, row))
        

    def draw_board(self, surface):
        def switch_color(color):
            if color == WHITE:
                color = BLACK
            else:
                color = WHITE
            return color
        
        pygame.draw.rect(surface, WHITE, self.border, width=5)

        color = WHITE
        for row in self.spaces:
            for space in row:
                pygame.draw.rect(surface, color, space)
                color = switch_color(color)
            color = switch_color(color)
        
        self.pieces.draw(surface)
    
    def get_board_size(self):
        return self.board_size
    
    def get_board_pos(self):
        return (self.board_start, self.board_end)
    
    def get_selected_piece(self, space_selected):
        for piece in self.pieces:
            if piece.get_pos() == space_selected:
                return piece

        