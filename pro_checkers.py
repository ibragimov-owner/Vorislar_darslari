"""
checkers_modern_real.py
Real qoidalarga mos, silliq animatsiyali, PvP va AI vs rejimlari bilan Pygame shashkasi.
Yaratilgan: ChatGPT yordamida (Muhim: pygame kerak)
"""

import pygame
import sys
import copy
import math
import time
import random

# --- Konfiguratsiya ---
pygame.init()
WIDTH, HEIGHT = 800, 880   # pastki qism menyu uchun biroz balandroq
BOARD_SIZE = 800
ROWS, COLS = 8, 8
SQUARE = BOARD_SIZE // COLS
FPS = 60

# Ranglar
WHITE = (245, 245, 245)
BLACK = (18, 18, 18)
LIGHT_SQ = (235, 235, 235)
DARK_SQ = (50, 50, 50)
RED = (220, 70, 70)
BLUE = (60, 140, 220)
GOLD = (230, 200, 80)
GREEN_HIGHLIGHT = (80, 200, 120)
TRANSPARENT = (0, 0, 0, 0)
BG = (28, 30, 34)
POSSIBLE_MOVE_ALPHA = 120

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Modern Real Checkers")
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont("arial", 18)
BIG_FONT = pygame.font.SysFont("arial", 28)

