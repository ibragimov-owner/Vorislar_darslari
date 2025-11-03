"""
checkers_modern_full.py
Modern, real-ish checkers with:
- PvP and simple (random-prefer-capture) AI
- Smooth non-blocking animations (no pygame.time.delay)
- Realistic moves: diagonal moves, capture logic for men (jump 2), king slides long diagonals
- Multi-jump for men supported
- Pause menu, Restart, Menu, Day/Night toggle
- Game timer (elapsed time)
Keys:
- R: restart
- P: pause / resume
- M: go to menu
- D: toggle Day/Night
- ESC / close: quit
"""

import pygame, sys, math, random, time, copy

pygame.init()

# --- Config ---
WIDTH, HEIGHT = 800, 880
BOARD_SIZE = 800
ROWS, COLS = 8, 8
SQUARE = BOARD_SIZE // COLS
FPS = 60

# Colors
WHITE = (245, 245, 245)
BLACK = (18, 18, 18)
LIGHT_SQ_DAY = (237, 235, 232)
DARK_SQ_DAY = (60, 60, 60)
LIGHT_SQ_NIGHT = (30, 30, 36)
DARK_SQ_NIGHT = (15, 15, 20)
RED = (200, 60, 60)
BLUE = (60, 130, 220)
GOLD = (230, 200, 90)
GREEN_HL = (80, 200, 120)
BG_DAY = (34, 36, 40)
BG_NIGHT = (8, 10, 14)
TEXT = (235, 235, 235)
POSSIBLE_ALPHA = 140

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Modern Real Checkers — Full")
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 18)
BIG = pygame.font.SysFont("Arial", 28)

