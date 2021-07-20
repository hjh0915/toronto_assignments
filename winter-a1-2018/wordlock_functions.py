"""Starter code for CSC108 Assignment 1 Winter 2018"""

# Game setting constants
SECTION_LENGTH = 3
ANSWER = 'CATDOGFOXEMU'

# Move constants
SWAP = 'S'
ROTATE = 'R'
CHECK = 'C'

# Add any additional constants here

def get_section_start(section_num: int) -> int:
    """ Return the starting index of the section corresponding to section_num.
    
    >>> get_section_start(1)
    0
    >>> get_section_start(3)
    6
    """
    return (section_num - 1) * SECTION_LENGTH

def is_valid_move(move: str) -> bool:
    """
    Return True if and only if the move.
    """
    return move == SWAP or move == ROTATE or move == CHECK

def is_valid_section(number: int) -> bool:
    """Return True if and only if the number that is a valid for 
    the current answer string and section length.
    """
    return number <= len(ANSWER) / SECTION_LENGTH

def check_section(state: str, number: int) -> bool:
    """Return True if and only if the specified section in the game
    state matches the same section in the answer string.
    """
    start = (number - 1) * SECTION_LENGTH
    stop = start + SECTION_LENGTH
    return ANSWER[start:stop] == state[start:stop]

def change_state(state: str, n: int, move: str) -> str:
    """Return a new string that reflects the updated game state after
    applying the given move to the specified section.
    
    >>> SECTION_LENGTH = 4
    >>> change_state('wrdokoclgmae', 2, 'S')
    'wrdolockgmae'
    >>> change_state('ordwlockgmae', 1, 'R')
    ''wordlockgmae'
    """
    start = (n - 1) * SECTION_LENGTH
    stop = start + SECTION_LENGTH
    section = state[start:stop]
    if move == SWAP:
        s = section[-1] + section[1:-1] + section[0]
    if move == ROTATE:
        s = section[-1] + section[:-1]
    return state[:start] + s + state[stop:]

def get_move_hint(state: str, n: int) -> str:
    """Return a move that will help the player rearrange the 
    specified section correctly.
    >>> SECTION_LENGTH = 3
    """
    start = (n - 1) * SECTION_LENGTH
    stop = start + SECTION_LENGTH
    section = state[start:stop]

    #section做交换
    s = section[-1] + section[1:-1] + section[0]
    if s == ANSWER[start:stop]:
        return SWAP
    else:
        #下一步做轮转
        x = s[-1] + s[:-1]
        if x == ANSWER[start:stop]:
            return SWAP
        else:
            return ROTATE