# --- Data klasslar ---
class Piece:
    PADDING = 12
    OUTLINE = 3

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.calc_pos()

        # Vizual pozitsiya (aniq sirpanish animatsiyasi uchun)
        self.vis_x = self.x
        self.vis_y = self.y

    def calc_pos(self):
        self.x = SQUARE * self.col + SQUARE // 2
        self.y = SQUARE * self.row + SQUARE // 2

    def make_king(self):
        self.king = True

    def draw(self, win, selected=False, highlight=False):
        # shadow / glow (shaеdon)
        radius = SQUARE // 2 - self.PADDING
        # Oval shadow
        shadow_surf = pygame.Surface((SQUARE, SQUARE), pygame.SRCALPHA)
        pygame.draw.circle(shadow_surf, (*self.color, 200), (SQUARE//2, SQUARE//2+6), radius+4)
        win.blit(shadow_surf, (self.vis_x - SQUARE//2, self.vis_y - SQUARE//2))

        # main circle (slightly translucent for modern look)
        main_surf = pygame.Surface((SQUARE, SQUARE), pygame.SRCALPHA)
        pygame.draw.circle(main_surf, (*self.color, 235), (SQUARE//2, SQUARE//2), radius)
        win.blit(main_surf, (self.vis_x - SQUARE//2, self.vis_y - SQUARE//2))

        # Outline
        pygame.draw.circle(win, BLACK, (int(self.vis_x), int(self.vis_y)), radius, 2)

        # King mark
        if self.king:
            # small crown — a ring
            pygame.draw.circle(win, GOLD, (int(self.vis_x), int(self.vis_y)), radius//2, 3)

        # selected outline
        if selected:
            pygame.draw.circle(win, GREEN_HIGHLIGHT, (int(self.vis_x), int(self.vis_y)), radius+6, 4)

    def update_visual_pos(self, dt=1):
        # Smooth move toward self.x, self.y
        speed = 12  # higher is faster
        dx = self.x - self.vis_x
        dy = self.y - self.vis_y
        self.vis_x += dx * min(1, speed * dt / 60)
        self.vis_y += dy * min(1, speed * dt / 60)

    def copy(self):
        p = Piece(self.row, self.col, self.color)
        p.king = self.king
        p.vis_x, p.vis_y = self.vis_x, self.vis_y
        return p

class Board:
    def __init__(self):
        # board[row][col] = Piece or 0
        self.board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        self.create_board()

    def create_board(self):
        for r in range(ROWS):
            for c in range(COLS):
                if (r + c) % 2 == 1:
                    if r < 3:
                        self.board[r][c] = Piece(r, c, RED)
                    elif r > 4:
                        self.board[r][c] = Piece(r, c, BLUE)
                    else:
                        self.board[r][c] = 0
                else:
                    self.board[r][c] = 0

    def draw_squares(self, win):
        # Gradient-like board using two colors
        for r in range(ROWS):
            for c in range(COLS):
                rect = (c*SQUARE, r*SQUARE, SQUARE, SQUARE)
                color = DARK_SQ if (r + c) % 2 else LIGHT_SQ
                pygame.draw.rect(win, color, rect)

    def draw(self, win, selected_piece=None, valid_moves=None):
        self.draw_squares(win)
        # highlight valid moves (semi-transparent circles)
        if valid_moves:
            surf = pygame.Surface((SQUARE, SQUARE), pygame.SRCALPHA)
            for mv, capture in valid_moves.items():
                r, c = mv
                surf.fill((0,0,0,0))
                pygame.draw.circle(surf, (*GREEN_HIGHLIGHT, POSSIBLE_MOVE_ALPHA), (SQUARE//2, SQUARE//2), 18)
                win.blit(surf, (c*SQUARE, r*SQUARE))

        # draw pieces
        for r in range(ROWS):
            for c in range(COLS):
                piece = self.board[r][c]
                if piece != 0:
                    is_selected = (selected_piece is not None and piece is selected_piece)
                    piece.update_visual_pos()
                    piece.draw(win, selected=is_selected)

    def move(self, piece, dest_row, dest_col):
        # Shift board positions
        self.board[piece.row][piece.col] = 0
        self.board[dest_row][dest_col] = piece
        piece.row = dest_row
        piece.col = dest_col
        piece.calc_pos()
        # Kinging
        if piece.color == BLUE and dest_row == 0:
            piece.make_king()
        if piece.color == RED and dest_row == ROWS - 1:
            piece.make_king()

    def remove(self, pieces):
        for p in pieces:
            self.board[p.row][p.col] = 0

    def get_piece(self, row, col):
        if 0 <= row < ROWS and 0 <= col < COLS:
            return self.board[row][col]
        return None

    def get_all_pieces(self, color):
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                p = self.board[r][c]
                if p != 0 and p.color == color:
                    res.append(p)
        return res

    def copy(self):
        newb = Board()
        newb.board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                p = self.board[r][c]
                if p != 0:
                    newb.board[r][c] = p.copy()
        return newb

# --- O'yin mantiqi (qoidalar) ---
def inside_board(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS

def get_valid_moves(board: Board, piece: Piece, must_capture_only=False):
    """
    Return dictionary of moves:
      { (dest_row, dest_col): [list_of_captured_pieces...] }
    Enforces real checkers rules:
      - Diagonal moves only
      - Simple move: one diagonal forward (except for kings)
      - Capture: jump over adjacent opponent piece to empty square beyond
      - Multi-jump chaining supported
      - If any capture exists for player, non-capture moves are not allowed (handled externally)
    """
    moves = {}

    directions = []
    if piece.king:
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    else:
        # BLUE moves up (row decreases), RED moves down (row increases)
        if piece.color == BLUE:
            directions = [(-1, -1), (-1, 1)]
        else:
            directions = [(1, -1), (1, 1)]

    # First look for captures (including multi-jump via recursion)
    def search_captures(board_state: Board, cur_piece: Piece, start_r, start_c, visited):
        found = {}
        any_capture = False
        for dr, dc in [(-1,-1), (-1,1), (1,-1), (1,1)]:
            nr, nc = start_r + dr, start_c + dc
            jr, jc = start_r + 2*dr, start_c + 2*dc
            if inside_board(nr, nc) and inside_board(jr, jc):
                mid = board_state.get_piece(nr, nc)
                dest = board_state.get_piece(jr, jc)
                if mid != 0 and mid.color != cur_piece.color and dest == 0:
                    # simulate capture
                    new_board = board_state.copy()
                    # find and remove mid on new_board
                    mid_copy = new_board.get_piece(nr, nc)
                    cur_copy = new_board.get_piece(start_r, start_c)
                    new_board.board[start_r][start_c] = 0
                    new_board.board[jr][jc] = cur_copy
                    cur_copy.row, cur_copy.col = jr, jc
                    # remove captured
                    new_board.board[nr][nc] = 0

                    # continue searching from new location
                    deeper = search_captures(new_board, cur_copy, jr, jc, visited + [(nr, nc)])
                    if deeper:
                        for k, v in deeper.items():
                            found[k] = [(nr, nc)] + v
                    else:
                        found[(jr, jc)] = [(nr, nc)]
                    any_capture = True
        return found

    captures = search_captures(board, piece, piece.row, piece.col, [])
    if captures:
        return captures

    # If must_capture_only and no captures, return empty dict
    if must_capture_only:
        return {}

    # Simple moves
    for dr, dc in directions:
        nr, nc = piece.row + dr, piece.col + dc
        if inside_board(nr, nc) and board.get_piece(nr, nc) == 0:
            moves[(nr, nc)] = []
    return moves

def any_player_must_capture(board: Board, color):
    for p in board.get_all_pieces(color):
        caps = get_valid_moves(board, p, must_capture_only=True)
        if caps:
            return True
    return False

# --- AI (minimax with alpha-beta) ---
def evaluate_board(board: Board, ai_color):
    # Simple heuristic: piece count + king weight + advancement
    score = 0
    for r in range(ROWS):
        for c in range(COLS):
            p = board.board[r][c]
            if p != 0:
                val = 1.0
                if p.king:
                    val = 2.0
                # advancement bonus: encourage moving forward for non-king
                adv = 0
                if not p.king:
                    if p.color == BLUE:
                        adv = (ROWS - r) * 0.02
                    else:
                        adv = (r + 1) * 0.02
                total = val + adv
                if p.color == ai_color:
                    score += total
                else:
                    score -= total
    return score

def get_all_moves_for_player(board: Board, color):
    moves = []  # list of tuples (piece, move_dest, captures_list)
    must_capture = any_player_must_capture(board, color)
    for p in board.get_all_pieces(color):
        valid = get_valid_moves(board, p, must_capture_only=must_capture)
        for dest, caps in valid.items():
            moves.append((p, dest, caps))
    return moves

def simulate_move(board: Board, piece: Piece, dest, captures):
    newb = board.copy()
    # find corresponding piece in newb
    p = newb.get_piece(piece.row, piece.col)
    dr, dc = dest
    # perform move
    newb.move(p, dr, dc)
    # remove captures
    rem = []
    for cap in captures:
        r, c = cap
        cp = newb.get_piece(r, c)
        if cp != 0:
            rem.append(cp)
    newb.remove(rem)
    # king if applicable
    return newb

def minimax(board: Board, depth, alpha, beta, maximizing, ai_color):
    # terminal or depth
    if depth == 0:
        return evaluate_board(board, ai_color), None
    color = ai_color if maximizing else (RED if ai_color == BLUE else BLUE)
    moves = get_all_moves_for_player(board, color)
    if not moves:
        # no moves -> losing position
        return evaluate_board(board, ai_color) * (100 if maximizing else -100), None

    best_move = None
    if maximizing:
        max_eval = -math.inf
        for (p, dest, caps) in moves:
            nb = simulate_move(board, p, dest, caps)
            eval_score, _ = minimax(nb, depth-1, alpha, beta, False, ai_color)
            if eval_score > max_eval:
                max_eval = eval_score
                best_move = (p, dest, caps)
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        for (p, dest, caps) in moves:
            nb = simulate_move(board, p, dest, caps)
            eval_score, _ = minimax(nb, depth-1, alpha, beta, True, ai_color)
            if eval_score < min_eval:
                min_eval = eval_score
                best_move = (p, dest, caps)
            beta = min(beta, eval_score)
            if beta <= alpha:
                break
        return min_eval, best_move

# --- O'yin suli (Game controller) ---
class Game:
    def __init__(self, ai_mode=False, ai_color=RED, ai_depth=4):
        self.board = Board()
        self.selected = None
        self.valid_moves = {}
        self.turn = BLUE  # Blue starts (can be changed)
        self.ai_mode = ai_mode
        self.ai_color = ai_color
        self.ai_depth = ai_depth
        self.move_history = []
        self.winner = None
        self.animating = False

    def reset(self):
        self.__init__(ai_mode=self.ai_mode, ai_color=self.ai_color, ai_depth=self.ai_depth)

    def select(self, row, col):
        if self.animating:
            return False
        piece = self.board.get_piece(row, col)
        if self.selected:
            # try to move to clicked cell if in valid_moves
            if (row, col) in self.valid_moves:
                captures = self.valid_moves[(row, col)]
                self.perform_move(self.selected, (row, col), captures)
                return True
            else:
                # change selection if own piece selected
                if piece != 0 and piece.color == self.turn:
                    self.selected = piece
                    self.update_valid_moves()
                else:
                    # deselect
                    self.selected = None
                    self.valid_moves = {}
                return False
        else:
            if piece != 0 and piece.color == self.turn:
                self.selected = piece
                self.update_valid_moves()
                return True
        return False

    def update_valid_moves(self):
        if self.selected:
            must_capture = any_player_must_capture(self.board, self.turn)
            self.valid_moves = get_valid_moves(self.board, self.selected, must_capture_only=must_capture)
        else:
            self.valid_moves = {}

    def perform_move(self, piece, dest, captures):
        # animate move
        dest_r, dest_c = dest
        # If capture list non-empty, we must perform possible multi-jump sequence
        # We'll remove captured pieces and move the piece.
        # For multi-jump we let rules enforce additional captures after moving.
        # Perform smooth visual movement by updating visual pos gradually.

        # animate position change
        self.animating = True
        start_x, start_y = piece.vis_x, piece.vis_y
        end_x = dest_c * SQUARE + SQUARE//2
        end_y = dest_r * SQUARE + SQUARE//2
        frames = 18
        for i in range(1, frames+1):
            t = i / frames
            piece.vis_x = start_x + (end_x - start_x) * t
            piece.vis_y = start_y + (end_y - start_y) * t
            draw(WIN, self)
            pygame.display.update()
            CLOCK.tick(FPS)
        # finalize move in board state
        # remove captured pieces
        cap_pieces = []
        for (r,c) in captures:
            cp = self.board.get_piece(r, c)
            if cp != 0:
                cap_pieces.append(cp)
        self.board.remove(cap_pieces)
        # move piece
        self.board.move(piece, dest_r, dest_c)
        # record move
        self.move_history.append(((piece.color, piece.row, piece.col), dest, captures))
        # After capture, check if there is additional capture from new pos (multi-jump)
        more_caps = get_valid_moves(self.board, piece, must_capture_only=True)
        if more_caps:
            # Player must continue capturing with same piece — keep it selected
            self.selected = piece
            self.valid_moves = more_caps
            # do not swap turn
        else:
            # end of turn
            self.selected = None
            self.valid_moves = {}
            self.turn = RED if self.turn == BLUE else BLUE
        self.animating = False

    def ai_move_if_needed(self):
        if self.ai_mode and self.turn == self.ai_color and not self.animating:
            # Simple delay so user can perceive turn change
            pygame.time.delay(200)
            # Use minimax to pick move
            _, best = minimax(self.board, self.ai_depth, -math.inf, math.inf, True, self.ai_color)
            if best is None:
                # No move -> lose
                self.winner = BLUE if self.ai_color == RED else RED
                return
            piece, dest, caps = best
            # find corresponding piece instance on current board (minimax used copies)
            real_piece = self.board.get_piece(piece.row, piece.col)
            if real_piece is None or real_piece == 0:
                # fallback: recompute moves to find one valid
                moves = get_all_moves_for_player(self.board, self.ai_color)
                if not moves:
                    self.winner = BLUE if self.ai_color == RED else RED
                    return
                p, dest, caps = random.choice(moves)
                real_piece = self.board.get_piece(p.row, p.col)
            self.perform_move(real_piece, dest, caps)

    def check_winner(self):
        # Winner if opponent has no pieces or no valid moves
        for color in (BLUE, RED):
            pieces = self.board.get_all_pieces(color)
            if not pieces:
                self.winner = RED if color == BLUE else BLUE
                return True
            moves = get_all_moves_for_player(self.board, color)
            if not moves:
                self.winner = RED if color == BLUE else BLUE
                return True
        return False

# --- UI, draw helpers ---
def draw_top_bar(win, text):
    # top small title
    rect = pygame.Rect(0, BOARD_SIZE, WIDTH, HEIGHT - BOARD_SIZE)
    pygame.draw.rect(win, BG, rect)
    t = FONT.render(text, True, WHITE)
    win.blit(t, (10, BOARD_SIZE+6))

def draw(window, game: Game):
    window.fill(BG)
    # Draw board and pieces
    game.board.draw(window, selected_piece=game.selected, valid_moves=game.valid_moves)
    # Bottom info
    draw_top_bar(window, f"Turn: {'BLUE' if game.turn==BLUE else 'RED'}    Mode: {'AI' if game.ai_mode else 'PvP'}    (Press R to reset, M to toggle mode)")
    # show menus
    if game.winner:
        txt = BIG_FONT.render(f"Winner: {'BLUE' if game.winner==BLUE else 'RED'}", True, WHITE)
        window.blit(txt, (WIDTH//2 - txt.get_width()//2, BOARD_SIZE + 8))

# Map mouse pos to row/col
def get_row_col_from_mouse(pos):
    x, y = pos
    if y >= BOARD_SIZE:
        return None, None
    row = y // SQUARE
    col = x // SQUARE
    return row, col

# --- Menu and main loop ---
def menu_screen():
    # Simple start menu to choose PvP or AI
    run = True
    choice = None
    while run:
        WIN.fill(BG)
        title = BIG_FONT.render("Modern Real Checkers", True, WHITE)
        WIN.blit(title, (WIDTH//2 - title.get_width()//2, 80))
        sub = FONT.render("Choose mode:", True, WHITE)
        WIN.blit(sub, (WIDTH//2 - sub.get_width()//2, 150))

        # Buttons
        btn_w, btn_h = 300, 60
        x = WIDTH//2 - btn_w//2
        y1 = 230
        y2 = 310
        y3 = 390

        mx, my = pygame.mouse.get_pos()
        # PvP
        rect1 = pygame.Rect(x, y1, btn_w, btn_h)
        rect2 = pygame.Rect(x, y2, btn_w, btn_h)
        rect3 = pygame.Rect(x, y3, btn_w, btn_h)

        pygame.draw.rect(WIN, DARK_SQ, rect1, border_radius=8)
        pygame.draw.rect(WIN, DARK_SQ, rect2, border_radius=8)
        pygame.draw.rect(WIN, DARK_SQ, rect3, border_radius=8)

        t1 = FONT.render("1) PvP (Two players on one PC)", True, WHITE)
        t2 = FONT.render("2) Play vs AI (You are BLUE, AI RED)", True, WHITE)
        t3 = FONT.render("3) Play vs AI (You are RED, AI BLUE)", True, WHITE)

        WIN.blit(t1, (x + 20, y1 + 18))
        WIN.blit(t2, (x + 20, y2 + 18))
        WIN.blit(t3, (x + 20, y3 + 18))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect1.collidepoint((mx, my)):
                    choice = ("pvp", None)
                    run = False
                if rect2.collidepoint((mx, my)):
                    choice = ("ai", RED)
                    run = False
                if rect3.collidepoint((mx, my)):
                    choice = ("ai", BLUE)
                    run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    choice = ("pvp", None); run = False
                if event.key == pygame.K_2:
                    choice = ("ai", RED); run = False
                if event.key == pygame.K_3:
                    choice = ("ai", BLUE); run = False

        pygame.display.update()
        CLOCK.tick(FPS)
    return choice

def main():
    # Show menu
    mode, ai_color = menu_screen()
    ai_mode = (mode == "ai")
    game = Game(ai_mode=ai_mode, ai_color=ai_color if ai_mode else None, ai_depth=4)

    running = True
    while running:
        CLOCK.tick(FPS)

        # AI move if it's AI's turn
        if game.ai_mode and game.turn == game.ai_color and not game.winner:
            game.ai_move_if_needed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                if row is not None:
                    # selection & move
                    game.select(row, col)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game.reset()
                if event.key == pygame.K_m:
                    # toggle mode quickly
                    game.ai_mode = not game.ai_mode
                    if game.ai_mode:
                        game.ai_color = RED
                    else:
                        game.ai_color = None

        # check winner
        if not game.winner:
            game.check_winner()

        draw(WIN, game)
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