# --- Piece & Board Classes ---
class Piece:
    PADDING = 12
    OUTLINE = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.calc_pos()
        # Visual position for smooth movement
        self.vis_x = self.x
        self.vis_y = self.y

    def calc_pos(self):
        self.x = self.col * SQUARE + SQUARE // 2
        self.y = self.row * SQUARE + SQUARE // 2

    def make_king(self):
        self.king = True

    def draw(self, win, selected=False, day=True):
        radius = SQUARE // 2 - self.PADDING
        # shadow
        shadow = pygame.Surface((SQUARE, SQUARE), pygame.SRCALPHA)
        shadow_color = (*self.color, 200)
        pygame.draw.circle(shadow, shadow_color, (SQUARE//2, SQUARE//2 + 6), radius+4)
        win.blit(shadow, (self.vis_x - SQUARE//2, self.vis_y - SQUARE//2))
        # main
        surf = pygame.Surface((SQUARE, SQUARE), pygame.SRCALPHA)
        pygame.draw.circle(surf, (*self.color, 235), (SQUARE//2, SQUARE//2), radius)
        win.blit(surf, (self.vis_x - SQUARE//2, self.vis_y - SQUARE//2))
        # outline
        pygame.draw.circle(win, BLACK, (int(self.vis_x), int(self.vis_y)), radius, self.OUTLINE)
        # king marker
        if self.king:
            pygame.draw.circle(win, GOLD, (int(self.vis_x), int(self.vis_y)), radius//2, 3)
        # selected highlight
        if selected:
            pygame.draw.circle(win, GREEN_HL, (int(self.vis_x), int(self.vis_y)), radius+6, 4)

    def update_vis(self, dt):
        # Smoothly move vis_x/y toward x/y
        speed = 18  # higher is faster
        dx = self.x - self.vis_x
        dy = self.y - self.vis_y
        self.vis_x += dx * min(1, speed * dt / (1000/60))
        self.vis_y += dy * min(1, speed * dt / (1000/60))

    def copy(self):
        p = Piece(self.row, self.col, self.color)
        p.king = self.king
        p.vis_x, p.vis_y = self.vis_x, self.vis_y
        return p

class Board:
    def __init__(self):
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

    def draw_squares(self, win, day=True):
        if day:
            light, dark = LIGHT_SQ_DAY, DARK_SQ_DAY
        else:
            light, dark = LIGHT_SQ_NIGHT, DARK_SQ_NIGHT
        for r in range(ROWS):
            for c in range(COLS):
                color = dark if (r + c) % 2 else light
                pygame.draw.rect(win, color, (c*SQUARE, r*SQUARE, SQUARE, SQUARE))

    def draw(self, win, selected_piece=None, valid_moves=None, day=True):
        # board
        self.draw_squares(win, day=day)
        # valid moves overlay
        if valid_moves:
            overlay = pygame.Surface((SQUARE, SQUARE), pygame.SRCALPHA)
            for mv, caps in valid_moves.items():
                r, c = mv
                overlay.fill((0,0,0,0))
                pygame.draw.circle(overlay, (*GREEN_HL, POSSIBLE_ALPHA), (SQUARE//2, SQUARE//2), 18)
                win.blit(overlay, (c*SQUARE, r*SQUARE))
        # pieces
        for r in range(ROWS):
            for c in range(COLS):
                p = self.board[r][c]
                if p != 0:
                    sel = (selected_piece is p)
                    p.update_vis(dt=1)  # small step; actual dt controlled globally
                    p.draw(win, selected=sel, day=day)

    def get_piece(self, r, c):
        if 0 <= r < ROWS and 0 <= c < COLS:
            return self.board[r][c]
        return None

    def move(self, piece, r, c):
        self.board[piece.row][piece.col] = 0
        self.board[r][c] = piece
        piece.row, piece.col = r, c
        piece.calc_pos()
        if piece.color == BLUE and r == 0:
            piece.make_king()
        if piece.color == RED and r == ROWS - 1:
            piece.make_king()

    def remove(self, pieces):
        for p in pieces:
            if p is None: continue
            # ensure it's still on board
            if 0 <= p.row < ROWS and 0 <= p.col < COLS and self.board[p.row][p.col] is p:
                self.board[p.row][p.col] = 0

    def get_all_pieces(self, color):
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                p = self.board[r][c]
                if p != 0 and p.color == color:
                    res.append(p)
        return res

    def copy(self):
        nb = Board()
        nb.board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        for r in range(ROWS):
            for c in range(COLS):
                p = self.board[r][c]
                if p != 0:
                    nb.board[r][c] = p.copy()
        return nb

# --- Rules and move generation ---
def inside(r,c):
    return 0 <= r < ROWS and 0 <= c < COLS

def get_valid_moves(board: Board, piece: Piece, must_capture_only=False):
    """
    returns dict: { (r,c): [ (cap_r,cap_c), ... ] }
    - For men: simple moves = 1-step diagonals forward (color-dependent)
      captures = jump over adjacent opponent to empty square (2-step), supports multi-jump via recursion
    - For kings: simple moves = any distance along diagonals until blocked
      captures for kings implemented as jump over adjacent opponent to immediate landing square (one-step beyond),
      and multi-jump supported by recursion by moving piece and removing captured in simulation.
    """
    moves = {}
    directions = [(-1,-1), (-1,1), (1,-1), (1,1)]
    # helper recursive search for captures (simulate board)
    def search_captures(bd: Board, cur_piece: Piece, r0, c0, visited):
        found = {}
        any_cap = False
        for dr,dc in directions:
            nr, nc = r0 + dr, c0 + dc
            jr, jc = r0 + 2*dr, c0 + 2*dc
            if inside(nr,nc) and inside(jr,jc):
                mid = bd.get_piece(nr,nc)
                dest = bd.get_piece(jr,jc)
                if mid != 0 and mid.color != cur_piece.color and dest == 0:
                    # simulate on copy
                    nb = bd.copy()
                    # locate corresponding cur_piece in nb
                    cp = nb.get_piece(r0, c0)
                    mid_cp = nb.get_piece(nr, nc)
                    nb.board[r0][c0] = 0
                    nb.board[jr][jc] = cp
                    cp.row, cp.col = jr, jc
                    nb.board[nr][nc] = 0
                    deeper = search_captures(nb, cp, jr, jc, visited + [(nr,nc)])
                    if deeper:
                        for k,v in deeper.items():
                            found[k] = [(nr,nc)] + v
                    else:
                        found[(jr,jc)] = [(nr,nc)]
                    any_cap = True
        return found

    # KING logic: sliding moves
    if piece.king:
        # captures first (simulate capture style - only immediate jump over adjacent piece to next empty)
        captures = {}
        for dr,dc in directions:
            r,c = piece.row, piece.col
            nr, nc = r+dr, c+dc
            if inside(nr,nc):
                mid = board.get_piece(nr,nc)
                if mid != 0 and mid.color != piece.color:
                    jr, jc = nr+dr, nc+dc
                    if inside(jr,jc) and board.get_piece(jr,jc) == 0:
                        # king can land on jr,jc (we don't allow long landing beyond the immediate square for simplicity)
                        # simulate recursion
                        nb = board.copy()
                        cp = nb.get_piece(piece.row, piece.col)
                        nb.board[piece.row][piece.col] = 0
                        nb.board[jr][jc] = cp
                        cp.row, cp.col = jr, jc
                        nb.board[nr][nc] = 0
                        deeper = search_captures(nb, cp, jr, jc, [(nr,nc)])
                        if deeper:
                            for k,v in deeper.items():
                                captures[k] = [(nr,nc)] + v
                        else:
                            captures[(jr,jc)] = [(nr,nc)]
        if captures:
            return captures
        if must_capture_only:
            return {}
        # simple sliding moves (any empty along each diagonal)
        for dr,dc in directions:
            r,c = piece.row+dr, piece.col+dc
            while inside(r,c) and board.get_piece(r,c) == 0:
                moves[(r,c)] = []
                r += dr; c += dc
        return moves

    # MEN logic
    # determine forward directions
    if piece.color == BLUE:
        fdirs = [(-1,-1), (-1,1)]
    else:
        fdirs = [(1,-1), (1,1)]

    # captures (search all 4 diagonals for captures; men can capture backward too)
    captures = search_captures(board, piece, piece.row, piece.col, [])
    if captures:
        return captures

    if must_capture_only:
        return {}

    # simple moves only forward
    for dr,dc in fdirs:
        nr, nc = piece.row + dr, piece.col + dc
        if inside(nr,nc) and board.get_piece(nr,nc) == 0:
            moves[(nr,nc)] = []
    return moves

def any_capture_for_player(board: Board, color):
    for p in board.get_all_pieces(color):
        caps = get_valid_moves(board, p, must_capture_only=True)
        if caps:
            return True
    return False

# --- Simple AI (dumb) ---
def ai_choose_move(board: Board, ai_color):
    # choose capture move if available; else random valid move
    moves = []
    must = any_capture_for_player(board, ai_color)
    for p in board.get_all_pieces(ai_color):
        valid = get_valid_moves(board, p, must_capture_only=must)
        for dest, caps in valid.items():
            moves.append((p, dest, caps))
    if not moves:
        return None
    # prefer captures
    captures = [m for m in moves if len(m[2])>0]
    if captures:
        return random.choice(captures)
    return random.choice(moves)

# --- Game Controller with non-blocking animation ---
class Game:
    def __init__(self, ai_mode=False, ai_color=RED):
        self.board = Board()
        self.selected = None
        self.valid_moves = {}
        self.turn = BLUE
        self.ai_mode = ai_mode
        self.ai_color = ai_color if ai_mode else None
        self.move_history = []
        self.winner = None
        self.animation = None  # dict describing ongoing animation
        self.paused = False
        self.start_time = time.time()
        self.pause_time_acc = 0.0
        self.last_update = pygame.time.get_ticks()
        self.day = True  # day mode default
        self.menu = False

    def reset(self):
        self.__init__(ai_mode=self.ai_mode, ai_color=self.ai_color)

    def elapsed(self):
        if self.paused:
            return self.pause_time_acc
        return time.time() - self.start_time

    def select(self, r, c):
        if self.paused or self.animation:
            return False
        piece = self.board.get_piece(r,c)
        if self.selected:
            if (r,c) in self.valid_moves:
                caps = self.valid_moves[(r,c)]
                self.start_move(self.selected, (r,c), caps)
                return True
            else:
                # change selection if selecting own piece
                if piece != 0 and piece.color == self.turn:
                    self.selected = piece
                    self.update_valid_moves()
                    return True
                else:
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
        if not self.selected:
            self.valid_moves = {}
            return
        must = any_capture_for_player(self.board, self.turn)
        self.valid_moves = get_valid_moves(self.board, self.selected, must_capture_only=must)

    def start_move(self, piece: Piece, dest, captures):
        # Set up non-blocking animation: record start, end, captured cells
        dest_r, dest_c = dest
        self.animation = {
            'piece': piece,
            'start_vis': (piece.vis_x, piece.vis_y),
            'end_vis': (dest_c * SQUARE + SQUARE//2, dest_r * SQUARE + SQUARE//2),
            'frames': 14,
            'frame': 0,
            'dest': dest,
            'captures': captures
        }
        # preemptively update logical board for multi-jump detection AFTER animation completes.
        # Do NOT modify board now; we'll finalize on animation end.

    def finish_move(self):
        # Called when animation completes
        anim = self.animation
        piece = anim['piece']
        dest_r, dest_c = anim['dest']
        captures = anim['captures']
        # remove captured pieces
        cap_pieces = []
        for (rr,cc) in captures:
            p = self.board.get_piece(rr,cc)
            if p != 0 and p is not None:
                cap_pieces.append(p)
        self.board.remove(cap_pieces)
        # move logical piece
        self.board.move(piece, dest_r, dest_c)
        # record move
        self.move_history.append(((piece.color, ), (piece.row, piece.col), anim['dest'], captures))
        # check for extra captures (multi-jump)
        more_caps = get_valid_moves(self.board, piece, must_capture_only=True)
        if more_caps:
            # keep same turn and keep piece selected
            self.selected = piece
            self.valid_moves = more_caps
            # Note: piece.vis_x,y already at dest
        else:
            # end turn
            self.selected = None
            self.valid_moves = {}
            self.turn = RED if self.turn == BLUE else BLUE
        self.animation = None

    def update(self, dt):
        # dt in milliseconds
        # progress animation if any
        if self.animation:
            anim = self.animation
            anim['frame'] += 1
            t = anim['frame'] / anim['frames']
            sx, sy = anim['start_vis']
            ex, ey = anim['end_vis']
            piece = anim['piece']
            piece.vis_x = sx + (ex - sx)*t
            piece.vis_y = sy + (ey - sy)*t
            if anim['frame'] >= anim['frames']:
                # finalize
                piece.vis_x, piece.vis_y = ex, ey
                self.finish_move()

        # AI move if needed (non-blocking: pick and start animation)
        if not self.paused and not self.animation and self.ai_mode and self.turn == self.ai_color and not self.winner:
            # small delay between AI moves: choose after short pause (simulate thinking)
            # We'll pick immediately (AI is dumb)
            choice = ai_choose_move(self.board, self.ai_color)
            if choice is None:
                self.winner = BLUE if self.ai_color == RED else RED
            else:
                p, dest, caps = choice
                # find real piece on board by position
                rp = self.board.get_piece(p.row, p.col)
                if rp == 0 or rp is None:
                    # fallback: random valid
                    moves = []
                    must = any_capture_for_player(self.board, self.ai_color)
                    for pp in self.board.get_all_pieces(self.ai_color):
                        valid = get_valid_moves(self.board, pp, must_capture_only=must)
                        for d,caps2 in valid.items():
                            moves.append((pp,d,caps2))
                    if moves:
                        rp, dest, caps = random.choice(moves)
                    else:
                        self.winner = BLUE if self.ai_color == RED else RED
                        return
                self.start_move(rp, dest, caps)

        # update all pieces visual toward their logical positions (to keep smoothness after e.g. reset)
        for r in range(ROWS):
            for c in range(COLS):
                p = self.board.get_piece(r,c)
                if p != 0:
                    p.update_vis(dt)

        # check winner
        if not self.winner:
            for color in (BLUE, RED):
                pieces = self.board.get_all_pieces(color)
                if not pieces:
                    self.winner = RED if color == BLUE else BLUE
                    break
                # if player has no moves
                if not any(get_all_moves_for_player(self.board, color)):
                    self.winner = RED if color == BLUE else BLUE
                    break

    def toggle_pause(self):
        self.paused = not self.paused
        if self.paused:
            # accumulate elapsed
            self.pause_time_acc = time.time() - self.start_time
        else:
            # resume: adjust start_time so elapsed excludes pause period
            self.start_time = time.time() - self.pause_time_acc

# helper: gather all moves for a player (used for winner check)
def get_all_moves_for_player(board: Board, color):
    res = []
    must = any_capture_for_player(board, color)
    for p in board.get_all_pieces(color):
        valid = get_valid_moves(board, p, must_capture_only=must)
        for dest, caps in valid.items():
            res.append((p,dest,caps))
    return res

# --- UI / Draw helpers ---
def draw_top_bar(win, game: Game):
    # bottom area reserved at y = BOARD_SIZE .. HEIGHT
    rect = pygame.Rect(0, BOARD_SIZE, WIDTH, HEIGHT - BOARD_SIZE)
    bg = BG_DAY if game.day else BG_NIGHT
    pygame.draw.rect(win, bg, rect)
    turn_txt = "BLUE" if game.turn == BLUE else "RED"
    mode_txt = "AI" if game.ai_mode else "PvP"
    s = f"Turn: {turn_txt}    Mode: {mode_txt}    (R:restart  P:pause  M:menu  D:day/night)"
    t = FONT.render(s, True, TEXT)
    win.blit(t, (10, BOARD_SIZE+6))
    # timer
    elapsed = int(game.elapsed())
    mins = elapsed // 60
    secs = elapsed % 60
    tt = FONT.render(f"Elapsed: {mins:02d}:{secs:02d}", True, TEXT)
    win.blit(tt, (WIDTH - tt.get_width() - 10, BOARD_SIZE+6))
    if game.winner:
        wb = BIG.render(f"Winner: {'BLUE' if game.winner==BLUE else 'RED'}", True, TEXT)
        win.blit(wb, (WIDTH//2 - wb.get_width()//2, BOARD_SIZE + 30))
    if game.paused:
        ptxt = BIG.render("PAUSED", True, TEXT)
        win.blit(ptxt, (WIDTH//2 - ptxt.get_width()//2, BOARD_SIZE + 30))

def draw(window, game: Game):
    window.fill(BG_DAY if game.day else BG_NIGHT)
    game.board.draw(window, selected_piece=game.selected, valid_moves=game.valid_moves, day=game.day)
    draw_top_bar(window, game)

def menu_screen():
    run = True
    choice = None
    while run:
        WIN.fill(BG_DAY)
        title = BIG.render("Modern Real Checkers", True, TEXT)
        WIN.blit(title, (WIDTH//2 - title.get_width()//2, 80))
        sub = FONT.render("Choose mode:", True, TEXT)
        WIN.blit(sub, (WIDTH//2 - sub.get_width()//2, 150))
        btn_w, btn_h = 360, 64
        x = WIDTH//2 - btn_w//2
        y1 = 230
        y2 = 314
        y3 = 398
        mx,my = pygame.mouse.get_pos()
        rect1 = pygame.Rect(x,y1,btn_w,btn_h)
        rect2 = pygame.Rect(x,y2,btn_w,btn_h)
        rect3 = pygame.Rect(x,y3,btn_w,btn_h)
        pygame.draw.rect(WIN, DARK_SQ_DAY if True else DARK_SQ_NIGHT, rect1, border_radius=8)
        pygame.draw.rect(WIN, DARK_SQ_DAY if True else DARK_SQ_NIGHT, rect2, border_radius=8)
        pygame.draw.rect(WIN, DARK_SQ_DAY if True else DARK_SQ_NIGHT, rect3, border_radius=8)
        t1 = FONT.render("1) PvP (Two players on one PC)", True, TEXT)
        t2 = FONT.render("2) Play vs AI (You are BLUE, AI RED)", True, TEXT)
        t3 = FONT.render("3) Play vs AI (You are RED, AI BLUE)", True, TEXT)
        WIN.blit(t1, (x+20, y1+20))
        WIN.blit(t2, (x+20, y2+20))
        WIN.blit(t3, (x+20, y3+20))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if rect1.collidepoint((mx,my)):
                    choice = ("pvp", None); run = False
                if rect2.collidepoint((mx,my)):
                    choice = ("ai", RED); run = False
                if rect3.collidepoint((mx,my)):
                    choice = ("ai", BLUE); run = False
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

# --- Main ---
def main():
    mode, ai_color = menu_screen()
    ai_mode = (mode == "ai")
    game = Game(ai_mode=ai_mode, ai_color=ai_color if ai_mode else None)
    running = True
    last_tick = pygame.time.get_ticks()
    while running:
        dt = pygame.time.get_ticks() - last_tick
        last_tick = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False; break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game.reset()
                if event.key == pygame.K_p:
                    game.toggle_pause()
                if event.key == pygame.K_m:
                    # go to menu: break to menu_screen
                    mode, ai_color = menu_screen()
                    ai_mode = (mode == "ai")
                    game = Game(ai_mode=ai_mode, ai_color=ai_color if ai_mode else None)
                if event.key == pygame.K_d:
                    game.day = not game.day
                if event.key == pygame.K_ESCAPE:
                    running = False; break
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not game.paused and not game.animation:
                    mx,my = pygame.mouse.get_pos()
                    if my < BOARD_SIZE:
                        row = my // SQUARE
                        col = mx // SQUARE
                        game.select(row, col)
        # update game
        if not game.paused:
            game.update(dt)

        # draw
        draw(WIN, game)
        pygame.display.update()
        CLOCK.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
