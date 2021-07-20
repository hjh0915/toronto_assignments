"""Phrase Puzzler: functions"""

# Phrase Puzzler constants

# Name of file containing puzzles
DATA_FILE = 'puzzles_small.txt'

# Letter values
CONSONANT_POINTS = 1
VOWEL_PRICE = 1
CONSONANT_BONUS = 2

# Players' names
PLAYER_ONE = 'Player One'
PLAYER_TWO = 'Player Two'

# Menu options - includes letter types
CONSONANT = 'C'
VOWEL = 'V'
SOLVE = 'S'
QUIT = 'Q'


# Define your functions here.

def is_win(puzzle: str, view: str) -> bool:
    """Return True if and only if puzzle is the same as view.

    >>> is_win('banana', 'banana')
    True
    >>> is_win('apple', 'a^^le')
    False
    """
    return view == puzzle


def game_over(puzzle: str, view: str, selection: str) -> bool:
    """Return True if and only if the puzzle is the same as the view or
    the current selection is QUIT.

    >>> game_over('melon', 'melon', VOWEL)
    True
    >>> game_over('pear', 'pe^^', QUIT)
    True
    >>> game_over('peach', 'pea^h', SOLVE)
    False
    """
    return puzzle == view or selection == QUIT

def bonus_letter(puzzle: str, view: str, letter: str) -> bool:
    """Return True if and only if the letter appears in the puzzle but
    not in its view.

    >>> bonus_letter('panda', 'pende', 'a')
    True
    >>> bonus_letter('monkey', 'banana', 'n')
    False
    """
    return (letter in puzzle) and (letter not in view) 

def update_letter_view(puzzle: str, view: str, index: int, letter: str) -> str:
    """ Retrun a single character string representing the next view of the 
    character at the given index. if the character at that index of the 
    puzzle matches the guess,then return that character.Otherwise, return 
    the character at that index of the view.
    """
    if puzzle[index] == letter:
        return puzzle[index]
    else:
        return view[index]

def calculate_score(score: int, number: int, letter: str) -> int:
    """Return the new score by adding CONSONANT_POINTS per occurence
    of the letter to the current score if the letter is a consonant,
    or by deducting the VOWEL_PRICE from the score if the letter is a vowel.
    """
    if letter in 'aeiou':
        return VOWEL_PRICE * number + score 
    else:
        return CONSONANT_POINTS * number + score 

def next_player(current_player: str, number: int):
    """Return the next player.
    """
    if number > 0:
        return current_player 
    else:
        if current_player == PLAYER_ONE:
            return PLAYER_TWO
        if current_player == PLAYER_TWO:
            return PLAYER_ONE 




if __name__ == '__main__':
    import doctest
    doctest.testmod()
