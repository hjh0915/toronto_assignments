def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """

    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """

    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """

    num = 0
    for i in dna:
        if i == nucleotide:
            num += 1

    return num 


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False

    """

    return dna2 in dna1


def is_valid_sequence(dna):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid
    (that is, it contains no characters other than 'A', 'T', 'C' and 'G'.)
    
    >>> is_valid_sequence('ATCGGC')
    True
    >>> is_valid_sequence('ATCGGCBDJIO')
    False
    """

    seq = 'ATCG'
    for d in dna:
        if d not in seq:
            return False 
    return True


def insert_sequence(dna1, dna2, index):
    """ (str, str, int) -> str

    Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index. 
    (You can assume that the index is valid.)

    >>> insert_sequence('CCGG', 'AT', 2)
    'CCATGG'
    >>> insert_sequence('CCGG', 'AT', 0)
    'ATCCGG'
    """

    return dna1[:index] + dna2 + dna1[index:]


def get_complement(nucleotide):
    """ (str) -> str

    Return the nucleotide's complement. 

    """

    return nucleotide

def get_complementary_sequence(dna):
    """ (str) -> str

    Return the DNA sequence that is complementary to the given DNA sequence. 
    
    >>> get_complementary_sequence('ACCGTA')
    'TGGCAT'
    """

    s = ''
    for d in dna:
        if d == 'A':
            s += 'T'
        elif d == 'T':
            s += 'A'
        elif d == 'C':
            s += 'G'
        elif d == 'G':
            s += 'C'

    return s 