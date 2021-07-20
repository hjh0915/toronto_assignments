"""Assignment 2: DNA Manipulation"""

from typing import List
import palindromes


CYTOSINE = 'C'
GUANINE = 'G'
ADENINE = 'A'
THYMINE = 'T'


####### BEGIN PROVIDED HELPER FUNCTION ####################

def get_complementary_base(base: str) -> str:
    """Return the complement of base.

    Precondition: base in 'ATCG', base is not empty

    >>> get_complementary_base('A')
    'T'
    >>> get_complementary_base('C')
    'G'
    """

    if base == ADENINE:
        return THYMINE
    elif base == THYMINE:
        return ADENINE
    elif base == CYTOSINE:
        return GUANINE
    else:  # base == GUANINE
        return CYTOSINE


####### END PROVIDED HELPER FUNCTION ####################


# Delete these two lines and write your Task 2 code here.  Don't forget to
# run a2_simple_checker.py to check parameter and return types, and style!

def is_base_pair(base1: str, base2: str) -> bool:
    """当且仅当两个参数形成一个碱基对时才True
    >>> is_base_pair('A', 'T')
    True
    >>> is_base_pair('A', 'C')
    False
    """
    x = get_complementary_base(base1)
    if x == base2:
        return True
    return False

def are_complementary(strands1: str, strands2: str) -> bool:
    """当两个字符串相等时，即为碱基对，则返回True
    >>> are_complementary('GGATC', 'CCTAG')
    True
    >>> are_complementary('GGATC', 'AGSET')
    False
    """
    s = ""
    for x in strands1:
        y = get_complementary_base(x)
        s += y 
    if s == strands2:
        return True
    else:
        return False

def is_dna_palindrome(strands1: str, strands2: str) -> bool:
    """当strands1的对应链为strands2时，再通过palindromes.py中的is_palindrome_phrase
    函数判断是否strands2为strands1的回文DNA
    >>> is_dna_palindrome('GGCC', 'CCGG')
    True
    >>> is_dna_palindrome('GGACATA', 'CCTGTAT')
    False
    """
    if are_complementary(strands1, strands2):
        if strands2 == strands1[::-1]:
            return True
        return False

def restriction_sites(strand: str, words: str) -> List[int]:
    """返回的列表中的索引是DNA链中每次出现识别序列开始的索引,注意从左到右的
    顺序
    >>> restriction_sites('AGGCCTAGC', 'GGCC')
    [1]
    >>> restriction_sites('AGGCCTAGGCC', 'GGCC')
    [1, 7]
    >>> restriction_sites('GGCCTAGC', 'GGCC')
    [0]
    >>> restriction_sites('GGCCTAGC', 'AATT')
    []
    """
    x = []
    i = 0
    length = len(words)
    while i<len(strand):
        s = ""
        if strand[i] == words[0]:
            s += strand[i: i+length]
        if s == words:
            x.append(i)
        i += 1
    return x

def match_enzymes(strand: str, names: List[str], sequences: List[str]) -> List[list]:
    """返回一个包含两个内容的列表，其中第一项是限制酶的名称，第二个是限制酶索引列表
    >>> match_enzymes('GGATCC', ['EcoRI', 'BamHI', 'HindIII', 'TaqI', 'NotI'], ['GAATTC', 'GGATCC', 'AAGCTT', 'TCGA', 'GCGGCCGC'])
    [['BamHI', [0]]]
    >>> match_enzymes('ATTTCGAGCCGGATCC', ['EcoRI', 'BamHI', 'TaqI', 'NotI'], ['GAATTC', 'GGATCC', 'TCGA', 'GCGGCCGC'])
    [['BamHI', [10]], ['TaqI', [3]]]
    """
    x = []
    for i, sequence in enumerate(sequences):
        enzyme = []
        if sequence in strand:
            name = names[i]
            enzyme.append(name)
            ind = restriction_sites(strand, sequence)
            enzyme.append(ind)
            x.append(enzyme)
    return x

def one_cutters(strand: str, names: List[str], sequences: List[str]) -> List[list]:
    """返回一个包含两个内容的列表，第一个是限制酶的名称，第二个是该酶切割的一个限制位点的索引
    >>> one_cutters('ATTGCCGGATCC', ['EcoRI', 'BamHI', 'TaqI'], ['GAATTC', 'GGATCC', 'TCGA'])
    [['BamHI', 6]]
    >>> one_cutters('GGATCCGAAGGAATGGATCCTGAGAATTC', ['EcoRI', 'BamHI'], ['GAATTC', 'GGATCC'])
    [['EcoRI', 23], ['BamHI', 0]]
    """
    x = []
    for i, sequence in enumerate(sequences):
        cutters = []
        if sequence in strand:
            enzymes = names[i]
            cutters.append(enzymes)
            y = restriction_sites(strand, sequence)
            cutters.append(y[0])
            x.append(cutters)
    return x


def replace_mutations(mutated_strands: List[str], clean: str, names: List[str], sequences: List[str]) -> None:
    """clean_strands与mutated_strands中都有同一个cutter切割，将mutated_strands中从切割位的索引
    位置开始的所有碱基都替换为clean_strands中的由cutter开始切割的索引位置之后的所有碱基，直到mutated_strands
    的末端
    >>> mutated_strands = ['ACGTGGCCTAGCT', 'CAGCTGATCG']
    >>> clean = 'ACGGCCTT'
    >>> names = ['HaeIII', 'HgaI', 'AluI']
    >>> sequences = ['GGCC', 'GACGC', 'AGCT']
    >>> replace_mutations(mutated_strands, clean, names, sequences)
    >>> mutated_strands
    ['ACGTGGCCTT', 'CAGCTGATCG']
    """
    for sequence in sequences:
        for strand in mutated_strands:
            s = ""
            if sequence in strand and sequence in clean:
                i = mutated_strands.index(strand)
                x = restriction_sites(clean, sequence)
                y = restriction_sites(strand, sequence)
                s += strand[0: y[0]] + clean[x[0]: len(clean)]
                mutated_strands[i] = s 


if __name__ == '__main__':
    # pass

    # Uncomment the next two lines to run the examples in your docstrings.
    import doctest
    doctest.testmod()
