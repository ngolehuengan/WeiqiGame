from __future__ import print_function
def eprint(*args, **kwargs): print(*args, file=sys.stderr, **kwargs)
import sys
import random
VERSION = '1.0'

board_9x9 = [
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 1, 2, 0, 0, 0, 0, 7,
    7, 0, 2, 1, 1, 2, 0, 0, 0, 0, 7,
    7, 0, 0, 2, 1, 2, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 2, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]

coords_9x9 = [
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX',
    'XX', 'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'J9', 'XX',
    'XX', 'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'J8', 'XX',
    'XX', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'J7', 'XX',
    'XX', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'J6', 'XX',
    'XX', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'J5', 'XX',
    'XX', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'J4', 'XX',
    'XX', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'J3', 'XX',
    'XX', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'J2', 'XX',
    'XX', 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'J1', 'XX',
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'
]

board_13x13 = [
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]

coords_13x13 = [
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX',
    'XX', 'A13','B13','C13','D13','E13','F13','G13','H13','J13','K13','L13','M13','N13','XX',
    'XX', 'A12','B12','C12','D12','E12','F12','G12','H12','J12','K12','L12','M12','N12','XX',
    'XX', 'A11','B11','C11','D11','E11','F11','G11','H11','J11','K11','L11','M11','N11','XX',
    'XX', 'A10','B10','C10','D10','E10','F10','G10','H10','J10','K10','L10','M10','N10','XX',
    'XX', 'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'J9', 'K9', 'L9', 'M9', 'N9', 'XX',
    'XX', 'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'J8', 'K8', 'L8', 'M8', 'N8', 'XX',
    'XX', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'J7', 'K7', 'L7', 'M7', 'N7', 'XX',
    'XX', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'J6', 'K6', 'L6', 'M6', 'N6', 'XX',
    'XX', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'J5', 'K5', 'L5', 'M5', 'N5', 'XX',
    'XX', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'J4', 'K4', 'L4', 'M4', 'N4', 'XX',
    'XX', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'J3', 'K3', 'L3', 'M3', 'N3', 'XX',
    'XX', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'J2', 'K2', 'L2', 'M2', 'N2', 'XX',
    'XX', 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'J1', 'K1', 'L1', 'M1', 'N1', 'XX',
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'
]

board_19x19 = [
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7,
    7, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7,
    7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7
]

coords_19x19 = [
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX',
    'XX', 'A19','B19','C19','D19','E19','F19','G19','H19','J19','K19','L19','M19','N19','O19','P19','Q19','R19','S19','T19','XX',
    'XX', 'A18','B18','C18','D18','E18','F18','G18','H18','J18','K18','L18','M18','N18','O18','P18','Q18','R18','S18','T18','XX',
    'XX', 'A17','B17','C17','D17','E17','F17','G17','H17','J17','K17','L17','M17','N17','O17','P17','Q17','R17','S17','T17','XX',
    'XX', 'A16','B16','C16','D16','E16','F16','G16','H16','J16','K16','L16','M16','N16','O16','P16','Q16','R16','S16','T16','XX',
    'XX', 'A15','B15','C15','D15','E15','F15','G15','H15','J15','K15','L15','M15','N15','O15','P15','Q15','R15','S15','T15','XX',
    'XX', 'A14','B14','C14','D14','E14','F14','G14','H14','J14','K14','L14','M14','N14','O14','P14','Q14','R14','S14','T14','XX',
    'XX', 'A13','B13','C13','D13','E13','F13','G13','H13','J13','K13','L13','M13','N13','O13','P13','Q13','R13','S13','T13','XX',
    'XX', 'A12','B12','C12','D12','E12','F12','G12','H12','J12','K12','L12','M12','N12','O12','P12','Q12','R12','S12','T12','XX',
    'XX', 'A11','B11','C11','D11','E11','F11','G11','H11','J11','K11','L11','M11','N11','O11','P11','Q11','R11','S11','T11','XX',
    'XX', 'A10','B10','C10','D10','E10','F10','G10','H10','J10','K10','L10','M10','N10','O10','P10','Q10','R10','S10','T10','XX',
    'XX', 'A9', 'B9', 'C9', 'D9', 'E9', 'F9', 'G9', 'H9', 'J9', 'K9', 'L9', 'M9', 'N9', 'O9', 'P9', 'Q9', 'R9', 'S9', 'T9', 'XX',
    'XX', 'A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8', 'J8', 'K8', 'L8', 'M8', 'N8', 'O8', 'P8', 'Q8', 'R8', 'S8', 'T8', 'XX',
    'XX', 'A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7', 'J7', 'K7', 'L7', 'M7', 'N7', 'O7', 'P7', 'Q7', 'R7', 'S7', 'T7', 'XX',
    'XX', 'A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6', 'J6', 'K6', 'L6', 'M6', 'N6', 'O6', 'P6', 'Q6', 'R6', 'S6', 'T6', 'XX',
    'XX', 'A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5', 'J5', 'K5', 'L5', 'M5', 'N5', 'O5', 'P5', 'Q5', 'R5', 'S5', 'T5', 'XX',
    'XX', 'A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4', 'J4', 'K4', 'L4', 'M4', 'N4', 'O4', 'P4', 'Q4', 'R4', 'S4', 'T4', 'XX',
    'XX', 'A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3', 'J3', 'K3', 'L3', 'M3', 'N3', 'O3', 'P3', 'Q3', 'R3', 'S3', 'T3', 'XX',
    'XX', 'A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'J2', 'K2', 'L2', 'M2', 'N2', 'O2', 'P2', 'Q2', 'R2', 'S2', 'T2', 'XX',
    'XX', 'A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'J1', 'K1', 'L1', 'M1', 'N1', 'O1', 'P1', 'Q1', 'R1', 'S1', 'T1', 'XX',
    'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX', 'XX'
]

