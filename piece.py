import os
import pygame

class Piece(pygame.sprite.Sprite):
    def __init__(self, surface_size, col, row):
        super().__init__()
        self.col = col
        self.row = row

        if row < 4:
            self.color = "black"
        else:
            self.color = "white"
        
        if row in (1,6):
            self.name = "pawn"
        else:
            match col:
                case 0 | 7:
                    self.name = "rook"
                case 1 | 6:
                    self.name = "knight"
                case 2 | 5:
                    self.name = "bishop"
                case 3:
                    self.name = "queen"
                case 4:
                    self.name = "king"
                case _:
                    assert False, "Invalid starting coordinates for a piece"
        
        space_size = surface_size * 0.125
        piece_size = space_size * 0.75
        image_path = os.path.join("images", f"{self.color}_{self.name}.png")
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (piece_size, piece_size))
        self.rect = self.image.get_rect()
        # self.rect.center = (surface_size * 0.125 * 0.5 + col, surface_size * 0.125 * 0.5 + row)
        self.rect.topleft = (col * space_size + space_size + (space_size - piece_size) / 2, row * space_size + space_size + (space_size - piece_size) / 2)

    def get_pos(self):
        return (self.col, self.row)
    
    def get_name(self):
        return self.name
    
    def move_to_location(self, x, y):
        self.rect.topleft = (x, y)