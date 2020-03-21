import math
import threat

piece_val = [100, 300, 400, 500, 1025, 20000]
push_pieces_to_center = [
                   -20, -10, -10, -10, -10, -10, -10, -20,
                   -10, 0,   0,   0,   0,   0,   0,   -10,
                   0,   10,  10,  10,  10,  10,  10,  0,
    -20, -10, 0,   10,  20,  20,  30,  30,  20,  20,  10, 0,  -10, -20,
    -10, 0,   10,  20,  30,  30,  35,  35,  30,  30,  20, 10, 0,   -10,
    -10, 0,   10,  20,  30,  35,  35,  35,  35,  30,  20, 10, 0,   -10,
    -10, 0,   10,  30,  35,  35,  40,  40,  35,  35,  30, 10, 0,   -10,
    -10, 0,   10,  30,  35,  35,  40,  40,  35,  35,  30, 10, 0,   -10,
    -10, 0,   10,  20,  30,  35,  35,  35,  35,  30,  20, 10, 0,   -10,
    -10, 0,   10,  20,  30,  30,  35,  35,  30,  30,  20, 10, 0,   -10,
    -20, -10, 0,   10,  20,  20,  30,  30,  20,  20,  10, 0,  -10, -20,
                   0,   10,  10,  10,  10,  10,  10,  0,
                   -10, 0,   0,   0,   0,   0,   0,   -10,
                   -20, -10, -10, -10, -10, -10, -10, -20
]
opening_positional = [[
                   0,   0,   0,   0,   0,   0,   0,   0,
                   0,   0,   0,   0,   0,   0,   0,   0,
                   0,   0,   0,   0,   0,   0,   0,   0,
    50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,
    -10, -20, 10,  -20, 30,  30,  35,  35,  30,  30,  -20, 10,  -20, -10,
    -10, -20, 10,  -20, 30,  35,  35,  35,  35,  30,  -20, 10,  -20, -10,
    -10, -10, -20, -30, 35,  35,  30,  30,  35,  35,  -30, -20, -10, -10,
    5,   20,  -20, -30, -35, 35,  -15, -15, 35,  -35, -30, -20, 20,  5,
    -10, -15, 10,  15,  -30, 35,  35,  35,  35,  -30, 15,  10,  -15, -10,
    0,   15,  -10, 20,  -30, -10, -10, -10, -10, -30, 20,  -10, 15,  0,
    0,   0,   10,  25,  20,  40,  40,  40,  -10, 20,  25,  10,  0,   0,
                   -5,  10,  10,  20,  40,  -10, 10,  -5,
                   10,  10,  10,  10,  10,  10,  10,  10,
                   0,   0,   0,   0,   0,   0,   0,   0
], [
                 0,   0,   10,  -5,  10,  10,  10,  -50,
                 0,   -15, 20,  15,  15,  15,  15,  -50,
                 10,  -10, 20,  15,  15,  15,  15,  -50,
    0, -10, -5,  -5,  -10, -10, -10, -10, -10, -10, -50, 0, 0, 0,
    0, -10, -10, -10, 30,  30,  -10, 35,  30,  30,  -50, 0, 0, 0,
    0, -10, -20, 20,  30,  35,  35,  35,  35,  30,  -50, 0, 0, 0,
    0, -10, -20, 30,  35,  35,  15,  10,  35,  35,  -50, 0, 0, 0,
    0, -10, -40, -40, -35, 35,  15,  10,  35,  -35, -50, 0, 0, 0,
    0, -10, -20, -40, 20,  35,  35,  35,  35,  20,  -50, 0, 0, 0,
    0, -10, -10, -20, -30, 10,  -10, -10, -10, 20,  -50, 0, 0, 0,
    0, -10, -10, -5,  20,  -25, -25, -5,  -10, 20,  -50, 0, 0, 0,
                 -10, 10,  10,  20,  40,  -10, 10,  -50,
                 0,   -15, 10,  10,  10,  10,  10,  -50,
                 0,   0,   10,  -5,  10,  10,  10,  -50
], [
                   0,   0,   0,   0,   0,   0,   0,   0,
                   10,  10,  10,  10,  10,  10,  10,  10,
                   -5,  10,  10,  20,  40,  -10, 10,  -5,
    0,   0,   10,  25,  20,  40,  40,  40,  -10, 20,  25,  10,  0,   0,
    0,   15,  -10, 20,  -30, -10, -10, -10, -10, -30, 20,  -10, 15,  0,
    -10, -15, 10,  15,  -30, 35,  35,  35,  35,  -30, 15,  10,  -15, -10,
    5,   20,  -20, -30, -35, 35,  -15, -15, 35,  -35, -30, -20, 20,  5,
    -10, -10, -20, -30, 35,  35,  30,  30,  35,  35,  -30, -20, -10, -10,
    -10, -20, 10,  -20, 30,  35,  35,  35,  35,  30,  -20, 10,  -20, -10,
    -10, -20, 10,  -20, 30,  30,  35,  35,  30,  30,  -20, 10,  -20, -10,
    50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,  50,
                   0,   0,   0,   0,   0,   0,   0,   0,
                   0,   0,   0,   0,   0,   0,   0,   0,
                   0,   0,   0,   0,   0,   0,   0,   0
], [
             -50, 10,  10,  10,  -5,  10,  0,   0,  
             -50, 15,  15,  15,  15,  20,  -15, 0,  
             -50, 15,  15,  15,  15,  20,  -10, 10, 
    0, 0, 0, -50, -10, -10, -10, -10, -10, -10, -5,  -5,  -10, 0,
    0, 0, 0, -50, 30,  30,  35,  -10, 30,  30,  -10, -10, -10, 0,
    0, 0, 0, -50, 30,  35,  35,  35,  35,  30,  20,  -20, -10, 0,
    0, 0, 0, -50, 35,  35,  10,  15,  35,  35,  30,  -20, -10, 0,
    0, 0, 0, -50, -35, 35,  10,  15,  35,  -35, -40, -40, -10, 0,
    0, 0, 0, -50, 20,  35,  35,  35,  35,  20,  -40, -20, -10, 0,
    0, 0, 0, -50, 20,  -10, -10, -10, 10,  -30, -20, -10, -10, 0,
    0, 0, 0, -50, 20,  -10, -5,  -25, -25, 20,  -5,  -10, -10, 0,
             -50, 10,  -10, 40,  20,  10,  10,  -10,
             -50, 10,  10,  10,  10,  10,  -15, 0,  
             -50, 10,  10,  10,  -5,  10,  0,   0  
], [
               20,  25,  25,  40,  35,  25,  25,  20,
               15,  15,  15,  15,  15,  15,  15,  15,
               5,   5,   5,   5,   5,   5,   5,   5,
    20, 15, 5, -35, -35, -35, -35, -35, -35, -35, -35, 5, 15, 20,
    25, 15, 5, -35, -40, -40, -40, -40, -40, -40, -35, 5, 15, 25,
    25, 15, 5, -35, -40, -40, -40, -40, -40, -40, -35, 5, 15, 25,
    40, 15, 5, -35, -40, -40, -40, -40, -40, -40, -35, 5, 15, 35,
    35, 15, 5, -35, -40, -40, -40, -40, -40, -40, -35, 5, 15, 40,
    25, 15, 5, -35, -40, -40, -40, -40, -40, -40, -35, 5, 15, 25,
    25, 15, 5, -35, -40, -40, -40, -40, -40, -40, -35, 5, 15, 25,
    20, 15, 5, -35, -35, -35, -35, -35, -35, -40, -35, 5, 15, 20,
               5,   5,   5,   5,   5,   5,   5,   5,
               15,  15,  15,  15,  15,  15,  15,  15,
               20,  25,  25,  35,  40,  25,  25,  20
]]