BOARDS = {
     '9': board_9x9,
    '13': board_13x13,
    '19': board_19x19
}

COORDS = {
     '9': coords_9x9,
    '13': coords_13x13,
    '19': coords_19x19,
}

EMPTY = 0
BLACK = 1
WHITE = 2
MARKER = 4
OFFBOARD = 7
LIBERTY = 8

#toạ độ của quân cờ đã đặt
liberties = []
#toạ độ xung quanh quân cờ đã đặt
block = []
board = None
coords = None

BOARD_WIDTH = 0
BOARD_RANGE = 0
MARGIN = 2

files = '     a b c d e f g h j k l m n o p q r s t'

pieces = '.BW  bw +'

def print_board():
    for row in range(BOARD_RANGE):
        for col in range(BOARD_RANGE):
            # đánh số cho từng vị trí trong bàn cờ
            square = row * BOARD_RANGE + col
            
            # gán giá trị hiện tại trong bàn cờ
            stone = board[square]
            
            if col == 0 and row > 0 and row < BOARD_RANGE - 1:
                rank = BOARD_RANGE - 1 - row
                space = '  ' if len(board) == 121 else '   '
                print((space if rank < 10 else '  ') + str(rank), end='')
            print(pieces[stone] + ' ', end='')
        print()
    print(('' if len(board) == 121 else ' ') + files[0:BOARD_RANGE*2] + '\n')

def set_board_size(command):
    global BOARD_WIDTH, BOARD_RANGE, board, coords
    size = int(command.split()[-1])
    
    if size not in [9, 13, 19]:
        print('? current board size not supported\n')
        return
    
    BOARD_WIDTH = size
    BOARD_RANGE = BOARD_WIDTH + MARGIN
    board = BOARDS[str(size)]
    coords = COORDS[str(size)]

def count(square, color):
    piece = board[square]
    if piece == OFFBOARD: return
    
    # KT có quân ở vị trí hiện tại / có trùng màu đang xét / có đánh dấu chưa
    if piece and piece & color and (piece & MARKER) == 0:
        # lưu toạ độ
        block.append(square)
        
        # đánh dấu quân cờ
        board[square] |= MARKER
        
        # tìm khí xung quanh quân cờ / chạy từ 0
        count(square - BOARD_RANGE, color) # Bắc
        count(square - 1, color)           # Đông
        count(square + BOARD_RANGE, color) # Nam
        count(square + 1, color)           # Tây
    
    # nếu chưa có quân
    elif piece == EMPTY:
        # đánh dấu ô đó
        board[square] |= LIBERTY
        
        # lưu toạ độ tự do
        liberties.append(square)

# xoá quân khi ăn
def clear_block():
    for captured in block: board[captured] = EMPTY

# khi bắt đầu ván mới
def clear_groups():
    global block, liberties
    block = []
    liberties = []

def restore_board():
    clear_groups()
    for square in range(BOARD_RANGE * BOARD_RANGE):
        # điểm đánh dấu bị xoá, quân cờ vẫn được giữ lại
        if board[square] != OFFBOARD: board[square] &= 3

def clear_board():
    clear_groups()
    for square in range(len(board)):
        if board[square] != OFFBOARD: board[square] = 0

# đặt cờ
def set_stone(square, color):
    board[square] = color
    captures(3 - color)

def play(command):
    color = BLACK if command.split()[1] == 'B' else WHITE
    if command.split()[-1] == 'pass': return
    
    square_str = command.split()[-1]
    col = ord(square_str[0]) - ord('A') + 1 - (1 if ord(square_str[0]) > ord('I') else 0)
    row_count = int(square_str[1:]) if len(square_str[1:]) > 1 else ord(square_str[1:]) - ord('0')
    row = (BOARD_RANGE - 1) - row_count
    square = row * BOARD_RANGE + col
    set_stone(square, color)

def captures(color):
    for square in range(len(board)):
        piece = board[square]
        
        if piece == OFFBOARD: continue
        
        if piece & color:
            count(square, color)
            
            if len(liberties) == 0: clear_block()
            
            restore_board()

def detect_edge(square):
    for direction in [BOARD_RANGE, 1, -BOARD_RANGE, -1]:
        if board[square + direction] == OFFBOARD: return 1
    return 0

def evaluate(color):
    best_count = 0
    best_liberty = liberties[0]
    
    for liberty in liberties:
        board[liberty] = color
        
        count(liberty, color)
        
        if len(liberties) > best_count and not detect_edge(liberty):
            best_liberty = liberty
            best_count = len(liberties)
            
        restore_board()
        board[liberty] = EMPTY
    return best_liberty

def gtp():
    while True:
        command = input()
        
        # handle commands
        if 'name' in command: print('= GoGame\n')
        elif 'protocol_version' in command: print('= 1\n')
        elif 'version' in command: print('=', VERSION, '\n')
        elif 'list_commands' in command: print('= protocol_version\n')
        elif 'boardsize' in command: set_board_size(command); print('=\n'); print_board(); print('=\n')
        elif 'clear_board' in command: clear_board(); print('=\n')
        elif 'play' in command: play(command); print('=\n'); print_board(); print('=\n')
        elif 'quit' in command: sys.exit()
        else: print('=\n') # skip currently unsupported commands

gtp()
