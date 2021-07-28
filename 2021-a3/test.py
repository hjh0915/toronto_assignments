import a3
import unittest

class Test(unittest.TestCase):
    def test_is_valid_word(self):
        wordlist = ['ANT', 'BOX', 'SOB', 'TO']
        word = 'TOO'
        expected = False
        result = a3.is_valid_word(wordlist, word)
        self.assertEqual(expected, result)

    def test_make_str_from_row(self):
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        row_index = 0
        expected = 'ANTT'
        result = a3.make_str_from_row(board, row_index)
        self.assertEqual(expected, result)

    def test_make_str_from_column(self):
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        column_index = 2 
        expected = 'TO'
        result = a3.make_str_from_column(board, column_index)
        self.assertEqual(expected, result)

    def test_board_contains_word_in_row(self):
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        word = 'SOB'
        expected = True
        result = a3.board_contains_word_in_row(board, word)
        self.assertEqual(expected, result)

    def test_board_contains_word_in_column(self):
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        word = 'ANT'
        expected = False
        result = a3.board_contains_word_in_column(board, word)
        self.assertEqual(expected, result)

    def test_board_contains_word(self):
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        word = 'ANT'
        expected = True
        result = a3.board_contains_word(board, word)
        self.assertEqual(expected, result)

    def test_num_words_on_board(self):
        board = [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]
        words = ['ANT', 'BOX', 'TT', 'TO', 'SOB']
        expected = 4
        result = a3.num_words_on_board(board, words)
        self.assertEqual(expected, result)

unittest.main()