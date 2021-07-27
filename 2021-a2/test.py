import a2
import unittest

class Test(unittest.TestCase):
    def test_get_length(self):
        dna = 'ATCGAT'
        expected = 6
        result = a2.get_length(dna)
        self.assertEqual(expected, result)

    def test_is_longer(self):
        dna1 = 'ATCG'
        dna2 = 'AT'
        expected = False
        result = a2.is_longer(dna2, dna1)
        self.assertEqual(expected, result)

    def test_count_nucleotides(self):
        dna = 'ATCGGC'
        nucl = 'G'
        expected = 2
        result = a2.count_nucleotides(dna, nucl)
        self.assertEqual(expected, result)

    def test_contains_sequence(self):
        dna1 = 'ATCGGC'
        dna2 = 'GT'
        expected = False
        result = a2.contains_sequence(dna1, dna2)
        self.assertEqual(expected, result)

    def test_is_valid_sequence(self):
        dna = 'ATCGGCKIO'
        expected = False
        result = a2.is_valid_sequence(dna)
        self.assertEqual(expected, result)

    def test_insert_sequence(self):
        dna1 = 'CCGG'
        dna2 = 'AT'
        index = 0
        expected = 'ATCCGG'
        result = a2.insert_sequence(dna1, dna2, index)
        self.assertEqual(expected, result)

    def test_get_complementary_sequence(self):
        dna = 'ACCGTA'
        expected = 'TGGCAT'
        result = a2.get_complementary_sequence(dna)
        self.assertEqual(expected, result)

unittest.main()