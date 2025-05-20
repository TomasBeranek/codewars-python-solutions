# Task:

# Capture pieces on a chessboard where each capture transforms the capturing piece
# into the captured piece.
# Inputs:

# (1) A two-dimensional array, representing a position on a 8 x 8 chessboard. The
# board will contain exactly one of each piece ('B' for bishop, 'K' for king, 'N'
# for knight, 'P' for pawn, 'Q' for queen, 'R' for rook). The king can be captured
# like any other piece.
# (2) A single letter representing the piece to start capturing with.
# Output:

# A list of the pieces remaining on the board after the sequence of captures
# terminates, sorted alphabetically.
# Example:

# Consider the following position, shown as an 2d-array on the right but probably
# clearer as displayed on the left.

#  ....R...                 [ ['.', '.', '.', '.', 'R', '.', '.', '.'],
#  ........                   ['.', '.', '.', '.', '.', '.', '.', '.'],
#  .K..N...                   ['.', 'K', '.', '.', 'N', '.', '.', '.'],
#  B.P.....                   ['B', '.', 'P', '.', '.', '.', '.', '.'],
#  ........                   ['.', '.', '.', '.', '.', '.', '.', '.'],
#  ........                   ['.', '.', '.', '.', '.', '.', '.', '.'],
#  ...Q....                   ['.', '.', '.', 'Q', '.', '.', '.', '.'],
#  ........                   ['.', '.', '.', '.', '.', '.', '.', '.'] ]

# Suppose the starting piece is 'Q'. The queen can capture the bishop. The inputs
# are generated so that it will always be the case that at each step either only
# one capture or no captures are possible. Capturing the bishop transforms the
# queen into a bishop. The bishop can then capture the king, transforming into a
# king. The king can then capture the pawn, transforming into a pawn. The pawn has
# no possible captures (pawns always move up the board). The function should return
# ['N', 'P', 'R'], the pieces remaining on the board in alphabetical order.

# Suppose the starting piece is 'R'. The rook captures the knight, which captures
# the pawn, which captures the king, which captures the bishop, which captures the
# queen, which is the only piece left on the board. The function should return ['Q'].

# If the starting piece was 'B', there would be two possible captures, either the
# king or the queen. It is guaranteed that such inputs will never occur.

# This kata was inspired by Transforming Chess Piece Puzzle, as well as the
# challenges at the website Echo Chess.

# For other kata related to capturing chess pieces, see Explain the Algebraic
# Chess Notation as well as The Capturing Rook and Losing Chess.


all_pieces = ['B', 'K', 'N', 'P', 'Q', 'R']


def find_piece(board, piece):
    for y, row in enumerate(board):
        if piece in row:
            return row.index(piece), y, piece
    return None, None, piece


def coords_are_valid(tile):
    x, y = tile
    return 0 <= x <= 7 and 0 <= y <= 7


def check_for_intersection(possible_tiles, occupied_tiles):
    possible_tiles = [
        tile for tile in possible_tiles if coords_are_valid(tile)]
    possible_take = list(set(possible_tiles) & set(occupied_tiles.keys()))

    if len(possible_take):
        x, y = possible_take[0]
        return x, y, occupied_tiles[possible_take[0]]
    else:
        return None, None, None


def bishops_reachable_tiles(x, y):
    possible_tiles = []
    for i in range(1, 8):
        possible_tiles += [(x+i, y+i), (x-i, y+i), (x-i, y-i), (x+i, y-i)]
    return possible_tiles


def kings_reachable_tiles(x, y):
    return [(x+1, y-1), (x+1, y), (x+1, y+1), (x, y+1), (x-1, y+1), (x-1, y), (x-1, y-1), (x, y-1)]


def rooks_reachable_tiles(x, y):
    possible_tiles = []
    for i in range(1, 8):
        possible_tiles += [(x+i, y), (x, y+i), (x-i, y), (x, y-i)]
    return possible_tiles


def bishop_can_capture(board, occupied_tiles, x, y):
    possible_tiles = bishops_reachable_tiles(x, y)
    return check_for_intersection(possible_tiles, occupied_tiles)


def king_can_capture(board, occupied_tiles, x, y):
    possible_tiles = kings_reachable_tiles(x, y)
    return check_for_intersection(possible_tiles, occupied_tiles)


def knight_can_capture(board, occupied_tiles, x, y):
    possible_tiles = [(x+2, y+1), (x+2, y-1), (x+1, y+2),
                      (x-1, y+2), (x-2, y+1), (x-2, y-1), (x-1, y-2), (x+1, y-2)]
    return check_for_intersection(possible_tiles, occupied_tiles)


def pawn_can_capture(board, occupied_tiles, x, y):
    possible_tiles = [(x-1, y-1), (x+1, y-1)]
    return check_for_intersection(possible_tiles, occupied_tiles)


def queen_can_capture(board, occupied_tiles, x, y):
    possible_tiles = kings_reachable_tiles(x, y)
    possible_tiles += bishops_reachable_tiles(x, y)
    possible_tiles += rooks_reachable_tiles(x, y)
    return check_for_intersection(possible_tiles, occupied_tiles)


def rook_can_capture(board, occupied_tiles, x, y):
    possible_tiles = rooks_reachable_tiles(x, y)
    return check_for_intersection(possible_tiles, occupied_tiles)


def capture_pieces(board, piece):
    piece_can_capture = {'B': bishop_can_capture,
                         'K': king_can_capture,
                         'N': knight_can_capture,
                         'P': pawn_can_capture,
                         'Q': queen_can_capture,
                         'R': rook_can_capture}

    pieces_positions = [find_piece(board, p) for p in all_pieces]
    occupied_tiles = {(x, y): p for x, y,
                      p in pieces_positions if x is not None}
    x, y, _ = find_piece(board, piece)

    while True:
        x_new, y_new, captured_piece = piece_can_capture[piece](
            board, occupied_tiles, x, y)
        if captured_piece is None:
            break

        occupied_tiles.pop((x, y))
        x, y, piece = x_new, y_new, captured_piece

    return list(occupied_tiles.values())
