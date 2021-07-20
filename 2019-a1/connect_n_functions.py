"""The student written functions for the Connect-N game.
"""

from math import sqrt

# Do not change these constants!
EMPTY = '-'
DOWN = 'down'
ACROSS = 'across'
DOWN_RIGHT = 'down_right'
DOWN_LEFT = 'down_left'
MAX_BOARD_SIZE = 9


def between(value: int, min_value: int, max_value: int) -> bool:
    """Return True if and only if value is between min_value and
    max_value, inclusive.

    Precondition: min_value <= max_value

    >>> between(1, 0, 2)
    True
    >>> between(0, 2, 3)
    False
    """
    if value >= min_value and value <= max_value:
        return True
    else:
        return False

def game_board_full(game_board: str) -> bool:
    """仅当已选择游戏板上的所有单元时，此函数才返回
    仅当游戏板上没有EMPTY字符，则返回
    >>> game_border('ASDFG-')
    False
    >>> game_border('ASDBFEW')
    True
    """
    if EMPTY not in game_board:
        return True
    else:
        return False

def get_board_size(game_board: str) -> int:
    """返回给定游戏板每侧的长度
    >>> game_board('ABDF')
    2
    >>> game_board('ANSOEITNS')
    3
    """
    return int(sqrt(len(game_board)))

def create_empty_board(board_size: int) -> str:
    """创建一个空游戏板，返回的字符串中的每个字符都将被
    设置为EMPTY字符
    >>> create_empty_board(3)
    '---------'
    >>> create_empty_board(1)
    '-'
    >>> create_empty_board(2)
    '----'
    """
    return EMPTY * (board_size ** 2)

def get_str_index(row: int, col: int, board_size: int) -> int:
    """返回游戏板的字符串表示形式中与给定行和列索引相对应的索引
    >>> get_str_index(1, 1, 4)
    0
    >>> get_str_index(3, 4, 4)
    11
    """
    str_index = (row-1) * board_size + (col-1)
    return str_index 

def make_move(symbol: str, row: int, col: int, game_board: str) -> str:
    """返回将给定符号放置在给定游戏板中给定单元位置时所得到的游戏板
    >>> make_move('R', 2, 2, 'RBR-B-R--')
    'RBRR'
    """
    board_size = get_board_size(game_board)
    str_index = get_str_index(row, col, board_size)
    if str_index == 0:
        x = symbol + game_board[1:]
    elif str_index == len(game_board)-1:
        x = game_board[:len(game_board)-1] + symbol
    else:
        x = game_board[:str_index] + symbol + game_board[str_index+1:]
    return x
    
def get_increment(direction: str, board_size: int) -> int:
    """返回沿direction指定的方向的一行上两个相邻单元的索引之间的差
    >>> get_increment('down_left', 3)
    2
    >>> get_increment('down', 2)
    2
    """
    if board_size == 1:
        increment = 0
    else:
        if direction == DOWN:
            increment = board_size
        elif direction == DOWN_LEFT:
            increment = board_size - 1
        elif direction == DOWN_RIGHT:
            increment = board_size + 1
        elif direction == ACROSS:
            increment = 1
    return increment

def get_last_index(row: int, col: int, direction: str, board_size: int) -> int:
    """返回direction指定大小的游戏板上从指定位置开始并沿指定方向一直到达游戏板边界的行中最后一个单元格的索引
    >>> get_last_index(1, 3, 'down_left', 3)
    6
    """
    str_index = get_str_index(row, col, board_size)
    increment = get_increment(direction, board_size)

    i = 1
    found = False
    while not found:
        str_index = str_index + increment
        nrow = str_index // board_size + 1
        ncol = str_index % board_size + 1
        
        if nrow > board_size or ncol > board_size:
            found = True
        
        if direction == ACROSS:
            if nrow != row:
                found = True

        if direction == DOWN:
            if ncol != col:
                found = True 

        if direction == DOWN_LEFT:
            if row+col != nrow+ncol:
                found = True
        
        if direction == DOWN_RIGHT:
            if nrow != row + i or ncol != col + i:
                found = True

        i += 1

    return str_index - increment

    # complete the implementation of this function


# Implement the rest of the required functions here.


if __name__ == '__main__':
    
    import doctest

    # Uncomment this line to run the examples in your docstrings.
    doctest.testmod()
