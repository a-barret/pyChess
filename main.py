import sys, pygame
from board import Board

BLACK = (0,0,0)
WHITE = (255,255,255)
GRAY = (128,128,128)

pygame.init()

SCREEN_SIZE = pygame.display.get_desktop_sizes()
WINDOW_SIZE = SCREEN_SIZE[0][1] * 0.9

window = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
window.fill(GRAY)

board = Board(WINDOW_SIZE)

def calc_relative_space(mouse_position, space_size):
    return (int(mouse_position[0] / space_size) - 1, int(mouse_position[1] / space_size) - 1)

def get_space_piece_placement_coordinates(x, y):
    return (board.get_board_size() * 0.125 * (x + 1.125), board.get_board_size() * 0.125 * (y + 1.125))

piece_selected = None
offset_x = board.get_board_size() * -0.046875
offset_y = offset_x

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            button_pressed = pygame.mouse.get_pressed(num_buttons=3)
            mouse_position = pygame.mouse.get_pos()
            board_position = board.get_board_pos()
            space_size = WINDOW_SIZE * 0.1
            if button_pressed == (True, False, False) and \
                board_position[0][0] <= mouse_position[0] <= board_position[1][0] and \
                board_position[0][1] <= mouse_position[1] <= board_position[1][1]:
                space_clicked = calc_relative_space(mouse_position, space_size)
                piece_selected = board.get_selected_piece(space_clicked)
                if piece_selected != None:
                    print(f"clicked in space {space_clicked} with the {piece_selected.get_name()}")
                else:
                    print(f"clicked in space {space_clicked}")
            else: print("Improper click")
        elif event.type == pygame.MOUSEBUTTONUP:
            mouse_position = pygame.mouse.get_pos()
            board_position = board.get_board_pos()
            space_size = WINDOW_SIZE * 0.1
            if board_position[0][0] <= mouse_position[0] <= board_position[1][0] and \
                board_position[0][1] <= mouse_position[1] <= board_position[1][1] and \
                piece_selected != None:
                space_released = calc_relative_space(mouse_position, space_size)
                print(f"released in space {space_released}")
                space_piece_placement = get_space_piece_placement_coordinates(space_released[0], space_released[1])
                print(space_piece_placement)
                piece_selected.rect.x = space_piece_placement[0]
                piece_selected.rect.y = space_piece_placement[1]
                piece_selected.col = space_released[0]
                piece_selected.row = space_released[1]
            else: print("Improper release")
        elif event.type == pygame.MOUSEMOTION and \
            pygame.mouse.get_pressed(num_buttons=3) == (True, False, False) and \
            piece_selected != None:
            print("Dragging piece")
            mouse_position = pygame.mouse.get_pos()
            piece_selected.rect.x = mouse_position[0] + offset_x
            piece_selected.rect.y = mouse_position[1] + offset_y

    board.draw_board(window)
    pygame.display.flip()

    