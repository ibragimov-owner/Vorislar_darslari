import pygame
import copy
import math
import sys

pygame.init()

# --- Sozlamalar ---
WIDTH, HEIGHT = 640, 640
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

RED = (255, 50, 50)
BLACK = (40, 40, 40)
WHITE = (240, 240, 240)
BLUE = (50, 50, 255)
GREEN = (0, 200, 0)
GRAY = (100, 100, 100)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shashka (AI bilan)")

# --- Dastlabki taxta yaratish ---
def create_board():
    board = []
    for r in range(ROWS):
        board.append([])
        for c in range(COLS):
            if (r + c) % 2 == 0:
                board[r].append(None)
            else:
                if r < 3:
                    board[r].append('b')
                elif r > 4:
                    board[r].append('r')
                else:
                    board[r].append(None)
    return board

def draw_board(win, board):
    win.fill(GRAY)
    for r in range(ROWS):
        for c in range(COLS):
            color = WHITE if (r + c) % 2 == 0 else BLACK
            pygame.draw.rect(win, color, (c*SQUARE_SIZE, r*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            piece = board[r][c]
            if piece:
                color = RED if piece.lower() == 'r' else BLUE
                pygame.draw.circle(win, color, (c*SQUARE_SIZE + SQUARE_SIZE//2, r*SQUARE_SIZE + SQUARE_SIZE//2), 28)
                if piece.isupper():
                    # Shoh bo'lsa, ichiga yashil doira chizamiz
                    pygame.draw.circle(win, GREEN, (c*SQUARE_SIZE + SQUARE_SIZE//2, r*SQUARE_SIZE + SQUARE_SIZE//2), 10)

def in_bounds(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS

# ✅ TO‘G‘RILANGAN FUNKSIYA — AI xatosiz ishlaydi
def get_piece_moves(board, r, c):
    piece = board[r][c]
    if not piece:
        return []
    color = 'r' if piece.lower() == 'r' else 'b'
    king = piece.isupper()
    directions = []
    if color == 'r' or king:
        directions += [(-1, -1), (-1, 1)]
    if color == 'b' or king:
        directions += [(1, -1), (1, 1)]

    simple_moves = []
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if in_bounds(nr, nc) and board[nr][nc] is None:
            simple_moves.append(([(r, c), (nr, nc)], []))

    def dfs(board_state, cr, cc, path, captured):
        local_piece = board_state[cr][cc]
        local_king = local_piece.isupper()
        local_color = 'r' if local_piece.lower() == 'r' else 'b'
        local_dirs = []
        if local_color == 'r' or local_king:
            local_dirs += [(-1, -1), (-1, 1)]
        if local_color == 'b' or local_king:
            local_dirs += [(1, -1), (1, 1)]
        results = []
        for dr, dc in local_dirs:
            mid_r, mid_c = cr + dr, cc + dc
            land_r, land_c = cr + 2*dr, cc + 2*dc
            if in_bounds(mid_r, mid_c) and in_bounds(land_r, land_c):
                mid_piece = board_state[mid_r][mid_c]
                if mid_piece and mid_piece.lower() != local_piece.lower() and board_state[land_r][land_c] is None:
                    new_board = copy.deepcopy(board_state)
                    new_board[land_r][land_c] = new_board[cr][cc]
                    new_board[cr][cc] = None
                    new_board[mid_r][mid_c] = None
                    new_path = path + [(land_r, land_c)]
                    new_captured = captured + [(mid_r, mid_c)]
                    if new_board[land_r][land_c].islower() and (land_r == 0 or land_r == ROWS-1):
                        new_board[land_r][land_c] = new_board[land_r][land_c].upper()
                    deeper = dfs(new_board, land_r, land_c, new_path, new_captured)
                    if deeper:
                        results.extend(deeper)
                    else:
                        results.append((new_path, new_captured))
        return results

    capture_moves = dfs(board, r, c, [(r, c)], [])
    if capture_moves:
        return capture_moves
    else:
        return simple_moves

def get_all_moves(board, color):
    moves = []
    for r in range(ROWS):
        for c in range(COLS):
            p = board[r][c]
            if p and ((color == 'r' and p.lower() == 'r') or (color == 'b' and p.lower() == 'b')):
                for mv in get_piece_moves(board, r, c):
                    moves.append(mv)
    captures = [m for m in moves if len(m[1]) > 0]
    if captures:
        return captures
    return moves

def apply_move(board, move):
    new_board = copy.deepcopy(board)
    path, captured = move
    r0, c0 = path[0]
    r1, c1 = path[-1]
    new_board[r1][c1] = new_board[r0][c0]
    new_board[r0][c0] = None
    for rr, cc in captured:
        new_board[rr][cc] = None
    if new_board[r1][c1].islower() and (r1 == 0 or r1 == ROWS-1):
        new_board[r1][c1] = new_board[r1][c1].upper()
    return new_board

def evaluate(board):
    val = 0
    for r in range(ROWS):
        for c in range(COLS):
            p = board[r][c]
            if p:
                v = 2 if p.isupper() else 1
                if p.lower() == 'r':
                    val += v
                else:
                    val -= v
    return val

def minimax(board, depth, alpha, beta, maximizing):
    if depth == 0:
        return evaluate(board), board
    color = 'r' if maximizing else 'b'
    moves = get_all_moves(board, color)
    if not moves:
        return evaluate(board), board
    if maximizing:
        max_eval = -math.inf
        best_move = None
        for move in moves:
            nb = apply_move(board, move)
            val, _ = minimax(nb, depth-1, alpha, beta, False)
            if val > max_eval:
                max_eval = val
                best_move = nb
            alpha = max(alpha, val)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        best_move = None
        for move in moves:
            nb = apply_move(board, move)
            val, _ = minimax(nb, depth-1, alpha, beta, True)
            if val < min_eval:
                min_eval = val
                best_move = nb
            beta = min(beta, val)
            if beta <= alpha:
                break
        return min_eval, best_move

def check_winner(board):
    reds = sum(p.lower() == 'r' for row in board for p in row if p)
    blues = sum(p.lower() == 'b' for row in board for p in row if p)
    if reds == 0:
        return "Blue (AI)"
    if blues == 0:
        return "Red (You)"
    return None

def main():
    board = create_board()
    clock = pygame.time.Clock()
    run = True
    selected = None
    player_turn = True
    winner = None

    while run:
        clock.tick(30)
        draw_board(WIN, board)
        if winner:
            font = pygame.font.SysFont(None, 60)
            text = font.render(f"{winner} yutdi!", True, GREEN)
            WIN.blit(text, (WIDTH//2 - 150, HEIGHT//2 - 30))
            pygame.display.update()
            continue

        pygame.display.update()
        winner = check_winner(board)
        if not player_turn:
            _, best_move = minimax(board, 3, -math.inf, math.inf, False)
            board = best_move
            player_turn = True
            continue

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and player_turn:
                x, y = pygame.mouse.get_pos()
                r, c = y // SQUARE_SIZE, x // SQUARE_SIZE
                if selected:
                    moves = get_all_moves(board, 'r')
                    chosen = None
                    for m in moves:
                        if m[0][0] == selected and m[0][-1] == (r, c):
                            chosen = m
                            break
                    if chosen:
                        board = apply_move(board, chosen)
                        player_turn = False
                    selected = None
                else:
                    if board[r][c] and board[r][c].lower() == 'r':
                        selected = (r, c)

main()
  