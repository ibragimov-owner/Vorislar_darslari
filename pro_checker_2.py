import pygame
import sys
import random
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

WIN = pygame.display.set_mode((WIDTH, HEIGHT + 100))
pygame.display.set_caption("Modern Real Checkers ♟️")

# RANG LAR
LIGHT = (238, 238, 210)
DARK = (118, 150, 86)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
GOLD = (255, 223, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NIGHT_BG = (25, 25, 25)
DAY_BG = (245, 245, 245)
BUTTON_COLOR = (180, 180, 180)
BUTTON_HOVER = (100, 200, 255)
BUTTON_PRESS = (50, 150, 255)

FPS = 60
font = pygame.font.SysFont("segoeui", 26)
timer_font = pygame.font.SysFont("consolas", 24)

clock = pygame.time.Clock()

# ----------- SHASHKA KLASSI ------------
class Checker:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

    def make_king(self):
        self.king = True

    def draw(self, win, highlight=False):
        radius = SQUARE_SIZE // 2 - 10
        x = self.col * SQUARE_SIZE + SQUARE_SIZE // 2
        y = self.row * SQUARE_SIZE + SQUARE_SIZE // 2
        if highlight:
            pygame.draw.circle(win, GREEN, (x, y), radius + 6, 4)
        pygame.draw.circle(win, self.color, (x, y), radius)
        if self.king:
            pygame.draw.circle(win, GOLD, (x, y), radius // 2, 3)

# ----------- BOARD KLASSI ------------
class Board:
    def __init__(self):
        self.board = []
        self.turn = BLACK
        self.selected = None
        self.valid_moves = {}
        self.create_board()

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if (row + col) % 2 == 0:
                    self.board[row].append(0)
                else:
                    if row < 3:
                        self.board[row].append(Checker(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Checker(row, col, BLACK))
                    else:
                        self.board[row].append(0)

    def draw_squares(self, win, night=False):
        for row in range(ROWS):
            for col in range(COLS):
                color = DARK if (row + col) % 2 else LIGHT
                if night:
                    color = (color[0]//2, color[1]//2, color[2]//2)
                pygame.draw.rect(win, color, (col*SQUARE_SIZE, row*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def get_checker(self, row, col):
        return self.board[row][col]

    def move(self, checker, row, col):
        self.board[checker.row][checker.col], self.board[row][col] = 0, checker
        checker.row, checker.col = row, col
        if row == 0 and checker.color == BLACK:
            checker.make_king()
        elif row == ROWS - 1 and checker.color == WHITE:
            checker.make_king()

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0

    def get_valid_moves(self, checker):
        moves = {}
        left = checker.col - 1
        right = checker.col + 1
        row = checker.row
        color = checker.color

        if color == BLACK or checker.king:
            moves.update(self._traverse_left(row - 1, max(row - 3, -1), -1, color, left))
            moves.update(self._traverse_right(row - 1, max(row - 3, -1), -1, color, right))
        if color == WHITE or checker.king:
            moves.update(self._traverse_left(row + 1, min(row + 3, ROWS), 1, color, left))
            moves.update(self._traverse_right(row + 1, min(row + 3, ROWS), 1, color, right))

        return moves

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                if last:
                    break
            elif current.color == color:
                break
            else:
                last = [current]
            left -= 1
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last
                if last:
                    break
            elif current.color == color:
                break
            else:
                last = [current]
            right += 1
        return moves

    def draw(self, win, night=False):
        self.draw_squares(win, night)
        for row in range(ROWS):
            for col in range(COLS):
                checker = self.board[row][col]
                if checker != 0:
                    highlight = (checker == self.selected)
                    checker.draw(win, highlight)

# ----------- O'YIN LOGIKASI ------------
class Game:
    def __init__(self, win):
        self._init()
        self.win = win
        self.start_time = pygame.time.get_ticks()

    def _init(self):
        self.board = Board()
        self.turn = BLACK
        self.selected = None
        self.night_mode = False
        self.paused = False
        self.ai_mode = False

    def reset(self):
        self._init()
        self.start_time = pygame.time.get_ticks()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        checker = self.board.get_checker(row, col)
        if checker != 0 and checker.color == self.turn:
            self.selected = checker
            self.valid_moves = self.board.get_valid_moves(checker)
            return True
        return False

    def _move(self, row, col):
        checker = self.selected
        if (row, col) in self.valid_moves:
            self.board.move(checker, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        return True

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == BLACK:
            self.turn = WHITE
        else:
            self.turn = BLACK

    def update(self):
        self.board.draw(self.win, self.night_mode)
        self.draw_buttons()
        self.draw_timer()
        pygame.display.update()

    def draw_buttons(self):
        buttons = [("Restart", 100), ("Night/Day", 300), ("Pause", 500), ("AI Mode", 700)]
        mouse = pygame.mouse.get_pos()
        for text, x in buttons:
            rect = pygame.Rect(x - 70, HEIGHT + 25, 140, 50)
            color = BUTTON_COLOR
            if rect.collidepoint(mouse):
                if pygame.mouse.get_pressed()[0]:
                    color = BUTTON_PRESS
                else:
                    color = BUTTON_HOVER
            pygame.draw.rect(self.win, color, rect, border_radius=10)
            label = font.render(text, True, BLACK)
            self.win.blit(label, (x - label.get_width()//2, HEIGHT + 35))

    def draw_timer(self):
        elapsed = (pygame.time.get_ticks() - self.start_time) // 1000
        label = timer_font.render(f"⏱️ Time: {elapsed}s", True, (255, 255, 255) if self.night_mode else (0, 0, 0))
        self.win.blit(label, (10, 10))

# ----------- ASOSIY SIKL ------------
def main():
    game = Game(WIN)
    run = True

    while run:
        clock.tick(FPS)
        if not game.paused:
            game.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                if y > HEIGHT:
                    if 30 < y - HEIGHT < 80:
                        if 30 < x < 170:
                            game.reset()
                        elif 230 < x < 370:
                            game.night_mode = not game.night_mode
                        elif 430 < x < 570:
                            game.paused = not game.paused
                        elif 630 < x < 770:
                            game.ai_mode = not game.ai_mode
                    continue

                row = y // SQUARE_SIZE
                col = x // SQUARE_SIZE
                game.select(row, col)

        if game.ai_mode and game.turn == WHITE and not game.paused:
            pygame.time.delay(500)
            moves = []
            for r in range(ROWS):
                for c in range(COLS):
                    piece = game.board.get_checker(r, c)
                    if piece != 0 and piece.color == WHITE:
                        valid = game.board.get_valid_moves(piece)
                        if valid:
                            for move, skip in valid.items():
                                moves.append((piece, move, skip))
            if moves:
                piece, move, skip = random.choice(moves)
                game.board.move(piece, move[0], move[1])
                if skip:
                    game.board.remove(skip)
                game.change_turn()

if __name__ == "__main__":
    main()