def evaluate_material(board):
    """ Evaluate The Material """
    sum = 0
    for square in board:
        if square == 0:
            continue
        if square[0] == 0 or square[0] == 2:
            sum += piece_val[square[1]]
        else:
            sum += -piece_val[square[1]]
    return sum

def evaluate_material_balance(board):
    """ Evaluate The Material Balance """
    sum = aa = bb = cc = dd = 0
    for square in board:
        if square == 0:
            continue
        if square[0] == 0:
            val = piece_val[square[1]]
            val /= 5
            aa += val
        elif square[0] == 1:
            val = piece_val[square[1]]
            val /= 5
            bb += -val
        elif square[0] == 2:
            val = piece_val[square[1]]
            val /= 5
            cc += val
        else:
            val = piece_val[square[1]]
            val /= 5
            dd += -val
    if aa > cc:
        sum += -(aa - cc)
    if cc > aa:
        sum += -(cc - aa)
    if bb > dd:
        sum += bb - dd
    if dd > bb:
        sum += dd - bb
    return sum

def evaluate_position(board, phase):
    """ Evaluate The Positional Play """
    sum = 0
    if phase == 1:
        start = 0
        for key, square in enumerate(board):
            if threat.valid_key(key):
                if square == 0:
                    continue
                if square[1] == 0:
                    sum += opening_positional[square[0]][start]
                if square[1] == 5:
                    if square[0] == 0 or square[0] == 2:
                        sum += opening_positional[4][start]
                    else:
                        sum += -opening_positional[4][start]
                start += 1
    else:
        start = 0
        for key, square in enumerate(board):
            if threat.valid_key(key):
                if square == 0:
                    continue
                if square[1] == 0:
                    """ Evaluate Endgame Pawns """
                else:
                    if square[0] == 0 or square[0] == 2:
                        sum += push_pieces_to_center[start]
                    else:
                        sum += -push_pieces_to_center[start]
                start += 1
    return sum

def evaluate(board, phase = 1):
    """ Evaluate The Pieces, Material Balance, And Positional Play """
    return evaluate_material(board) + evaluate_material_balance(board) + evaluate_position(board, phase)