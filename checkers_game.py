import pygame, sys, math

pygame.init()
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

# Ranglar
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 70, 70)
BLUE = (70, 130, 255)
GRAY = (200, 200, 200)
GOLD = (255, 215, 0)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Modern Smooth Checkers")

# Shashka klassi
class Piece:
    PADDING = 15
    OUTLINE = 3
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        # Shaffof soyali aylana
        shadow = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(shadow, (*self.color, 200), (SQUARE_SIZE // 2, SQUARE_SIZE // 2), radius)
        win.blit(shadow, (self.x - SQUARE_SIZE // 2, self.y - SQUARE_SIZE // 2))

        if self.king:
            pygame.draw.circle(win, GOLD, (self.x, self.y), radius // 2, 4)

    def move(self, row, col):
        # Silliq harakat animatsiyasi
        start_x, start_y = self.x, self.y
        end_x = SQUARE_SIZE * col + SQUARE_SIZE // 2
        end_y = SQUARE_SIZE * row + SQUARE_SIZE // 2

        steps = 20
        for i in range(1, steps + 1):
            t = i / steps
            self.x = start_x + (end_x - start_x) * t
            self.y = start_y + (end_y - start_y) * t
            draw_board(WIN, board)
            pygame.display.update()
            pygame.time.delay(10)

        self.row = row
        self.col = col
        self.calc_pos()

# Taxta klassi
class Board:
    def __init__(self):
        self.board = []
        self.create_board()

    def draw_squares(self, win):
        win.fill(GRAY)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, BLACK, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, RED))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, BLUE))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = 0, piece
        piece.move(row, col)
        if row == ROWS - 1 or row == 0:
            piece.make_king()

def draw_board(win, board):
    board.draw(win)

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

board = Board()
selected = None
turn = BLUE

def main():
    global selected, turn
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60) 

        draw_board(WIN, board)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                piece = board.board[row][col]

                if selected:
                    board.move(selected, row, col)
                    turn = RED if turn == BLUE else BLUE
                    selected = None
                elif piece != 0 and piece.color == turn:
                    selected = piece
   
main()

